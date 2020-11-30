from django.shortcuts import HttpResponse
# from .utils import signup
from .models import Signup
from .forms import SignupForm
import json


def subscribe(request):
    data = {

    }
    if request.is_ajax():
        email = request.POST.get('email' or None)
        if email is not None:
            subscriber = Signup.objects.filter(email=email)
            if subscriber.exists():
                data.update({'message': 'You are already subscribed to the mailing list.'})
            else:
                # signup(email)
                form = SignupForm(email)
                form.save()
                data.update({'message': 'You have successfully subscribed to the mailing list.'})
    return HttpResponse(json.dumps(data), content_type="application/json")
