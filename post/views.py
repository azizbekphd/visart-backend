import json
from django.forms import model_to_dict

from django.http import HttpResponse

from users.models import User
from .models import VideoPost, ImagePost, Post

def new_video(request):
    user = User.objects.get(token=request.META.get("HTTP_AUTHORIZATION").split(" ")[1])
    body = json.loads(request.body.decode('utf-8'))
    post = VideoPost(youtube_link=body["youtube_link"], title=body["title"], description=body["description"], author=user)
    post.save()
    return HttpResponse(json.dumps(model_to_dict(post)), status=200)
    

def new_image(request):
    pass
