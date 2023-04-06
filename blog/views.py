from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # 게시 예약 기능이 되겠구나... __lte=timezone.now()
    # 어이가 없네 개쉑히. created_date 가 아녔네. 아 놔...썅
    # posts = Post.objects.all
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

@login_required()
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            # 바로 공개되지 않게 하기.
            post.save()
            return redirect('post_detail', pk=post.pk)
        # post.pk 는 새로 save된 post의 pk
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

@login_required()
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # instance=post 는 폼에 수정 전 글이 채워진 상태로 보여준다.
        form = PostForm(request.POST, instance=post)
        #form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        # form = PostForm()

    return render(request, 'blog/post_edit.html', {'form':form})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish() #모델에서 추가한 함수
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete() # 장고 모델의 기본 메서드 delete()
    return redirect('post_list')