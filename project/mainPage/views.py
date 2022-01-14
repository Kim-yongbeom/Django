from django.shortcuts import render

# Create your views here.
from mainPage.models import Good


def main(request):
    print('mainPage 호출됨')
    goods_list = Good.objects.all()
    context = {'mbti': ['ENFJ','ENFP','ENTJ','ENTP','ESFJ',
                 'ESFP','ESTJ','ESTP','INFJ','INFP',
                 'INTJ','INTP','ISFJ','ISFP','ISTJ','ISTP'],
               'goods' : goods_list
               }
    return render(request, 'mainPage/main.html',context)