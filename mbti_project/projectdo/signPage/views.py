from django.shortcuts import render, redirect

from signPage.models import User
from django.contrib import messages

mbti_list = ['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ',
             'ESFP', 'ESTJ', 'ESTP', 'INFJ', 'INFP',
             'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP']

# Create your views here.
def signUp(request):
    print('signup호출')
    context = {
        'mbti' : mbti_list
    }
    return render(request, 'signPage/signUp.html', context)

def signUp2(request):
    data = request.POST
    print('회원가입데이터>> ', data)
    userId = data.get('userId')
    userPw = data.get('userPw')
    nickname = data.get('nickname')
    mbti = data.get('mbti')
    sex = data.get('sex')
    age = data.get('age')
    job = data.get('job')
    like = data.get('like')
    if not(userId and userPw and nickname and mbti and sex and age and job and like):
        messages.error(request, "모든 값을 입력해주세요!!")
        return render(request, 'signPage/signUp.html')
    else:
        one = User(userId=userId, userPw=userPw, nickname=nickname, mbti=mbti, sex=sex, age=age, job=job, like=like)
        one.save()
        messages.success(request, "회원가입성공!!")
        return redirect('/')

def signIn(request):
    print('signin호출')
    context = {
        'mbti': mbti_list
    }
    return render(request, 'signPage/signIn.html', context)

def signIn2(request):
    print('signin2호출')
    data = request.POST
    login_userId = data.get('userId')
    login_userPw = data.get('userPw')
    if not (login_userId and login_userPw):
        messages.error(request, "아이디 또는 비밀번호를 입력해주세요!!")
        return render(request, 'signPage/signIn.html')
    else:
        try:
            myUser = User.objects.get(userId=login_userId)
            if login_userPw == myUser.userPw and login_userId == myUser.userId:
                request.session['user'] = myUser.id
                request.session['nickname'] = myUser.nickname
                print('userSession---> ', request.session['user'])
                messages.success(request, "로그인성공!!")
                return redirect('/')
            else:
                messages.error(request, "비밀번호가 틀렸습니다!!")
                return render(request, 'signPage/signIn.html')
        except:
            messages.error(request, "아이디 또는 비밀번호가 틀렸습니다!!")
            return render(request, 'signPage/signIn.html')

def logOut(request):
    request.session.clear()
    messages.info(request, '로그아웃 되었습니다!')
    return redirect('/')

def userUpdate(request, id):
    print('userUpdate출력')
    one = User.objects.get(id = id)
    try:
        usermbti = User.objects.get(id=request.session['user'])
        context = {
            'one' : one,
            'mbti': mbti_list,
            'usermbti' : usermbti
        }
    except:
        context = {
            'one': one,
            'mbti': mbti_list,
        }
    return render(request, 'signPage/userUpdate.html', context)

def userUpdate2(request):
    print('userUpdate2출력')
    data = request.POST
    update = User.objects.get(id = request.session['user'])
    update.userId = data.get('userId')
    update.userPw = data.get('userPw')
    update.nickname = data.get('nickname')
    update.mbti = data.get('mbti')
    update.sex = data.get('sex')
    update.age = data.get('age')
    update.job = data.get('job')
    update.like = data.get('like')

    if not(update.userId and update.userPw and update.nickname and update.mbti and update.sex and update.age and update.job and update.like):
        messages.error(request, "모든 값을 입력해주세요!!")
        return render(request, 'signPage/userUpdate.html')
    else:
        update.save()
        messages.success(request, "수정완료 되었습니다!!")
        return redirect('/')