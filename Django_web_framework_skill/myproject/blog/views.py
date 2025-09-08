from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Post
from .forms import CommentForm, PostForm


@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # create object but don’t save yet
            post.author = request.user      # assign logged-in user
            post.save()
            return redirect('post_list')    # redirect to blog home
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # fetch from DB
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog/my_posts.html', {'posts': posts})



def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


@login_required(login_url='login')
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:  # ❌ not the owner
        raise PermissionDenied

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/update_post.html', {'form': form})


@login_required(login_url='login')
def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.author != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/delete_post.html', {'post': post})

