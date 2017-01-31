from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Place
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm, PlaceForm

def category_list(request):
    return render(request, 'blog/category_list.html')

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def place_list(request):
    places = Place.objects.all()
    template = 'blog/place_list.html'
    context = {'places': places}
    return render(request, template, context)

def post_detail(request, pk):
	post= get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def place_new(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.save()
            return redirect('place_detail', pk=place.pk)
    else:
        form = PlaceForm()
    return render(request, 'blog/place_edit.html', {'form': form}) 

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def place_edit(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            place.save()
            return redirect('place_detail', pk=place.pk)
    else:
        form = PlaceForm(instance=place)
    return render(request, 'blog/place_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk).delete()
    return render(request, 'blog/post_delete.html', {'post': post})

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment= form.save(commit=False)
            comment.post = post 
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
        template = 'blog/add_comment.html'
        context = {'form': form}
        return render(request, template, context)
