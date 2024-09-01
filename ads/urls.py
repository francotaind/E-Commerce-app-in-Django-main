from django.urls import path
from .views import serve_ads_txt

urlpatterns = [
    path('ads.txt', serve_ads_txt, name='ads_txt'),
]

