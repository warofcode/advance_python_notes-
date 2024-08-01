import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
import memegenerator
import dao

DATABASE = 'memegen.db'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return redirect(url_for("get_images"))


@app.route('/image', methods=['GET'])
def get_images():
    db_images = dao.get_images(get_db())
    form_data = dict()
    images = list()
    for image in db_images:
        html_image = dict()
        html_image['id_url'] = url_for('get_image', image_id=image[0])
        html_image['img_url'] = url_for('static',
                                        filename='images/%s' % image[1])
        images.append(html_image)
    form_data['images'] = images
    form_data['to_upload'] = True
    return render_template('grid.html', form_data=form_data)


@app.route('/image/<int:image_id>', methods=['GET'])
def get_image(image_id):
    image = dict()
    image['id'] = image_id
    image['name'] = dao.get_image_path(get_db(), image_id)
    return render_template('make_meme.html', image=image)


@app.route('/image', methods=['POST'])
def post_images():
    img = request.files['image']
    img.save('static/images/%s' % img.filename)
    img_id = dao.create_image(get_db(), img.filename)
    return redirect(url_for("get_image", image_id=img_id))


@app.route('/meme/<int:meme_id>', methods=['GET'])
def get_meme(meme_id):
    return redirect(url_for('static', filename='memes/%d.png' % meme_id))


@app.route('/meme', methods=['GET'])
def get_memes():
    db_images = dao.get_memes(get_db())
    form_data = dict()
    images = list()
    for image in db_images:
        html_image = dict()
        html_image['img_url'] = url_for('static',
                                        filename='memes/%d.png' % image[0])
        html_image['id_url'] = html_image['img_url']
        images.append(html_image)

    form_data['images'] = images
    form_data['to_upload'] = False
    return render_template('grid.html', form_data=form_data)


@app.route('/meme', methods=['POST'])
def post_meme():
    meme_id = dao.create_meme(get_db(),
                              int(request.form['image']),
                              request.form['top'],
                              request.form['bottom'])
    image_name = dao.get_image_path(get_db(),
                                    int(request.form['image']))
    memegenerator.gen_meme(image_name,
                           request.form['top'],
                           request.form['bottom'],
                           meme_id)
    return redirect(url_for('static', filename='memes/%d.png' % meme_id))


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_db()
    return db


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
