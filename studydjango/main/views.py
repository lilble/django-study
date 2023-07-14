from django.shortcuts import render

from .models import Room

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def map(request):
    roomlist = Room.objects.all() # 모든 Room 을 가져와서 roomlist에 저장.

    your_objects = Room.objects.all()  # 테이블의 모든 데이터를 가져옵니다.

    for obj in your_objects:
        print(obj.column1, obj.column2)  # 데이터의 컬럼
        
    return render(request, 'main/map.html', {'roomlist':roomlist}) # map.html 페이지를 열 때 roomlist도 같이 가져옴.

def room_info(request, pkkk):
    room = Room.objects.get(pk=pkkk)
    return render(request, 'main/roominfo.html', {'room':room})