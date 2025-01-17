from django.shortcuts import render
from .models import About, Testimonial
from .forms import TestimonialForm

# Create your views here.
def about_us(request):
  """
  A view which renders the about page.
  """

  about = About.objects.all().last()
  testimonials = Testimonial.objects.all()

  if request.method == "POST":
    testimonial_form = TestimonialForm(data=request.POST)
    if testimonial_form.is_valid():
        testimonial = testimonial_form.save(commit=False)
        testimonial.author = request.user
        testimonial.save()

  testimonial_form = TestimonialForm()
  
  return render(
    request,
    "about/about.html",
    {
      'about': about,
      'testimonial_form': testimonial_form,
      'testimonials': testimonials,
    },
  )