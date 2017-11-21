from django.shortcuts import render
from core.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-id')
    context = {'posts':posts }
    return render(request, 'index.html', context)

def article_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post':post }
    return render(request, 'article_detail.html', context)
