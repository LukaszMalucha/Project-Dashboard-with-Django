from django.shortcuts import render, get_object_or_404


def dashboard(request):

    return render(request, "dashboard.html")

