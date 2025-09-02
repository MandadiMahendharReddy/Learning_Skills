from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm, PostForm


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
