from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from allauth.socialaccount.models import SocialAccount
import json

def mod_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous():
            return HttpResponseRedirect('/accounts/login')
        else:
            name = request.user.username
            user = SocialAccount.objects.get(user=request.user)
            data = user.extra_data
            if any("SketchDaily" in s for s in data):
                return func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(reverse('suggestion'))
    return wrapper


