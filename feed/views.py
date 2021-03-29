from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import NewCommentForm, NewPostForm


class HomeView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'feed/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10


@login_required
def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()

            return HttpResponseRedirect(reverse('index'))

    return render(request, 'feed/new_post.html', {
        'form': NewPostForm()
    })


@login_required
def post_details(request, _id):
    post = get_object_or_404(Post, pk=_id)

    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.post = post
            data.user = request.user
            data.save()
        else:
            return render(request, 'feed/post_details.html', {
                'post': post,
                'form': form
            })

    return render(request, 'feed/post_details.html', {
        'post': post,
        'form': NewCommentForm()
    })
