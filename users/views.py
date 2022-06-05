from django.http import HttpResponse
from .models import User
import json
from django.forms.models import model_to_dict
from django.db.models import Q
import hashlib
from datetime import datetime


def get_hash(s):
    sha256 = hashlib.sha256()
    sha256.update(s.encode('utf-8'))
    return sha256.hexdigest()


def login(request):
    user = User.objects.get(token=request.META.get("HTTP_AUTHORIZATION").split(" ")[1])
    return HttpResponse(json.dumps(model_to_dict(user)), status=200)


def signin(request):
    body = json.loads(request.body.decode('utf-8'))
    user = User.objects.get(Q(username=body["login"]) | Q(
        email=body["login"]) | Q(phone=body["login"]))
    if (get_hash(body["password"]) == user.password):
        result = model_to_dict(user)
        result["token"] = user.token
        return HttpResponse(json.dumps(result), status=200)
    else:
        return HttpResponse(json.dumps({
            "error": "Password is incorrect"
        }), status=422)


def signup(request):
    body = json.loads(request.body.decode('utf-8'))
    username_filter = Q(username=body["username"] if "username" in body.keys() else "")
    email_filter = Q(email=body["email"] if "email" in body.keys() else "")
    phone_filter = Q(phone=body["phone"] if "phone" in body.keys() else "")
    user = User.objects.filter(username_filter | email_filter | phone_filter)
    if (not user.exists()):
        user = User()
        user.username = body["username"]
        user.name = body["name"]
        user.bio = body["bio"] if "bio" in body.keys() else ""
        user.password = get_hash(body["password"])
        user.surname = body["surname"] if "surname" in body.keys() else ""
        user.verified = False
        user.banned = False
        user.email = body["email"] if "email" in body.keys() else ""
        user.phone = body["phone"] if "phone" in body.keys() else ""
        user.token = hashlib.md5(
            str(datetime.now().timestamp()).encode('utf-8')).hexdigest()
        user.save()
        result = model_to_dict(user)
        result["token"] = user.token
        return HttpResponse(json.dumps(result), status=200)
    else:
        return HttpResponse(json.dumps({
            "error": "User is already exist"
        }), status=422)
