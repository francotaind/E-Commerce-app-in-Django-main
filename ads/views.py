from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.conf import settings
import os

def serve_ads_txt(request):
    ads_txt_path = os.path.join(settings.BASE_DIR, 'ads.txt')
    if os.path.exists(ads_txt_path):
        with open(ads_txt_path, 'rb') as f:
            ads_txt_content = f.read()
        return HttpResponse(ads_txt_content, content_type='text/plain')
    else:
        return HttpResponse('ads.txt not found', status=404)

