""" Views for the base application """

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    """ Default view for the root """
    if request.user.is_authenticated():
        return redirect('/dash')
    return render(request, 'base/home.html')


@login_required
def dash(request):
    return render(request, 'dash.html')
