from django.db import models

class Post(models.Model):
    id = models.AutoField("id", primary_key=True)
    author = models.ForeignKey("users.User", verbose_name="author", on_delete=models.CASCADE)
    pub_date = models.DateTimeField("Publication date", auto_now=False, auto_now_add=True)
    edit_date = models.DateTimeField("Last edit date", auto_now=True, auto_now_add=False)
    title = models.CharField("Post title", max_length=255, default="")
    description = models.TextField("Post description", blank=True, default="")

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return f"Post #{self.id} — {self.author.username}"
    

class VideoPost(Post):
    youtube_link = models.URLField("video YouTube link", max_length=200)

class ImagePost(Post):
    source = models.URLField("image url", max_length=200)
