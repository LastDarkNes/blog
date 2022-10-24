from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.urls import reverse
from django.contrib.auth.models import User


# Create your views here.
def news_render(request, page=0):
    posts = Post.objects.all()[page:]
    number_of_pages = None
    if posts.count() > 10:
        number_of_pages = range(posts.count() % 10)
        posts = posts[page * 10 - 10:page * 10]

    is_authenticated = request.user.is_authenticated
    is_admin = request.user.is_staff

    context = {
        'is_authenticated': is_authenticated,
        'is_admin': is_admin,
        'posts': posts,
        'number_of_pages': number_of_pages,
    }

    # if request.POST:
    #     text = request.POST['text']
    #     user = request.user
    #
    #     return redirect(reverse('newsboard'))

    return render(request, "newsboard/posts.html", context)


def single_post(request, pk):
    is_authenticated = request.user.is_authenticated
    is_admin = request.user.is_staff
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(auto_id=False)

    context = {
        'post': post,
        'is_authenticated': is_authenticated,
        'is_admin': is_admin,
        'form': form,
    }

    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user
            text = form.cleaned_data['text']
            comment = Comment(author=user, text=text, post=post)
            comment.save()

    return render(request, 'newsboard/single_post_page.html', context)


def return_to_home_page(request):
    return redirect('newsboard')
