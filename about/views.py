from django.shortcuts import render
from .models import About

# Create your views here.
def about_us(request):
  """
  A view which renders the about page.
  """

  about = About.objects.all().last()

  return render(
    request, 
    "about/about.html",
    {"about": about,
    },
  )