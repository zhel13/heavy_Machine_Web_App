from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from part.forms import SearchPartForm
from part.models import Part
from user_profile.forms import UserProfileForm


# def part_home(request: HttpRequest) -> HttpResponse:
#     ...
#
# def part_add(request: HttpRequest) -> HttpResponse:
#     ...
#
# def part_details(request: HttpRequest) -> HttpResponse:
#     ...
#
# def part_remove(request: HttpRequest) -> HttpResponse:
#     ...
def dashboard(request: HttpRequest) -> HttpResponse:
    form = SearchPartForm(request.GET or None)
    parts = Part.objects.all()

    if request.method == 'GET':
        if form.is_valid():
            query = form.cleaned_data['query']
            parts = Part.objects.filter(title__icontains=query)

    context = {
        'parts': parts,
        'form': form,
    }

    return render(request, 'dashboard.html', context)