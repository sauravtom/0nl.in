""" User profile views """

from backend.controller.app_controller import Controller
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def create_profile(request):
    """ Create a user profile """

    # Get app controller
    controller = Controller(request)
    data, html = controller.get_create_profile()

    return render(request, html, data)

def profile(request, id):
    """ Profile page of a user """

    # Get app controller
    controller = Controller(request)
    data, html = controller.get_profile_data(id)

    return render(request, html, data)

def edit_profile(request, id):
    """ Edit profile page of a user """

    # Get app controller
    controller = Controller(request)
    data, html = controller.get_edit_profile_data(id)

    return render(request, html, data)

def template1(request):
    """ Static template 1 for preview """

    data = {}
    html = 'static_templates/template1.html'
    return render(request, html, data)

def template2(request):
    """ Static template 2 for preview """

    data = {}
    html = 'static_templates/template2.html'
    return render(request, html, data)

def template3(request):
    """ Static template 3 for preview """

    data = {}
    html = 'static_templates/template3.html'
    return render(request, html, data)
