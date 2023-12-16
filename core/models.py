from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import uuid


# POST MODEL
class Post(models.Model):
    hangul_title = models.CharField(max_length=100, default='신쳔지')
    title = models.CharField(max_length=100)
    content = models.TextField()
    start_date = models.IntegerField(default=1983)
    # auto_now adds the time of post
    # auto_now_add adds a date that cannot be changed.
    # default means i can change these dates when i need to
    date_posted = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date_posted} {self.title}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Quote(models.Model):
    hangul_title = models.CharField(max_length=100, default='신쳔지')
    title = models.CharField(max_length=100)
    content = models.TextField()
    start_date = models.IntegerField(default=1983)
    # auto_now adds the time of post
    # auto_now_add adds a date that cannot be changed.
    # default means i can change these dates when i need to
    date_posted = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date_posted} {self.title}"

    def get_absolute_url(self):
        return reverse('quote-detail', kwargs={'pk': self.pk})


# class DM(models.Model):
#     id = models.UUIDField(primary_key=True, max_length=15, editable=False, default=uuid.uuid4)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     c_post = models.ForeignKey(Post, on_delete=models.CASCADE,
#                                related_name='daily_missions')  # when getting the comments of a given user we
#     # shall use author.comments to get all the posts of a given user
#     body = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     edited = models.DateTimeField(auto_now=True)
#
#
#     def __str__(self):
#         return f"Comment by {self.author} on {self.c_post}"

# Create your models here.
class Test(models.Model):
    number = models.CharField(max_length=3)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    number = models.CharField(max_length=2)
    qtn = models.TextField()

    def __str__(self):
        return f'{self.number} {self.qtn}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    number = models.CharField(max_length=2)
    ans = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.question} {self.ans} no. {self.number}'


class Video(models.Model):
    video = models.FileField(upload_to='grad_vids')
    caption = models.CharField(max_length=50, default="vid")
    date_posted = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.caption
