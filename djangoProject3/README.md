# url파일 연결, js, css , jquery, 사진넣기, static폴더사용, ajax

### url파일 연결하는법
- app5의 views 파일
<img width="524" alt="스크린샷 2022-01-07 오전 10 30 57" src="https://user-images.githubusercontent.com/89058117/148476576-a41b360b-6317-483f-ae98-b800326dcff8.png">

- app5에 urls 파일 생성후 작성
<img width="395" alt="스크린샷 2022-01-07 오전 10 31 04" src="https://user-images.githubusercontent.com/89058117/148476586-72661b3d-e1bd-49f2-84e6-277592ef8f43.png">

- 장고프로젝트의 urls 파일
<img width="329" alt="스크린샷 2022-01-07 오전 10 31 15" src="https://user-images.githubusercontent.com/89058117/148476589-fa697605-1f50-417b-baf4-3c53a0369546.png">

- 장고프로젝트의 views 파일
<img width="345" alt="스크린샷 2022-01-07 오전 10 31 25" src="https://user-images.githubusercontent.com/89058117/148476591-082dfee0-5f00-4a41-829a-1d95ebdea10d.png">
----------------------------------------------------------------------------------------------------------------------------------

### 자바스크립트
- 위에서 이미 app5를 include로 받아왔기 때문에 파일에 추가만 해주면 된다.
- app5의 views 파일
<img width="532" alt="스크린샷 2022-01-07 오전 10 53 26" src="https://user-images.githubusercontent.com/89058117/148478603-2fcedee2-60c8-4335-9b52-acf0a3ca075b.png">

- app5의 urls 파일
<img width="376" alt="스크린샷 2022-01-07 오전 10 56 00" src="https://user-images.githubusercontent.com/89058117/148478800-06dc30eb-8b2d-4708-863c-33d47be6130a.png">

- js01.html 파일
<img width="433" alt="스크린샷 2022-01-07 오전 10 56 27" src="https://user-images.githubusercontent.com/89058117/148478842-97e6a306-387a-4f1a-ae2e-e1f993f7847e.png">

### jquery
<img width="785" alt="스크린샷 2022-01-07 오후 2 51 51" src="https://user-images.githubusercontent.com/89058117/148498513-264d7494-0da5-48b2-8970-25a901e31ac1.png">
<img width="620" alt="스크린샷 2022-01-07 오후 3 09 07" src="https://user-images.githubusercontent.com/89058117/148500048-b1f58b68-2fce-4c8c-9f8f-bd52c8d44ad6.png">
<img width="250" alt="스크린샷 2022-01-07 오후 3 09 12" src="https://user-images.githubusercontent.com/89058117/148500053-d8af91f5-a657-40a0-a8eb-0797ca9cf5bc.png">

### static 폴더에 이미지, jquery, css, js 넣기
<img width="223" alt="스크린샷 2022-01-07 오후 4 20 43" src="https://user-images.githubusercontent.com/89058117/148507044-5180a0d0-fa84-4a02-8080-cdabc56899fe.png">

### 임의로 만들어준 static폴더 사용하기 위해선 장고프로젝트 셋팅.py추가
```
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```
<img width="601" alt="스크린샷 2022-01-07 오후 4 27 57" src="https://user-images.githubusercontent.com/89058117/148507865-b4c95fa0-5b2d-40c4-8286-dbc9dfc65dce.png">

### js06파일 -> 사진넣기, static폴더 사용하는법
<img width="696" alt="스크린샷 2022-01-07 오후 4 40 16" src="https://user-images.githubusercontent.com/89058117/148509211-3636c022-609f-4f86-974f-04ab4f77b92b.png">


### js06파일 -> ajax (비동기 통신 기술)
<img width="426" alt="스크린샷 2022-01-07 오후 4 55 13" src="https://user-images.githubusercontent.com/89058117/148510936-2b1af710-0b31-4acb-a9e4-3bd9bcb6023c.png">


