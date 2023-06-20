from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}, {self.user.email}, {self.id} picture is {self.photo}"


class Contact(models.Model):
    follower = models.ForeignKey(
        User, related_name="follows", on_delete=models.CASCADE, default=None
    )
    following = models.ForeignKey(
        User, related_name="following", on_delete=models.CASCADE, default=None
    )
    up_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["-up_time"]),
        ]
        ordering = ["-up_time"]
        # uniqur_together =

    def __str__(self):
        return f"{self.follower} follows {self.following}"


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="users_posts")
    content = models.CharField(max_length=300)
    time_up = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, blank=True, related_name="liked_by")

    def __str__(self):
        return f"{self.content}"

    class Meta:
        ordering = ["-time_up"]
