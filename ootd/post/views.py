# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CreatePostForm
from django.utils import timezone
from django.contrib.auth.models import User


def index(request):
    boards = Post.objects.all()

    # current =0;
    # if request.user == Board.user_id:
    #     current=1;

    return render(request, "post/board_index.html", {'boards' : boards})

def show_board(request, id):
    boards = Post.objects.get(id = id)
    return render(request, 'post/board_show.html', {'boards' : boards})

def create_board(request):
    form = PostForm(request.POST, request.FILES)

    if form.is_valid():
        post = form.save(commit=False)
        post.user_id = request.user
        post.date = timezone.now()
        post.save()
        return redirect(index)

    return render(request, 'post/board_form.html', {'form' : form})

def update_board(request, id):
    boards = Post.objects.get(id = id)
    form = PostForm(request.POST or None, instance = boards)


    if form.is_valid():
        form.save()
        return redirect(index)

    return render(request, 'post/board_form_update.html', {'form' : form, 'boards' : boards})

def delete_board(request, id):
    boards = Post.objects.get(id = id)

    if request.method == 'POST':
        boards.delete()
        return redirect(index)

    return render(request, 'post/board_delete_confirm.html', {'boards' : boards})


def create_comment(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.user_id = request.user
        post.date = timezone.now()
        post.save()
        return redirect(index)

    return render(request, 'post/board_form.html', {'form' : form})

def delete_comment(request, id):
    boards = Comment.objects.get(id = id)

    if request.method == 'POST':
        boards.delete()
        return redirect(index)

    return render(request, 'post/board_delete_confirm.html', {'boards' : boards})
