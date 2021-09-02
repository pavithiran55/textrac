
from re import template
from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .forms import *   
import json
# Create your views here.
import pytesseract 
from PIL import Image, ImageFilter
from tesserocr import PyTessBaseAPI

@csrf_exempt
class OcrFormView(TemplateView):
    template_name = 'index.html'

def index(request, *args, **kwargs):
    if request.method == 'POST':
        img = OcrForm(request.POST,request.FILES)
        if img.is_valid():
            response_data = {}
            img.save()
            text = pytesseract.image_to_string(Image.open(img))
            response_data['text'] = text     
            
    else:
        img = OcrForm()
    return render(request, "index.html", {"form":img})

