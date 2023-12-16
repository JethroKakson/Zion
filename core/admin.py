from django.contrib import admin
from .models import Test, Question, Answer, Post, Quote, Video

# Register your models here.
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Post)
admin.site.register(Quote)
admin.site.register(Video)
