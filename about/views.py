from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
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
        messages.success(request, 'Testimonial submitted for review')

  testimonial_form = TestimonialForm()
  
  return render(request, "about/about.html",
    {
      'about': about,
      'testimonial_form': testimonial_form,
      'testimonials': testimonials,
    },
  )

@login_required
def edit_testimonial(request, testimonial_id):
  """
  Allows users to edit existing testimonials they've submitted
  """
  testimonial = get_object_or_404(Testimonial, pk=testimonial_id, author=request.user)

  if request.method == "POST":
    testimonial_form = TestimonialForm(request.POST, instance=testimonial)
    if testimonial_form.is_valid():
      testimonial = testimonial_form.save(commit=False)
      testimonial.approved = 0
      testimonial.save()
      messages.success(request, "Successfully updated Testimonial!")
      return HttpResponseRedirect(reverse("about"))
    else:
      messages.error(request, "Failed to update Testimonial. Please ensure the form is valid.")

  return render(request, "about/about.html", {"testimonial_form": TestimonialForm(instance=testimonial)})


@login_required
def delete_testimonial(request, testimonial_id):
  """
  Allows users to delete existing testimonials they've submitted
  """
  testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
  testimonial.delete()
  messages.success(request, 'Testimonial deleted!')
  return redirect(reverse('about'))