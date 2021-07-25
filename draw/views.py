# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })

def mobile_3(request):
    return render(request, 'draw/mobile_3.html')

def mobile_5(request):
    return render(request, 'draw/mobile_5.html')

def mobile_7(request):
    return render(request, 'draw/mobile_7.html')

def mobile_text(request):
    return render(request, 'draw/mobile_text.html')

def web(request):
    return render(request, 'draw/web.html')

def test(request):
    return render(request, 'draw/test.html')
