from django.shortcuts import render

# Create your views here.
def start5(request):
    print('start5 호출됨.')
    context = {'today' : '금요일', 'when' : '2022년 1월 7일'}
    return render(request, 'app5/start5.html', context=context)

def js01(request):
    print('js01 호출됨')
    return render(request, 'app5/js01.html')

def js02(request):
    print('js02 호출됨')
    return render(request, 'app5/js02.html')

def js03(request):
    print('js03 호출됨')
    return render(request, 'app5/js03.html')

def js04(request):
    print('js04 호출됨')
    return render(request, 'app5/js04.html')

def js05(request):
    print('js05 호출됨')
    return render(request, 'app5/js05.html')

def js06(request):
    print('js06 호출됨')
    return render(request, 'app5/js06.html')