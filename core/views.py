from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from .models import Answer, Test, Question, Quote, Video
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
@login_required
def home(request):
    return render(request, 'core/index.html')


def questions(request, test_id):
    test = Test.objects.get(id=test_id)
    qtns = test.questions.all()

    return render(request, 'core/questions.html', {'qtns': qtns, 'test': test})


def next_qtn(request, test_id, qtn_id):
    test = get_object_or_404(Test, pk=test_id)
    qtns = test.questions.all()
    qtn = qtns.objects.get(pk=qtn_id)
    anss = qtn.answers.all()

    qtn.id += 1
    nxt_qtn = qtns.objects.get(pk=qtn.id)

    return render(request, 'core/answer.html', {'test': test, 'qtn': nxt_qtn, 'anss': anss})


def answers(request, test_id, pk):
    test = Test.objects.get(id=test_id)
    qtns = test.questions.all()
    qtn = qtns.get(id=pk)
    anss = qtn.answers.all()

    return render(request, 'core/answer.html', {'anss': anss, 'qtns': qtns, 'qtn': qtn,
                                                'test': test})

def study_tool(request):
    return render(request, 'core/study_tool.html')


def tests(request):
    tests = Test.objects.all()
    return render(request, 'core/tests.html', {'tests': tests})


# POSTS
class PostListView(ListView):
    model = Post
    template_name = 'core/posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 8


class QuoteListView(ListView):
    model = Quote
    template_name = 'core/quotes.html'
    context_object_name = 'quotes'
    ordering = ['-date_posted']


class UserPostListView(ListView):
    model = Post
    template_name = 'core/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'

    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

class QuoteDetailView(DetailView):
    model = Quote

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): #for getting the author of post
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuoteCreateView(LoginRequiredMixin, CreateView):
    model = Quote
    fields = ['title', 'content']

    def form_valid(self, form):  # for getting the author of post
        form.instance.author = self.request.user
        return super().form_valid(form)


class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    fields = ['video', 'caption']


    def form_valid(self, form):  # for getting the author of post
        form.instance.author = self.request.user
        return super().form_valid(form)

class Videos(ListView):
    model = Video
    template_name = 'core/video.html'
    context_object_name = 'videos'
    ordering = ['-date_posted']


#the UserPassesTestMixin cheks whether the owner of the post is the one
#altering the message. if we have it in plae we can create a text_func method
#this is what the mixin uses to do the checks.
# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     fields = ['title', 'content']
#
#     def form_valid(self, form): #for getting the author of post
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     #this should check whether the user is the author of the post.
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Post
#     success_url = 'posts/'
#
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


