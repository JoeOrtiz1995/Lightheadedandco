from django.shortcuts import render

# Create your views here.
def view_bag(request):
  """
  A view to return a page with the User's bag contents.
  """
  return render(request, 'bag/bag.html')
