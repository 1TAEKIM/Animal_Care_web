from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


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
    # children = comment.children.all()
    comment_form = CommentForm(request.POST)
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        # 'children': children,
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


# def post_like(request, pk):
#     post = Post.objects.get(pk=pk)
#     if request.user in post.like_users.all():
#         post.like_users.remove(request.user)
#     post.like_users.add(request.user, through_defaults={'memo':'메모'})
#     return redirect('community:posting', post.pk)


def post_like(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user, through_defaults={'memo':'메모'})
    return redirect('community:posting', post.pk)


def create_comment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            parent_comment_id = request.POST.get('parent_comment_id')  # 부모 댓글의 ID를 가져옴
            parent_comment = None
            if parent_comment_id:  # 부모 댓글이 있는 경우
                parent_comment = get_object_or_404(Comment, pk=parent_comment_id)
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.parent = parent_comment  # 대댓글의 부모 댓글 설정
            comment.save()
            return redirect('community:posting', post.pk)
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form
    }
    return render(request, 'community/post.html', context)



def update_comment(request, pk, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if comment.user.id != request.user.id:
        return redirect('community:posting', pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('community:posting', pk=pk)  # 수정 후 리디렉션할 페이지 지정
    # GET 요청일 때는 수정 폼을 보여줌
    comment_form = CommentForm(instance=comment)
    context = {
        'comment_form': comment_form,
        'comment': comment,
    }
    return render(request, 'community/update_comment.html', context)


@login_required(login_url='accounts:login')
def delete_comment(request, post_id, comment_id):
    print('함수 돌아감')
    comment = Comment.objects.get(pk=comment_id)
    print(comment_id)
    print(comment.user.id)
    print(request.user.id)

    print(comment.user.id != request.user.id)
    if comment.user.id != request.user.id:
        return redirect('community:posting', post_id)
    print('댓글 삭제')
    comment.delete()
    return redirect('community:posting', post_id)

