from django.shortcuts import HttpResponse


def index(request):
    request.session["test"] = "test"
    return HttpResponse("Hello, world. You're at the polls index.")
