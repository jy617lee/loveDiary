from django.shortcuts import render
from django.http import HttpResponse
from .models import Posting

# Create your views here.
def index(request):
    postings = Posting.objects.all()
    return render(request, 'diary/default.html', {'postings':postings})
