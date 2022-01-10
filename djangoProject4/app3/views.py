from django.shortcuts import render

# Create your views here.
def start3(request):
    print('받은 데이터 n1>>  ', request.GET['n1'])
    print('받은 데이터 n2>>  ', request.GET['n2'])
    print('받은 데이터 subject>>  ', request.GET['subject'])
    print('start3함수 호출됨.')
    n1 = int(request.GET['n1'])
    n2 = int(request.GET['n2'])
    subject = request.GET['subject']
    result = n1+n2
    # html에 넣고 싶은 데이터가 있으면 dic로 만들어줘라!!
    context = {'result':result, 'n1':n1, 'n2':n2, 'subject':subject}

    # 템플릿에서 만든것 불러오기
    return render(request, "app3/start3.html", context)