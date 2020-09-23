from django.shortcuts import render

from HierarchyApp.models import Monitor

def index_view(request):
    return render(request, 'homepage.html', {"monitors": Monitor.objects.all()})