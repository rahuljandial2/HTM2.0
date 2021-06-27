from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from . models import User, Profile, VerifyKey

def varification_view(request, _key):
    verifykey = get_object_or_404(VerifyKey, key=_key)
    if verifykey.is_key_valid():
        verifykey.user.profile.activate()
        return HttpResponse('Done')
    return HttpResponse('Time\'s over')