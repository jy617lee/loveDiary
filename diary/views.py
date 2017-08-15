from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posting
from .form import PostForm


# Create your views here.
def index(request):
    postings = Posting.objects.all()
    return render(request, 'diary/default.html', {'postings':postings})

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST);
        if form.is_valid :
            post = form.save(commit = False)
            post.generate()
            return redirect('index')
    else :
        form = PostForm();
        return render(request, 'diary/form.html', {'form':form})
