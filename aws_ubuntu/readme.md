# aws, 우분투, 파이참에 aws 연결!!

### 1. aws ec2연결 (+ chrome확장app설치, secure shell, mac은 터미널에서!! 본인이 받은 키폴더 안에서 ssh -i ~ 넣기)

### 2. aws ec2 filezilla 연결
- server_practice 레포지토리에서 보기!!

### 3. /var폴더로 이동하여 run폴더와 spool폴더의 권한 확인해보기
- 접속 후 /var써주면 바로 이동 가능
- li -al 해주면 권한 확인 가능

### 4. 연결된 ec2의 ip확인해보기
- ifconfig

### 5. tcp통신으로 설정된 네트워크 포트 확인해보기 netstat -옵션
- netstat -anp tcp

### 6. 연결된 계정의 홈으로 이동

### 7. apple계정 생성하여 sudo그룹으로 포함시키고, apple계정의 모든 그룹 확인
- sudo useradd -m apple
- sudo usermod -aG sudo apple
- groups apple로 확인 가능

### 8. https://tomcat.apache.org/download-80.cgi로 접속하여 8.5.3버전의 core배포중 tar.gz를 다운로드하여 압축 풀어 목록 확인 연결된 계정의 홈디렉토리아래 download폴더를 생성후, 다운로드후, 압축풀 것 sudo wget <url>
- root 폴더에서 sudo wget 주소(https://dlcdn.apache.org/tomcat/tomcat-8/v8.5.73/bin/apache-tomcat-8.5.73.tar.gz)
- tar -zxvf 압축을 풀 파일이름(apache-tomcat-8.5.73.tar.gz)
- tar 파일이라 위의 방법을 취해줌
  
### 9. 8번에서 압축을 푼 폴더로 이동, 숨긴 파일/폴더를 포함한 상세 정보목록을 apache_list.txt로 저장 화면을 깨끗하게 정리 지금까지의 명령어 목록을 프린트하고 history_new.txt로 저장 프린트한 목록 중 최근 목록을 실행 프린트한 목록 중 특정한 번호를 실행
- ls -al > apache_list.txt
- cat apache_list.txt
- history > history_new.txt
- cat history_new.txt
- !65 -> 65번줄 실행
  
  
### 10. history_new.txt의 권한을 내계정은 읽고쓰고실행가능하게, 내그룹은 읽기만, 다른그룹은 권한을 주지 않게 설정 history_new.txt의 파일에 터미널에 프린트된 현재 날짜를 추가(파이프연산자 사용) apache_list.txt의 권한은 나만 읽는 권한 설정
- chmod 740 history_new.txt (7 = rwx 다키기!!, 4, 0)
- 첫번째 자리 내계정, 두번째 자리 그룹, 세번째 자리 전체 그룹
- chmod 400 apache_list.txt
  
  
### 11. 연결된 홈에 문제 3, 4, 5, 6번을 배치처리할 수있는 쉘프로그래밍을 하여 my_move.sh로 저장하여 실행
- vi my_move.sh 에서 코드 작성
- . my_move.sh 로 실행
  
### 12. 8번에서 설치한 웹서버는 자바프로그램으로 구현된 웹서비스를 하기위한 서버입니다. bin폴더로 이동 후 ./start.sh를 실행해보고 출력되는 내용을 확인해보세요.
- Neither the JAVA_HOME nor the JRE_HOME environment variable is defined At least one of these environment variable is needed to run this program
  
### 13. python3을 실행하여 hello를 화면에 출력해보고, python프로그램에서 나오세요.
- python3
- print('hello')
- exit()
  
### 14. 연결된 계정의 홈디렉토리에 python_file폴더를 만들어 모든 권한을 부여하고 확인
- mkdir python_file
  
### 15. vi를 이용하여 hello.py에 hello를 프린트하는 함수를 정의하여 호출하는 프로그램을 완성하시오. python3으로 만든 모듈을 실행하여 결과 확인.
- python3 hello.py
  
### 16. hello.py를 hello2.py로 복사하여 python_file/advanced폴더로 이동

  
### 17. hello2.py에 두 수를 입력받아 사칙연산하는 함수 4개, 입력받아 정수로 변환하는 함수 1개, 터미널에서 입력받는 함수 1개를 정의하여  터미널에서 입력받아 두 수를 정수로 변환하여  사칙연산 함수를 호출하는 프로그래밍 완성하여 실행

  
### 18. python_files폴더 아래의 모든 파일과 폴더를 zip을 이용하여 압축하여 압축된 파일 확인 로그인한 계정의 홈에 move_file폴더를 만들어 압축파일 이동하여 압축해제

  
### 19. 현재 위치 확인, 현재 로그인한 계정의 사용자 변수/시스템 변수 내용 출력

  
### 20. 터미널에서 오늘의 할일을 5개 적어서 today.txt로 저장 vi를 열어 행번호를 표시, 1행으로 이동하여 제목을 --- 오늘의 할일  ----삽입 6행에 --- 내일의 할일 ---삽입, 내일의 할일을 5개 더 추가하여 tomorrow.txt로 저장 터미널에서 tommorrow.txt와 today.txt의 파일 내용을 확인
  
 
  
### Nginx
- systemctl status nginx.service
- sudo apt install nginx
- cd etc
- cd nginx
- cd sites-enabled
- cat default
- root에서 /var/www/html;
- sudo vi index.nginx-debian.html
- 퍼블릭 ip주소 쳐보기
  
### S3
  
![screencapture-s3-console-aws-amazon-s3-bucket-create-2022-01-20-16_42_57](https://user-images.githubusercontent.com/89058117/150295599-6d4866ff-b174-4478-a7cb-2c4e8fcb6a9c.png)
  
  
  - 업로드 할 때 설정!!
  <img width="842" alt="스크린샷 2022-01-21 오전 10 44 24" src="https://user-images.githubusercontent.com/89058117/150450531-11e0c026-0866-4c03-9bae-f1f20c0642b1.png">

  

### I AM 사용자 추가하기

<img width="1440" alt="스크린샷 2022-01-20 오후 4 47 19" src="https://user-images.githubusercontent.com/89058117/150296059-9fe45003-923b-4266-9acd-ccc0c5285b38.png">
<img width="1440" alt="스크린샷 2022-01-20 오후 4 48 10" src="https://user-images.githubusercontent.com/89058117/150296089-28473b76-4f95-47f6-9185-252c126d192a.png">
- 그룹 만들어주고 사용자 새로 만들어 줌 마지막에 csv파일로 저장하는거 있다. 그걸로 저장해주면 키 관리 편함
  
### RDS 만들어준거 DBeaver에 연결
- 엔드포인트 복사해서 서버 호스트에 붙이기
- RDS에서 설정해준 비밀번호 입력
<img width="991" alt="스크린샷 2022-01-20 오후 4 51 04" src="https://user-images.githubusercontent.com/89058117/150296375-751eda03-d5c2-48d3-809c-2b4a3fb0c65c.png">

  
  
- RDS 파라미터그룹에서 utf8로 바꿔주기!!
![screencapture-ap-northeast-2-console-aws-amazon-rds-home-2022-01-20-17_23_52](https://user-images.githubusercontent.com/89058117/150301944-7c641bf0-d2b8-476e-8d6f-52b82b8d0b89.png)

  
- DBeaver에서 utf8로 바꿔주기
<img width="480" alt="스크린샷 2022-01-20 오후 5 28 50" src="https://user-images.githubusercontent.com/89058117/150301630-b0e3fa58-53ac-4306-9466-aeeb4bdf0b5c.png">

  
### 터미널에서 RDS mysql 연결해주기
- sudo mysql -h (엔드포인트 복사!!) -u root -p 
- 비밀번호는 RDS에서 설정해준 비밀번호 입력
  
### EC2
- 인스턴스 아이디 -> 보안 -> 보안그룹 확인 (launch-wizard-8)
- 네트워크 및 보안 -> 보안그룹 -> 보안그룹 동일한 이름 확인 후 클릭 -> 인바운드 규칙 편집
<img width="1400" alt="스크린샷 2022-01-20 오후 6 30 35" src="https://user-images.githubusercontent.com/89058117/150311721-564cf6db-c845-40ea-92b0-3de048c93055.png">
  
  
  ## 파이참에 연결
  

  
  ### 파이참에 설치할 라이브러리
  - pip install boto3 
  - pip install django-storages
  
  
  ### static에 있는 파일들 다 올리는 명령어
  - python ./manage.py collectstatic
  - s3에 올라와 있는것을 확일할 수 있다.
  
  ### 파이참 설정에서 python interpreter에서 PyMySQL, mysqlclient 설치!!
  - 설정창에서 추가 안되면 
  - sudo pip install 고고

  
  ### 설치받고 셋팅.py에 추가
  - import pymysql
  - pymysql.install_as_MySQLdb()
  
  ### Database 추가해줌 !!
  - 코드는 project 폴더에서 확인!
  
  ### models.py
  - python manage.py makemigration (생략)
  - python manage.py migrate
  
  ### ALLOWED_HOSTS에  = ['*'] 추가!!!
  
  
  ### 전체적인 코드
  ```
  """
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import pymysql
from pathlib import Path
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*0=3w&xse0a*&wb&+@gw@egm*y-c*25xpw*i&@stvs)%=pe#vg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainPage.apps.MainpageConfig',
    'storages', # s3 파일  storages추가해줌
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql', # 고정
        'NAME': 'mldb', # DB 이름
        'USER': 'root', # 계정
        'PASSWORD': 'high1234', # 암호
        'HOST': 'database-1.cf5t92t5we65.us-east-2.rds.amazonaws.com', # IP RDS 엔드포인트 복사
        'PORT': '3306' # 별도로 설정한 게 아니라면 3306일 것이다.
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# 파일의 끝에 AWS 관련 내용을 추가
AWS_ACCESS_KEY_ID = '아이디' #인증받은 키 아이디 -> I AM에서 인증받은 사용자 키!!
AWS_SECRET_ACCESS_KEY = '비번비번' # 비번
AWS_S3_REGION_NAME = 'us-east-2' #지역
AWS_STORAGE_BUCKET_NAME = 'high03' # s3 이름
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
AWS_DEFAULT_ACL = 'public-read'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATICFILES_STORAGE = 'project.storage.S3StaticStorage' # storage생성해준 다음 작성!!

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

  ```
  
  ### 깃허브 클론을 통해 우분투 넣는 과정들
  - sudo apt update
  - cd venvs/
  - sudo apt install python3-venv
  - ls
  - cd venvs/
  - mkdir project2
  - mkdir venvs
  - cd venvs
  - python3 -m venv mysite2
  - ls
  - cd mysite2/
  - ls
  - cd bin
  - ls -al
  - ls
  - . activate
  - cd ~
  - ls
  - cd venvs
  - cd ..
  - cd venvs/mysite2/bin
  - ls
  - pip install wheel
  - pip install django==3.2.11
  
  - 우분투 서버에서 새로 설치
  - pip install boto3
  - pip install django-storages
  - git clone https://github.com/Kim-yongbeom/Django.git
  - 서버 실행할 폴더로 들어가준다
  - python ./manage.py runserver 0:5555
  
  
  ### 파일질라
  - mysite2 가상환경을 들어가준 후에 실행
  
  ### 페이지 들어가는 법!!
  - ec2  퍼블릭 ip주소 52.79.236.205
  - 실행해준 포트 번호 나는 5555 선호
  - 52.79.236.205:5555 로 들어가 보렴
