from django.shortcuts import render
from .models import About, Testimonial

# Create your views here.
def about_us(request):
  """
  A view which renders the about page.
  """

  about = About.objects.all().last()
  testimonials = Testimonial.objects.all()
  
  # queryset = Testimonial.objects.filter(approved=1).order_by("created_on")
  # testimonial = get_object_or_404(Testimonial, pk=testimonial_id)

  # context = {
  #   'about': about,
  #   'testimonial': testimonial,
  # }

  return render(
    request,
    "about/about.html",
    {
      'about': about,
      'testimonials': testimonials,
    },
  )