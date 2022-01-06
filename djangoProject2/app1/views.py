from django.shortcuts import render

# Create your views here.
def start(request):
    print('start함수 호출됨.')
    data = {'name': 'hong', "age":100}
    # html에 넣고 싶은 데이터가 있으면 dic로 만들어줘라!!

    # 템플릿에서 만든것 불러오기
    return render(request, "app1/start.html",data)