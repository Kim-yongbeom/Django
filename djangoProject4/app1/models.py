from django.db import models

# Create your models here.
## 1. db에 생성할 테이블을 클래스로 정의해 놓으면(상속),
## 2. db에 테이블을 생성할 수 있는 파이썬 파일을 자동 생성해줌.
##      makemigrations(py)
## 3. 위에서 생성한 py파일을 실행해주면, db에 테이블이 자동생성됨
##      migrate

class Test100(models.Model):
    #테이블안에 생성할 컬럼들을 지정
    # id는 설정 안해주면 자동생성됨 무조건
    pw = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self): # 오버라이드
        return self.pw + ", " + self.name

class Test200(models.Model):
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=300)
    tel = models.CharField(max_length=300)

    def __str__(self):
        return self.title + ' : ' + self.content + ' : ' + self.tel