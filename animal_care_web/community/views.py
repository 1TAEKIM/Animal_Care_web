from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'community/index.html')


def board(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'community/board.html', context)


def posting(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'community/post.html', context)

@login_required  # 작동 안함
def postwrite(request):
    if not request.user.is_authenticated:
        return render(request, 'community/login.html')
    # save post
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print('save')
            post = form.save(user_id=request.user)  # user_id 붙이려면 commit=False 해야되는지도..
            return redirect('community:posting', pk=post.pk)
    # write post
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'community/postwrite.html', context)


def postupdate(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('community:posting', post.pk)
    form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'community/postupdate.html', context)


def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('community:board')
