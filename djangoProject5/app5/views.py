from django.http import JsonResponse
from django.shortcuts import render, redirect

from app5.models import Test


def test(request):
    test_list = Test.objects.order_by('-name')[:10]
    print('검색한 결과 >> ' ,  test_list)
    print('검색한 결과 >> ', test_list[0])
    context = {'test_list':test_list}
    return render(request, 'app5/test.html', context)

def create(request):
    return render(request,'app5/create.html')

def create2(request):
    data = request.POST
    newId = Test(name=data.get('name'),tel=data.get('tel'),addr=data.get('addr'))
    newId.save()
    return redirect('/app5/test')

def person(request, id):
    print('받은 id는>> ', id)
    one = Test.objects.get(id=id)
    context = {'one': one}
    return render(request,'app5/person.html',context)

def delete(request, id):
    print('삭제할 id는>> ', id)
    one = Test.objects.get(id=id)
    one.delete()
    print(id, '삭제됨')
    return redirect('/app5/test')
    # redirect는 서버가 클라이언트에게 해당주소를 요청하도록 명령함.
    # 그냥 호출하면 DB데이터가 없어 호출하면 안됨

def update(request, id): # 수정할 수 있는 화면을 호출하는 함수
    # update는 주소가 2개가 필요하다!!
    # 1) 기존 내용을 수정할 수 있는 화면을 만드는 주소
    # 2) 수정하는 화면에서 수정된 내용인 db에 반영처리되도록 하는 주소가 필요
    print('수정할 id는>> ', id)
    one = Test.objects.get(id=id) #db 검색후, template파일에 넘기기
    context = { 'one':one}
    return render(request,'app5/update.html', context)

def update2(request): # 수정될 데이터 받아서 데이터베이스에 update
    data = request.POST
    print('수정할 데이터들>> ',data)
    # 검색을 먼저 한 다음에, 특정한 컬럼값 변경해주고, 전체 목록페이지를 호출
    one = Test.objects.get(id=data.get('id'))
    one.name = data.get('name')
    one.tel = data.get('tel')
    one.addr = data.get('addr')
    one.save()
    return redirect('/app5/test')

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

def ajax0(request):
    print('ajax0 호출됨')
    return  render(request,'app5/ajax0.html')

def ajax3(request):
    print('ajax3 호출됨')
    return  render(request, 'app5/ajax3.html')

def ajax1(request):
    print('ajax1 호출됨')
    return  render(request,'app5/ajax1.html')

def target0(request):
    print('ajax0 호출됨')
    context = {'result':100, 'sum':1000}
    return  render(request,'app5/target0.html',context)

def target00(request):
    print('ajax00 호출됨')
    context = {'today': -10, 'today2': 'bad'}
    return  render(request,'app5/target00.html',context)

def target(request):
    print('=================== target호출됨.')
    context = {'result' : 100, 'age' : 100, 'tel' : [100, 200, 300]}
    # return render(request, "app5/target.html", context)
    # return HttpResponse(context)
    return JsonResponse(context)

def ajax2(request):
    print('=================== ajax2호출됨.')
    return render(request, "app5/ajax2.html")

def target2(request): # 종로3가 위도, 경도
    print('=================== target2호출됨.')
    context = {"lat" : 37.570580, "lng" : 126.99212654}
    return JsonResponse(context)

def target3(request): # 동대문 위도, 경도
    print('=================== target3호출됨.')
    context = {"lat" : 37.5642135, "lng" : 127.0016985}
    return JsonResponse(context)

def target4(request): # 동대문 위도, 경도
    print('=================== target4호출됨.')
    context = {'comment' : ['좋네요','음...','별로'], 'score' : [5,3,2]}
    return JsonResponse(context)
