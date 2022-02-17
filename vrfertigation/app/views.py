"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/home.html',
        {
            'title':'home',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def scene2(request):
    """Renders the scene2 page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/scene2.html',
        {
            'title':'Scene2',
            'message':'Your scene2page.',
            'year':datetime.now().year,
        }
    )
def scene3(request):
    """Renders the scene2 page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/scene3.html',
        {
            'title':'Scene3',
            'message':'Your scene3page.',
            'year':datetime.now().year,
        }
    )
def scene4(request):
    """Renders the scene4 page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/scene4.html',
        {
            'title':'Scene4',
            'message':'Your scene3page.',
            'year':datetime.now().year,
        }
    )
def scene5(request):
    """Renders the scene4 page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/scene5.html',
        {
            'title':'Scene5',
            'message':'Your scene3page.',
            'year':datetime.now().year,
        }
    )
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
           'title' : 'videoladang' 
        }
    )
