from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

class User(models.Model):

    username = models.CharField(_("username"), max_length=50)
    name = models.CharField(_("name"), max_length=50, null=True, blank=True, default=None)
    surname = models.CharField(_("surname"), max_length=50, null=True, blank=True, default=None)
    bio = models.CharField(_("bio"), max_length=255, null=True, blank=True, default=None)
    password = models.CharField(_("password hash"), max_length=64, editable=False)
    verified = models.BooleanField(_("verified"), default=False)
    email = models.EmailField(_("email"), max_length=254, null=True, blank=True, default=None)
    phone = models.CharField(_("phone number"), max_length=15, null=True, blank=True, default=None)
    token = models.CharField(_("token"), max_length=50, editable=False)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})
