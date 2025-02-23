from django.shortcuts import get_object_or_404, render

from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from .forms import BlogPostForm, CategoryForm
from django.shortcuts import redirect

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
    'category_count':category_count,
    'blogs_count': blogs_count,
}
    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    return render(request, 'dashboard/categories.html')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()

    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)

def edit_category(request, pk):
    category =get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories') #Redirect to the categories page after a successful update
    else:
        form = CategoryForm(instance = category)
    context= {
        'form': form,
        'category': category,
    
    }
    return render(request, 'dashboard/edit_category.html', context)
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

def posts(request):
    posts = Blog.objects.all()
    context={
        'posts': posts
    }
    return render(request, 'dashboard/posts.html', context)
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  #temporary saving the form
            post.author = request.user
            post.save()
            return redirect('posts')
        else:
            print('form is invalid')
            print(form.errors)
    form=BlogPostForm()
    context={
        'form': form 
    }
    return render(request, 'dashboard/add_post.html', context)