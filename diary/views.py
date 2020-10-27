from django.shortcuts import render
from diary import models
# Create your views here.
def diary(request):
    my_diarys=models.diary.objects.all().order_by("-data")
    content = {'my_diarys':my_diarys,'tite':'我的日记'}
    return render(request,'diary.html',content)