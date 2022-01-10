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

def js07(request):
    print('js07 호출됨')
    return render(request, 'app5/js07.html')

def js08(request):
    print('js08 호출됨')
    return render(request, 'app5/js08.html')

def js09(request):
    print('js09 호출됨')
    return render(request, 'app5/js09.html')

def js10(request):
    print('js10 호출됨')
    return render(request, 'app5/js10.html')

def js11(request):
    print('js11 호출됨')
    # db연동 결과를 검색해서 가지고 온다.
    # 결과를 html로 보내주어야 한다.
    # db에서 가져온 값을 context로 만들어야한다.
    context = {'userName' : 'hong',
               'field' :'shoes',
               'email' : 'aliciawill@kakap.com',
               'contact' : '010-4904-2995',
               'payValue' : 5000}
    return render(request, 'app5/js11.html', context)

def js12(request):
    print('js12 호출됨')
    context = {'site' : [100,200,300],
               'url' : {'u1':'naver','u2':'daum','u3':'google'},
               'name' : ['hong', 'kim', 'apple'],
               }
    return render(request, 'app5/js12.html', context)

def map1(request):
    print('=================== map1호출됨.')
    context = {'lats' : [ 37.5705805429368, 37.560260, 37.689447 ],
               'lngs' : [ 126.99212654046664, 126.942149, 127.046558 ]}
    return render(request, "app5/map1.html", context)

def chart1(request):
    print('chart1 호출됨')
    return render(request, 'app5/chart1.html')