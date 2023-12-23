from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')


@login_required(login_url='/accounts/login-v1/')
def google_maps(request):
  context = {
    'parent': 'maps',
    'segment': 'google_maps',
    'api_key' : getattr(settings, 'GOOGLE_MAP_API_KEY')
  }
  return render(request, 'pages/chart-maps/map-google.html', context)