from django.http import HttpResponse
from .models import User
import json
from django.forms.models import model_to_dict
from django.db.models import Q
import hashlib

def get_hash(s):
    sha256 = hashlib.sha256()
    sha256.update(s.encode('utf-8'))
    return sha256.hexdigest()

def login(request):
    body = json.loads(request.body.decode('utf-8'))
    user = User.objects.get(token=body["token"])
    return HttpResponse(json.dumps(model_to_dict(user)), status=200)

def signin(request):
    body = json.loads(request.body.decode('utf-8'))
    user = User.objects.get(Q(username=body["login"]) | Q(email=body["login"]) | Q(phone=body["login"]))
    if (get_hash(body["password"]) == user.password):
        return HttpResponse(json.dumps(model_to_dict(user)), status=200)
    else:
        return HttpResponse(json.dumps({
            "error": "Password is incorrect"
        }))
    
def signup(request):
    pass