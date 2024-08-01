from django.shortcuts import render
from .models import Food
from .forms import ListForm


def home(request):
    if request.method == "POST":  # Check whether the request method is post
        form = ListForm(request.POST or None)
        if form.is_valid():  # If input by user matches the input fields then only save in database
            form.save()
            context = Food.objects.all  # Get all the contents from the database
            return render(request, 'home.html', {'context': context})
    else:
        context = Food.objects.all  # Get all the contents from the database
        return render(request, 'home.html', {'context': context})
