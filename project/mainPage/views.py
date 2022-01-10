from django.shortcuts import render

# Create your views here.
def main(request):
    print('mainPage 호출됨')
    return render(request, 'mainPage/main.html')