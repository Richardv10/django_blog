from django.shortcuts import render
from .models import About

# Create your views here.

def about_me(request):
    """
    This function is to ask the server for the info to populate the page, the data is from the About class, and we store the 
    queryset in the variable <about> then the return statement is calling render( with three params, the request object, and the url pairs)
    """
    about = About.objects.all().order_by('-updated_on').first()
    return render(request, "about/about.html", {"about": about},)