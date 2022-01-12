from django.shortcuts import render

# Create your views here.
def main(request):
    print('mainPage 호출됨')
    mbti_list = {'mbti': ['ENFJ','ENFP','ENTJ','ENTP','ESFJ',
                 'ESFP','ESTJ','ESTP','INFJ','INFP',
                 'INTJ','INTP','ISFJ','ISFP','ISTJ','ISTP']}
    return render(request, 'mainPage/main.html',mbti_list)