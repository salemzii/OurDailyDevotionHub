from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, Comment, Like, BookMark
from django.views.generic import DetailView, CreateView
from .forms import CommentForm, PostForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import JsonResponse
import json


"""
class TopicView(DetailView):
    model = Post
    template_name = 'accounts/post.html'
    context_object_name = 'post'
"""


def TopicView(request, id):
    post = Post.objects.get(id=id)
    likes = [like for like in post.likes.all()]
    user_likes = []
    for user in likes:
        user_likes.append(user)
    check_user = request.user in user_likes
    return render(request, 'accounts/post.html', context={'true': check_user, 'post': post})

def addpost(request):
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.user_id = user.id
            form.save()
            return redirect('devotions')
    else:
        form= PostForm()
    return render(request, 'accounts/addpost.html', {'form': form})


def devotions(request):
    posts = Post.objects.all()
    devotion = [post for post in posts if post.category == 'devotion']
    return render(request, 'accounts/devotions.html', {'devotions': devotion})
    

def addcomment(request, id):
    user = User.objects.get(username= request.user.username)
    post = Post.objects.get(id= id)
    if request.method == "POST":          
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.user_id = user.id
            form.instance.post_id = post.id
            form.save()
            return redirect(reverse('topic', args=[post.id]))
    else:
        form = CommentForm()
    return render(request, 'accounts/addComment.html', {'form': form})


def add_bookmark(request):
    data = json.loads(request.body)
    print(data)
    postId = data['postId']
    action = data['action']
    print('Action:', action)
    print('Post:', postId)

    user = request.user
    post = Post.objects.get(id=postId)

    if action == 'bookmark':
        bookmark = BookMark.objects.create(user=user, post=post)
        bookmark.save()
    return JsonResponse('Post Bookmarked Successfully!', safe=False)


def like_post(request):
    data = json.loads(request.body)
    print(data)
    postId = data['postId']
    action = data['action']
    print('Action:', action)
    print('Post:', postId)

    user = request.user
    post = Post.objects.get(id=postId)

    if action == 'like':
        like = Like.objects.create(user=user, post=post, liked=True)
        like.save()
    elif action == 'unlike':
        like = Like.objects.get(user=user)
        like.delete()
        like.save()

    return JsonResponse('Post Liked Successfully!', safe=False)


def remove_bookmark(request):
    data = json.loads(request.body)
    print(data)
    postId = data['postId']
    action = data['action']
    print('Action:', action)
    print('Post:', postId)

    user = request.user
    bookmark = BookMark.objects.get(id=postId)

    if action == "delete":
        bookmark.objects.delete()
    return JsonResponse('Bookmark Removed Successfully!', safe=False)



def bookmarks(request):
    user = User.objects.get(id=request.user.id)
    bookmarks = user.bookmark_set.all()
    context = {'bookmarks': bookmarks}
    return render(request, 'accounts/bookmarks.html', context)

# Create your views here.
