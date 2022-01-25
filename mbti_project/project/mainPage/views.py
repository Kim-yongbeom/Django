import random

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from time import sleep
from mainPage.models import Product

from mainPage.models import Board, Comment

mbti_list = ['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ',
                 'ESFP', 'ESTJ', 'ESTP', 'INFJ', 'INFP',
                 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP']

def main(request):
    print('mainPage 호출됨')
    goods_list = Product.objects.all()
    mood = list(Product.objects.filter(individuality=1))
    moodpick = random.sample(mood, 10)
    objpick = Product.objects.order_by('-ENFJ')[:10]

    context = {'mbti': mbti_list,
               'goods' : goods_list,
               'mood': moodpick,
               'obj': objpick,
               }
    return render(request, 'mainPage/main.html',context)

def target(request):
    goods_list = Product.objects.all()

    context = {
               'goods': serializers.serialize('json', goods_list),
               }
    # print(serializers.serialize('json', goods_list))
    return JsonResponse(context)


def visual(request):
    print('visualPage 호출됨')
    context = {'mbti': mbti_list}
    return render(request, 'mainPage/visual.html', context)

def community(request):
    print('게시판')

    board_list = Board.objects.order_by('-id')
    print("게시물 전체 조회 >> ", board_list)

    context = {
        'board': board_list,
    }
    return render(request, 'mainPage/community.html', context)

def comment(request):
    print('view all comments')

    comments = Comment.objects.order_by('-id')
    print("댓글 전체 조회 >> ", comments)

    context = {
        'comments': comments,
    }

    return render(request, 'mainPage/comment.html', context)

def mood(request, no):
    no = no
    if no == 1:
        data = Product.objects.filter(minimal=1)
    elif no ==2:
        data = Product.objects.filter(modern=1)
    elif no == 3:
        data = Product.objects.filter(individuality=1)
    elif no == 4:
        data = Product.objects.filter(natural=1)
    elif no == 5:
        data = Product.objects.filter(vintage=1)
    elif no == 6:
        data = Product.objects.filter(romantic=1)
    elif no == 7:
        data = Product.objects.filter(useful=1)
    elif no == 8:
        data = Product.objects.filter(casual=1)
    # print('---------------', data)
    no = no
    name = data.values('name')
    mood = list(data.values('mood'))
    mood1 = data.values('mood1')
    mood2 = data.values('mood2')
    mood3 = data.values('mood3')
    category = data.values('category')
    mood_pic = data.values('mood_pic')
    detail_pic = data.values('detail_pic')
    likes = data.values('likes')
    context = {
        'mbti': mbti_list,
            'no' : no,
            # 'no2' : no2,
            'data' : list(data),
            'name': name,
            'mood' : mood,
            'category' :  category,
            'mood_pic' : mood_pic,
            'detail_pic': detail_pic,
            'likes' : likes,
            'mood1': mood1,
            'mood2': mood2,
            'mood3': mood3,
        }

    return render(request, 'mainPage/mood.html',context)

def mood2(request):
    no = request.GET.get('no')
    # print(no, '----------------------')
    data = None
    if no == '1':
        data = Product.objects.filter(minimal=1)
    elif no == '2':
        data = Product.objects.filter(modern=1)
    elif no == '3':
        data = Product.objects.filter(individuality=1)
    elif no == '4':
        data = Product.objects.filter(natural=1)
    elif no == '5':
        data = Product.objects.filter(vintage=1)
    elif no == '6':
        data = Product.objects.filter(romantic=1)
    elif no == '7':
        data = Product.objects.filter(useful=1)
    elif no == '8':
        data = Product.objects.filter(casual=1)
    # print('---------------', data)
    # no = no
    # print(data , '=========================')
    name = data.values('name')
    mood = list(data.values('mood'))
    mood1 = data.values('mood1')
    mood2 = data.values('mood2')
    mood3 = data.values('mood3')
    category = data.values('category')
    mood_pic = data.values('mood_pic')
    detail_pic = data.values('detail_pic')
    likes = data.values('likes')
    context = {
        'mbti': mbti_list,
            'no' : no,
            'data' : list(data),
            'name': name,
            'mood' : mood,
            'category' :  category,
            'mood_pic' : mood_pic,
            'detail_pic': detail_pic,
            'likes' : likes,
            'mood1': mood1,
            'mood2': mood2,
            'mood3': mood3,
        }

    return render(request, 'mainPage/mood2.html',context)

def mood3(request):
    no = request.GET.get('no')
    no2 = request.GET.get('no2')
    print('-----------------',no2)
    # no2 = URLDecoder.decode(decodeURIComponent(no2));
    print(no, '----------------------')
    data = None
    if no == '1':
        data = Product.objects.filter(minimal=1, category = no2)
        print(data)
    elif no == '2':
        data = Product.objects.filter(modern=1, category = no2)
    elif no == '3':
        data = Product.objects.filter(individuality=1, category = no2)
    elif no == '4':
        data = Product.objects.filter(natural=1, category = no2)
    elif no == '5':
        data = Product.objects.filter(vintage=1, category = no2)
    elif no == '6':
        data = Product.objects.filter(romantic=1, category = no2)
    elif no == '7':
        data = Product.objects.filter(useful=1, category = no2)
    elif no == '8':
        data = Product.objects.filter(casual=1, category = no2)
    # print('---------------', data)
    # no = no
    # print(data , '=========================')
    name = data.values('name')
    mood = list(data.values('mood'))
    mood1 = data.values('mood1')
    mood2 = data.values('mood2')
    mood3 = data.values('mood3')
    category = data.values('category')
    mood_pic = data.values('mood_pic')
    detail_pic = data.values('detail_pic')
    likes = data.values('likes')
    context = {
        'mbti': mbti_list,
            'no' : no,
            'no2' : no2,
            'data' : list(data),
            'name': name,
            'mood' : mood,
            'category' :  category,
            'mood_pic' : mood_pic,
            'detail_pic': detail_pic,
            'likes' : likes,
            'mood1': mood1,
            'mood2': mood2,
            'mood3': mood3,
        }

    return render(request, 'mainPage/mood3.html',context)

def mbti(request, mbti):
    mbti = mbti

    for i in mbti_list:
        if mbti == i:
            data = Product.objects.all().order_by('-'+i)

    name = data.values('name')
    mood1 = data.values('mood1')
    mood2 = data.values('mood2')
    mood3 = data.values('mood3')
    category = data.values('category')
    mood_pic = data.values('mood_pic')
    detail_pic = data.values('detail_pic')
    likes = data.values('likes')
    context = {
            'mbti': mbti_list,
            'data': list(data),
            'name': name,
            'mood' : mood,
            'category' :  category,
            'mood_pic' : mood_pic,
            'detail_pic': detail_pic,
            'likes' : likes,
            'mood1': mood1,
            'mood2': mood2,
            'mood3': mood3,
        }

    return render(request, 'mainPage/mbti.html',context)



def mbti2(request):
    mbti = request.GET.get('mbti')
    for i in mbti_list:
        if mbti == i:
            data = Product.objects.all().order_by('-'+i)
    # # print('---------------', data)
    # no = no
    name = data.values('name')
    mood = list(data.values('mood'))
    mood1 = data.values('mood1')
    mood2 = data.values('mood2')
    mood3 = data.values('mood3')
    category = data.values('category')
    mood_pic = data.values('mood_pic')
    detail_pic = data.values('detail_pic')
    likes = data.values('likes')
    context = {
            'mbti': mbti_list,
            'mbti' : mbti,
            'data' : list(data),
            'name': name,
            'mood' : mood,
            'category' :  category,
            'mood_pic' : mood_pic,
            'detail_pic': detail_pic,
            'likes' : likes,
            'mood1': mood1,
            'mood2': mood2,
            'mood3': mood3,
        }
    return render(request, 'mainPage/mbti2.html',context)



def mbti3(request):
    mbti = request.GET.get('mbti')
    no2 = request.GET.get('no2')
    for i in mbti_list:
        if mbti == i:
            data = Product.objects.filter(category=no2).order_by('-'+i)
    no2 = no2
    name = data.values('name')
    mood = list(data.values('mood'))
    mood1 = data.values('mood1')
    mood2 = data.values('mood2')
    mood3 = data.values('mood3')
    category = data.values('category')
    mood_pic = data.values('mood_pic')
    detail_pic = data.values('detail_pic')
    likes = data.values('likes')
    context = {
        'mbti': mbti_list,
             'no2' : no2,
            'data' : list(data),
            'name': name,
            'mood' : mood,
            'category' :  category,
            'mood_pic' : mood_pic,
            'detail_pic': detail_pic,
            'likes' : likes,
            'mood1': mood1,
            'mood2': mood2,
            'mood3': mood3,
        }

    return render(request, 'mainPage/mbti3.html',context)







