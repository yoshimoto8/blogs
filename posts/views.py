from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("Hello World! このぺーずは投稿のインデックスです")

    return render(request, 'posts/index.html')
