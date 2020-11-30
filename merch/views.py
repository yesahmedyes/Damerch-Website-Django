from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


def nav(request):
    context = {
        'request_path': request.POST.get("path"),
        'user_auth': request.user.is_authenticated,
    }

    if request.is_ajax():
        template = render_to_string(request.POST.get("href"), context=context)
        return HttpResponse(template)


def my_404(request):
    return render(request, "base/404.html")

