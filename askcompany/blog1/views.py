from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    print(qs)
    return render(request,'blog1/post_list.html',{
        'post_list':qs,
    })