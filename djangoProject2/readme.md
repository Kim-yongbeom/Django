# GET, POST

python ./manage.py startapp app1을 터미널로 만들었다면
settings.py에서 INSTALLED_APPS 안에 
app1.apps.App1Config넣어줘야함


### app1에 models.py에서 
- db에 생성할 테이블을 클래스로 정의해 놓으면(상속),
- db에 테이블을 생성할 수 있는 파이썬 파일을 자동 생성해줌.
-      makemigrations(py)
- 위에서 생성한 py파일을 실행해주면, db에 테이블이 자동생성됨
-      migrate
```
class Test100(models.Model):
    #테이블안에 생성할 컬럼들을 지정
    # id는 설정 안해주면 자동생성됨 무조건
    pw = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
```

```
class Test200(models.Model):
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=300)
    tel = models.CharField(max_length=300)
```

### 적어준 후 터미널에 밑에 작성
- python ./manage.py makemigrations
- python ./manage.py migrate
- 해주면 DB 생성


### 관리자모드에서 DB관리 해주고 싶다면 admin 파일로 들어가서 site.register해줘야함
<img width="432" alt="스크린샷 2022-01-06 오전 11 01 58" src="https://user-images.githubusercontent.com/89058117/148356975-2501c27c-4a32-42ae-bdd5-b39a33a0034f.png">


### 관리자 모드에서 보기 편하게 만들기
```
def __str__(self):
    return self.name + ' : ' + self.content + ' : ' + str(self.price)
```
<img width="682" alt="스크린샷 2022-01-06 오전 11 09 47" src="https://user-images.githubusercontent.com/89058117/148357063-fe14d861-df95-4d12-8fc6-156d4ac3e346.png">
<img width="668" alt="스크린샷 2022-01-06 오전 11 09 57" src="https://user-images.githubusercontent.com/89058117/148357075-72de2d35-3746-45c1-9217-4aaf49f000f7.png">



### templates에 app1~app4 만들고 html 작성
<img width="432" alt="스크린샷 2022-01-06 오후 12 44 59" src="https://user-images.githubusercontent.com/89058117/148357099-f7b8a355-4145-4ed1-a1da-3392cb9108b9.png">


### static 폴더를만들자 (여기에는 css, js, 이미지들 다 넣어줄거)
<img width="207" alt="스크린샷 2022-01-06 오후 12 48 34" src="https://user-images.githubusercontent.com/89058117/148357107-990855bc-bab8-462e-ad9a-2dfa3ad22c5a.png">


### 각각의 views에 작성해주고 urls에서 리스트에 담아주기
<img width="334" alt="스크린샷 2022-01-06 오후 12 52 56" src="https://user-images.githubusercontent.com/89058117/148357117-431318f1-cfce-4785-9b68-a8ff869a7d0f.png">


### 템플릿에서 만들것 불러오기 app1/views.py에서
### render 함수 쓰기 
<img width="592" alt="스크린샷 2022-01-06 오후 4 12 58" src="https://user-images.githubusercontent.com/89058117/148357134-77445493-af9c-4680-b687-cf349e3930cb.png">




### 결국 직접작성한것과 별 차이없음!!
<img width="585" alt="스크린샷 2022-01-06 오후 4 15 56" src="https://user-images.githubusercontent.com/89058117/148357158-6a5eae27-187c-4e84-9f0f-59e0223d6b5f.png">



### html에 데이터 넣어주기
### 데이터 넣어주고 html파일에 데이터 넣어주기
<img width="436" alt="스크린샷 2022-01-06 오후 4 23 58" src="https://user-images.githubusercontent.com/89058117/148357187-4c58851a-465c-4c69-a380-4645c36fd01b.png">
<img width="589" alt="스크린샷 2022-01-06 오후 4 24 57" src="https://user-images.githubusercontent.com/89058117/148357192-c5ca94cd-b812-4b7b-97fd-724710c493b4.png">



### 숫자 넣기
<img width="461" alt="스크린샷 2022-01-06 오후 4 44 49" src="https://user-images.githubusercontent.com/89058117/148357207-b1cbea05-802f-47b7-b663-19810a2728fb.png">


----------------------------------
### start2.html에서 주소에서 받아준 값들 GET으로 받아오기
### urls.py에 path('start3', app3.views.start3)추가
<img width="727" alt="스크린샷 2022-01-06 오후 5 31 24" src="https://user-images.githubusercontent.com/89058117/148357312-ad94de0a-a71b-465e-a81a-650c09e0d35d.png">
<img width="596" alt="스크린샷 2022-01-06 오후 5 32 09" src="https://user-images.githubusercontent.com/89058117/148357319-45f9a3dc-802e-4ab8-8ef2-4b80f5822de5.png">
<img width="567" alt="스크린샷 2022-01-06 오후 5 32 29" src="https://user-images.githubusercontent.com/89058117/148357323-5fd3e688-79d0-47f8-b560-eb9f191f63a8.png">



### app4 에는 post로 만들어줌 토큰 필수!!!!
### urls.py 에  path('start4', app4.views.start4)추가
### subject는 히든값으로 넣어줬기 때문에 홈페이지에선 안보임
<img width="840" alt="스크린샷 2022-01-06 오후 5 47 27" src="https://user-images.githubusercontent.com/89058117/148357386-35026832-de4e-4f6b-9cdb-a710a2a57653.png">
<img width="540" alt="스크린샷 2022-01-06 오후 5 48 23" src="https://user-images.githubusercontent.com/89058117/148357392-230e8ee2-b224-4365-8541-6dfb6388abf5.png">


