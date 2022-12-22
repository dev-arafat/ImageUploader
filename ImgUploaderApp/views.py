from django.shortcuts import render, redirect
from .models import *
from .forms import ImageForm


def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'index.html', {'img': img, 'form': form})
