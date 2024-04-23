from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, Comment
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


# @login_required(login_url='accounts:login')
def posting(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comments.all()
    comment_form = CommentForm(request.POST)
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'community/post.html', context)


@login_required(login_url='accounts:login')
def postwrite(request):
    print('user')
    print(request.user)
    # save post
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            print(request.user)
            post.user = request.user
            post.save()
            return redirect('community:posting', pk=post.pk)
    # write post
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'community/postwrite.html', context)


@login_required(login_url='accounts:login')
def postupdate(request, pk):
    post = Post.objects.get(pk=pk)
    # 작성자가 아니면 수정 권한이 없음
    if post.user.id != request.user.id:
        return redirect('community:posting', pk)
    # 수정본 저장
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('community:posting', post.pk)
    # 수정 화면
    form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'community/postupdate.html', context)


@login_required(login_url='accounts:login')
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    # 작성자가 아니면 삭제 권한이 없음
    if post.user.id != request.user.id:
        return redirect('community:posting', pk)
    post.delete()
    return redirect('community:board')

def create_comment(request, pk):
    post = Post.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect('community:posting', post.pk)
    context = {
        'post': post,
        'comment_form': comment_form
    }
    return render(request, 'community/postcreate.html', context)
