from django.shortcuts import render

# Create your views here.
#博客
def article(request):

    return render(request,'article.html')

def read(request):

    return render(request,'read.html')