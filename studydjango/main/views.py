from django.shortcuts import render

from .models import Room

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def map(request):
    roomlist = Room.objects.all() # 모든 Room 을 가져와서 roomlist에 저장.
    return render(request, 'main/map.html', {'roomlist':roomlist}) # map.html 페이지를 열 때 roomlist도 같이 가져옴.