import random
import pandas as pd
from time import sleep
from django.core import serializers
from django.http import JsonResponse, request
from django.shortcuts import render, redirect

# Create your views here.
from time import sleep
from mainPage.models import Product

from mainPage.models import Board

from signPage.models import User

from mainPage.module import onehot



import joblib
from sklearn.linear_model import LogisticRegression


# mldf = onehot.tomldata('ESFP', '남자', '10대', '무직', 3)
# print(mldf)

mbti_list = ['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ',
             'ESFP', 'ESTJ', 'ESTP', 'INFJ', 'INFP',
             'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP']

category_list = ['테이블','침대','침구류','조명','의자','거울','수납장','러그']

# userInfo = User.objects.get(id=request.session.user)
# user_MBTI = userInfo.mbti

def main(request):
    print('mainPage 호출됨')

    goods_list = Product.objects.all()
    header = random.sample(list(goods_list), 6)
    header1 = header[0]
    headers = header[1:]
    bx = random.sample(list(goods_list), 24)
    try:
        usermbti = User.objects.get(id=request.session['user'])

        mbti = usermbti.mbti
        sex = usermbti.sex
        age = usermbti.age
        job = usermbti.job
        like = usermbti.like
        heart = usermbti.heart

        # 좋아요 누른것 보이게 만들기!!
        liked_pd = heart[:-1]
        liked_pd = liked_pd.strip()
        liked_pd = liked_pd.split(',')
        print(liked_pd)

        if mbti == '모름':
            print('mbti 모름')
            context = {'mbti': mbti_list,
                       'goods': goods_list,
                       'bx': bx,
                       'usermbti': usermbti,
                       'liked_pd': liked_pd,
                       'header1': header1,
                       'headers': headers,
                       }
        else:
            mldf = onehot.tomldata(mbti, sex, age, job, int(like))
            print(mldf)

            mood = list(Product.objects.filter(**{mldf: 1}))
            moodpick = random.sample(mood, 10)
            # print(moodpick)

            if mldf == 'minimal':
                mood_name = '미니멀'
            elif mldf == 'modern':
                mood_name = '모던'
            elif mldf == 'natural':
                mood_name = '내추럴'
            elif mldf == 'individuality':
                mood_name = '개성'
            elif mldf == 'vintage':
                mood_name = '빈티지'
            elif mldf == 'romantic':
                mood_name = '로맨틱'
            elif mldf == 'useful':
                mood_name = '실용적'
            elif mldf == 'casual':
                mood_name = '캐주얼'
            print(mood_name)
            objpick = Product.objects.order_by('-' + mbti)[:10]
            context = {'mbti': mbti_list,
                       'goods': goods_list,
                       'mood_name': mood_name,
                       'mood': moodpick,
                       'obj': objpick,
                       'usermbti': usermbti,
                       'bx': bx,
                       'header1': header1,
                       'headers': headers,
                       }

    except:
        # 로그인 안했을때는 무드추천 mbti 추천 안해줌
        print('except로 넘어옴')
        context = {'mbti': mbti_list,
                   'goods': goods_list,
                   'bx': bx,
                   'header1': header1,
                   'headers': headers,
                   }


    return render(request, 'mainPage/main.html',context)

def heart(request,pid):
    heart = pid
    like = request.POST.get('like')
    userid = request.session.get('user')
    user = User.objects.get(id=userid)
    if(like == '1'):
        user.heart += heart + ','
        liked_pd = user.heart[:-1]
        liked_pd = liked_pd.strip()
        liked_pd = liked_pd.split(',')
        liked_pd = set(liked_pd)
        liked_pd = list(liked_pd)
        user.heart = ''
        for i in liked_pd:
            user.heart += i + ','

    else:
        liked_pd = user.heart[:-1]
        liked_pd = liked_pd.strip()
        liked_pd = liked_pd.split(',')
        for i in liked_pd:
            if heart == i:
                liked_pd.remove(heart)
        user.heart = ''
        for j in liked_pd:
            user.heart += j + ','


    user.save()

    context = {
        'data': user.heart,
        'heart' : heart
    }
    return JsonResponse(context)

def redheart(request):
    usermbti = User.objects.get(id=request.session['user'])
    # heart = usermbti.heart
    heart = usermbti.heart[:-1]
    heart = heart.split(',')

    context = {'heart' : heart}

    return JsonResponse(context)

def target(request):
    category = request.GET.get('category')
    if category == '모든상품':
        data = Product.objects.all()
    elif category == '테이블':
        data = Product.objects.filter(category=category)
    elif category == '침대':
        data = Product.objects.filter(category=category)
    elif category == '침구류':
        data = Product.objects.filter(category=category)
    elif category == '조명':
        data = Product.objects.filter(category=category)
    elif category == '의자':
        data = Product.objects.filter(category=category)
    elif category == '거울':
        data = Product.objects.filter(category=category)
    elif category == '수납장':
        data = Product.objects.filter(category=category)
    elif category == '러그':
        data = Product.objects.filter(category=category)

    context = {
        'data': serializers.serialize('json', list(data)),
    }
    return JsonResponse(context)


def target1(request):
    goods_list = Product.objects.all()

    context = {
        'goods': serializers.serialize('json', goods_list),
    }
    # print(serializers.serialize('json', goods_list))
    return JsonResponse(context)

def target2(request):
    mbti = request.GET.get('mbti')
    for i in mbti_list:
        if mbti == i:
            data = Product.objects.all().order_by('-' + i)
    context = {
        'data' : serializers.serialize('json', data),
    }
    return JsonResponse(context)

def target3(request):

    mbti = request.GET.get('mbti')
    category = request.GET.get('category')

    if category == 'table':
        category = '테이블'
    elif category =='bed':
        category = '침대'
    elif category == 'bedding':
        category = '침구류'
    elif category == 'light':
        category = '조명'
    elif category == 'chair':
        category = '의자'
    elif category == 'mirror':
        category = '거울'
    elif category == 'closet':
        category = '수납장'
    elif category == 'rug':
        category = '러그'

    for i in mbti_list:
        if mbti == i:
            data = Product.objects.filter(category=category).order_by('-'+ i)
    context = {
        'data' : serializers.serialize('json', data),
    }
    # print(serializers.serialize('json', goods_list))
    return JsonResponse(context)


def visual(request):
    print('visualPage 호출됨')
    try:
        usermbti = User.objects.get(id=request.session['user'])
        context = {'mbti': mbti_list,
                   'usermbti': usermbti,}
    except:
        context = {'mbti': mbti_list,}
    return render(request, 'mainPage/visual.html', context)

def community(request):
    print('게시판')

    board_list = Board.objects.order_by('-id')
    print("게시물 전체 조회 >> ", board_list)
    try:
        usermbti = User.objects.get(id=request.session['user'])
        context = {
            'board': board_list,
            'usermbti':usermbti,
            'mbti': mbti_list
        }
    except:
        context = {
            'board': board_list,
            'mbti': mbti_list
        }
    return render(request, 'mainPage/community.html', context)

def insert(request):
    return render(request, 'mainPage/insert.html')

def insert2(request):
    data = request.POST
    print(data)
    print("게시물의 title >> ", data.get('title'))
    print("게시물의 img >> ", data.get('img'))
    print("게시물의 content >> ", data.get('content'))

    # 받은 데이터 db에 저장
    title = data.get('title')
    img = data.get('img')
    content = data.get('content')

    userid = request.session.get('user')
    user = User.objects.get(id=userid)
    writer = user.nickname

    board = Board(title=title,
                  content=content,
                  writer=writer,
                  like=0,
                  img=img)

    # 객체 생성 -> save()
    board.save()
    return redirect('/community')

def delete(request, bid):
    board = Board.objects.get(id=bid)
    board.delete()
    return redirect('/community')

def edit(request, bid):
    board = Board.objects.get(id=bid)
    context = {
        'board': board
    }
    return render(request, 'mainPage/edit.html', context)

def edit2(request, bid):
    data = request.POST

    title = data.get('title')
    img = data.get('img')
    content = data.get('content')

    board = Board.objects.get(id=bid)

    board.title = title
    board.img = img
    board.content = content

    board.save()
    return redirect('/community')

def mood(request, mood):
    mood = mood
    if mood == 1:
        data = Product.objects.filter(minimal=1)
    elif mood ==2:
        data = Product.objects.filter(modern=1)
    elif mood == 3:
        data = Product.objects.filter(individuality=1)
    elif mood == 4:
        data = Product.objects.filter(natural=1)
    elif mood == 5:
        data = Product.objects.filter(vintage=1)
    elif mood == 6:
        data = Product.objects.filter(romantic=1)
    elif mood == 7:
        data = Product.objects.filter(useful=1)
    elif mood == 8:
        data = Product.objects.filter(casual=1)
    # print('---------------', data)
    mood = mood
    name = data.values('name')
    mood1 = data.values('mood1')
    mood2 = data.values('mood2')
    mood3 = data.values('mood3')
    category = data.values('category')
    mood_pic = data.values('mood_pic')
    detail_pic = data.values('detail_pic')
    likes = data.values('likes')
    try:
        usermbti = User.objects.get(id=request.session['user'])

        context = {
            'mbti': mbti_list,
            'mood' : mood,
            # 'no2' : no2,
            'data' : list(data),
            'name': name,
            'category' :  category,
            'mood_pic' : mood_pic,
            'detail_pic': detail_pic,
            'likes' : likes,
            'mood1': mood1,
            'mood2': mood2,
            'mood3': mood3,
            'usermbti': usermbti,
        }
    except:
        context = {
            'mbti': mbti_list,
            'mood': mood,
            # 'no2' : no2,
            'data': list(data),
            'name': name,
            'category': category,
            'mood_pic': mood_pic,
            'detail_pic': detail_pic,
            'likes': likes,
            'mood1': mood1,
            'mood2': mood2,
            'mood3': mood3,
        }

    return render(request, 'mainPage/mood.html',context)

def mood2(request):
    mood = request.GET.get('mood')
    data = None
    if mood == '1':
        data = Product.objects.filter(minimal=1)
    elif mood == '2':
        data = Product.objects.filter(modern=1)
    elif mood == '3':
        data = Product.objects.filter(individuality=1)
    elif mood == '4':
        data = Product.objects.filter(natural=1)
    elif mood == '5':
        data = Product.objects.filter(vintage=1)
    elif mood == '6':
        data = Product.objects.filter(romantic=1)
    elif mood == '7':
        data = Product.objects.filter(useful=1)
    elif mood == '8':
        data = Product.objects.filter(casual=1)

    context = {
        'data' : serializers.serialize('json', data),
    }

    return JsonResponse(context)

def mood3(request):
    mood = request.GET.get('mood')
    category = request.GET.get('category')

    if category == 'table':
        category = '테이블'
    elif category =='bed':
        category = '침대'
    elif category == 'bedding':
        category = '침구류'
    elif category == 'light':
        category = '조명'
    elif category == 'chair':
        category = '의자'
    elif category == 'mirror':
        category = '거울'
    elif category == 'closet':
        category = '수납장'
    elif category == 'rug':
        category = '러그'


    if mood == '1':
        data = Product.objects.filter(minimal=1, category = category)
    elif mood == '2':
        data = Product.objects.filter(modern=1, category = category)
    elif mood == '3':
        data = Product.objects.filter(individuality=1, category = category)
    elif mood == '4':
        data = Product.objects.filter(natural=1, category = category)
    elif mood == '5':
        data = Product.objects.filter(vintage=1, category = category)
    elif mood == '6':
        data = Product.objects.filter(romantic=1, category = category)
    elif mood == '7':
        data = Product.objects.filter(useful=1, category = category)
    elif mood == '8':
        data = Product.objects.filter(casual=1, category = category)


    context = {
        'data': serializers.serialize('json', data),
    }

    return JsonResponse(context)

def mbti(request, mbti):
    mbti = mbti

    for i in mbti_list:
        if mbti == i:
            data = Product.objects.all().order_by('-'+i)
    # print(list(data.values('id')))
    name = data.values('name')
    mood1 = data.values('mood1')
    mood2 = data.values('mood2')
    mood3 = data.values('mood3')
    category = data.values('category')
    mood_pic = data.values('mood_pic')
    detail_pic = data.values('detail_pic')
    likes = data.values('likes')
    try:
        usermbti = User.objects.get(id=request.session['user'])

        context = {
            'mbti': mbti_list,
            'mbti_one' : mbti,
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
            'usermbti': usermbti,
        }
    except:
        context = {
            'mbti': mbti_list,
            'mbti_one': mbti,
            'data': list(data),
            'name': name,
            'mood': mood,
            'category': category,
            'mood_pic': mood_pic,
            'detail_pic': detail_pic,
            'likes': likes,
            'mood1': mood1,
            'mood2': mood2,
            'mood3': mood3,
        }


    return render(request, 'mainPage/mbti.html',context)

def category(request, mbti, category):
    mbti = mbti
    category = category
    for i in mbti_list:
        if mbti == i:
            data = Product.objects.all().order_by('-'+i)

    name = data.values('name')
    mood1 = data.values('mood1')
    mood2 = data.values('mood2')
    mood3 = data.values('mood3')
    category = category
    mood_pic = data.values('mood_pic')
    detail_pic = data.values('detail_pic')
    likes = data.values('likes')
    try:
        usermbti = User.objects.get(id=request.session['user'])
        context = {
            'mbti': mbti_list,
            'mbti_one' : mbti,
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
            'usermbti': usermbti,
        }
    except:
        context = {
            'mbti': mbti_list,
            'mbti_one': mbti,
            'data': list(data),
            'name': name,
            'mood': mood,
            'category': category,
            'mood_pic': mood_pic,
            'detail_pic': detail_pic,
            'likes': likes,
            'mood1': mood1,
            'mood2': mood2,
            'mood3': mood3,
        }

    return render(request, 'mainPage/category.html',context)


def moodCategory(request, mood, category):
    mood = mood
    category = category

    data = None

    if category == 'table':
        category = '테이블'
    elif category =='bed':
        category = '침대'
    elif category == 'bedding':
        category = '침구류'
    elif category == 'light':
        category = '조명'
    elif category == 'chair':
        category = '의자'
    elif category == 'mirror':
        category = '거울'
    elif category == 'closet':
        category = '수납장'
    elif category == 'rug':
        category = '러그'


    if mood == 1:
        data = Product.objects.filter(minimal=1, category = category)
    elif mood == 2:
        data = Product.objects.filter(modern=1, category = category)
    elif mood == 3:
        data = Product.objects.filter(individuality=1, category = category)
    elif mood == 4:
        data = Product.objects.filter(natural=1, category = category)
    elif mood == 5:
        data = Product.objects.filter(vintage=1, category = category)
    elif mood == 6:
        data = Product.objects.filter(romantic=1, category = category)
    elif mood == 7:
        data = Product.objects.filter(useful=1, category = category)
    elif mood == 8:
        data = Product.objects.filter(casual=1, category = category)

    name = data.values('name')
    mood1 = data.values('mood1')
    mood2 = data.values('mood2')
    mood3 = data.values('mood3')
    category = category
    mood_pic = data.values('mood_pic')
    detail_pic = data.values('detail_pic')
    likes = data.values('likes')

    try:
        usermbti = User.objects.get(id=request.session['user'])
        context = {
            'mbti': mbti_list,
            'mbti_one': mbti,
            'data': list(data),
            'name': name,
            'mood': mood,
            'category': category,
            'mood_pic': mood_pic,
            'detail_pic': detail_pic,
            'likes': likes,
            'mood1': mood1,
            'mood2': mood2,
            'mood3': mood3,
            'usermbti':usermbti,
        }
    except:
        context = {
            'mbti': mbti_list,
            'mbti_one': mbti,
            'data': list(data),
            'name': name,
            'mood': mood,
            'category': category,
            'mood_pic': mood_pic,
            'detail_pic': detail_pic,
            'likes': likes,
            'mood1': mood1,
            'mood2': mood2,
            'mood3': mood3,
        }


    return render(request, 'mainPage/moodCategory.html',context)





