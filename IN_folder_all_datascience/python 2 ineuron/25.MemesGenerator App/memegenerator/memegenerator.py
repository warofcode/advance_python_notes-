import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import os

font_path = "static/fonts/Impact.ttf"


def gen_meme(image_name, top, bottom, meme_id):
    top = top.upper()
    bottom = bottom.upper()
    image_path = os.path.join('static/images', image_name)

    img = Image.open(str(image_path))
    imageSize = img.size

# find biggest font size that works
    fontSize = int(imageSize[1]/5)
    font = ImageFont.truetype(font_path, fontSize)
    topTextSize = font.getsize(top)
    bottomTextSize = font.getsize(bottom)
    while topTextSize[0] > imageSize[0]-20 or bottomTextSize[0] > imageSize[0]-20:
        fontSize = fontSize - 1
        font = ImageFont.truetype(font_path, fontSize)
        topTextSize = font.getsize(top)
        bottomTextSize = font.getsize(bottom)

# find top centered position for top text
    topTextPositionX = (imageSize[0]/2) - (topTextSize[0]/2)
    topTextPositionY = 0
    topTextPosition = (topTextPositionX, topTextPositionY)

# find bottom centered position for bottom text
    bottomTextPositionX = (imageSize[0]/2) - (bottomTextSize[0]/2)
    bottomTextPositionY = imageSize[1] - bottomTextSize[1]
    bottomTextPosition = (bottomTextPositionX, bottomTextPositionY)

    draw = ImageDraw.Draw(img)

# draw outlines
# there may be a better way
    outlineRange = int(fontSize/15)
    for x in range(-outlineRange, outlineRange+1):
        for y in range(-outlineRange, outlineRange+1):
            draw.text(
                (topTextPosition[0]+x, topTextPosition[1]+y), top, (0, 0, 0), font=font)
            draw.text(
                (bottomTextPosition[0]+x, bottomTextPosition[1]+y), bottom, (0, 0, 0), font=font)

    draw.text(topTextPosition, top, (255, 255, 255), font=font)
    draw.text(bottomTextPosition, bottom, (255, 255, 255), font=font)

    img.save("static/memes/%s.png" % meme_id)


if __name__ == '__main__':
    gen_meme("Hello", "World", "aliens")
