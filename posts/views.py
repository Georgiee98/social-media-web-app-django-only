from django.shortcuts import render, redirect
from .forms import PostCreateForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from django.shortcuts import get_object_or_404


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
    else:
        form = PostCreateForm(data=request.GET)
    return render(request, 'posts/create.html', {'form': form})


def feed(request):
    if request.method == "POST":
       comment_form = CommentForm(data=request.POST)
       new_comment = comment_form.save(commit=False)
       post_id = request.POST.get('post_id')
       post = get_object_or_404(Post, id=post_id)
       new_comment.post = post
       new_comment.save()
    else:
       comment_form = CommentForm()
    posts = Post.objects.all()
    logged_user = request.user
    return render(
       request, 'posts/feed.html',
       {'posts': posts, 'logged_user': logged_user,
        'comment_form': comment_form})

from django.http import JsonResponse

def like(request):
  post_id = request.POST.get('post_id')
  post = get_object_or_404(Post, id=post_id)
  liked = False
  if post.liked_by.filter(id=request.user.id).exists():
    post.liked_by.remove(request.user)
  else:
    post.liked_by.add(request.user)
    liked = True
  post.save()
  response_data = {
    'liked': liked,
    'like_count': post.liked_by.count(),
    'already_liked': post.liked_by.filter(id=request.user.id).exists(),
  }
  return JsonResponse(response_data)
