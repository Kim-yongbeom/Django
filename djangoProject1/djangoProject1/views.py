from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def start(request): # views 내에 정의된 함수는 반드시 파라메터를 하나 이상 넣어줘야 한다.
    # 클라이언트가 입력한 데이터를 받아주기 위한 변수!!
    print('start함수가 호출되었음!!!')
    return HttpResponse('<body bgcolor=red>' +
                        '<a href="http://www.naver.com"> to naver</a><br>' +
                        '<a href="http://www.google.com"> to google</a><br>' +
                        '<a href="http://www.daum.net"> to daum</a><br>' +
                        'i am a start page..@@@</body>')
    # 자동 import -> 해당 라이브러리에 커서를 가져간후 option 엔터 또는 alt 엔터

def start2(request):
    print('start2!!')
    return HttpResponse('start2입니당')

def start3(request):
    return HttpResponse('<body><a href="http://127.0.0.1:7777"> start</a><br>' +
                        '<a href="http://127.0.0.1:7777/start2"> start2</a><br></body>')