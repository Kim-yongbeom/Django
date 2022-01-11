# ajax, DB, 회원가입, 수정, 삭제!!

### ajax0.html
- target은 통신시 데이터, 텍스트를 넘겨주는 느낌인것 같다.
- text(), html(), append()가능 append는 버튼 누를때 마다 계속 추가됨
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    {% load static %}
    <script type="text/javascript" src="{% static 'jquery-3.6.0.js' %}"></script>
    <script>
        $(function () {
            $('#b1').click(function () {
                $.ajax({
                    url : "http://127.0.0.1:5555/app5/target0",
                    success : function (response) {
                        alert('받은 응답은 ' + response)
                        $('#d1').html(response)
                    },
                    error : function () {
                        alert('통신 실패@@@@@')
                    }
                })//ajax
            })//b1
             $('#b2').click(function () {
                $.ajax({
                    url : "http://127.0.0.1:5555/app5/target00",
                    success : function (response) {
                        alert('받은 응답은 ' + response)
                        $('#d2').html(response)
                    },
                    error : function () {
                        alert('통신 실패@@@@@')
                    }
                })//ajax
            })//b1
        })//root
    </script>
</head>
<body>
    <button id="b1">ajax test1</button>
    <button id="b2">ajax test2</button>
<hr>
<div id="d1"></div>
<div id="d2"></div>
</body>
</html>
```

### target0.html
```
<h1>
    제품의 단가는 {{ result }}이고,
    총 금액은 {{ sum }}입니다.
</h1>
```

### target00.html
```
오늘 날씨는 {{ today }}이고 미세먼지는 {{ today2 }}이다
```

### 버튼을 누르면 통신
<img width="617" alt="스크린샷 2022-01-11 오전 10 32 03" src="https://user-images.githubusercontent.com/89058117/148865609-36df2fe6-696a-4807-9f22-4c9d447b02f9.png">


### 바로 JSON데이터 받아오기
- views.py에서 새로운 함수만들때 return render말고 return JsonResponse 해주기!!

```
def target(request):
    print('=================== target호출됨.')
    context = {'result' : 100, 'age' : 100, 'tel' : [100, 200, 300]}
    # return render(request, "app5/target.html", context)
    # return HttpResponse(context)
    return JsonResponse(context)
```
- json으로 받아오기
```
$.ajax({
                    url : "http://127.0.0.1:5555/app5/target",
                    success : function (json) {
                        console.log('받은 응답은 ' + typeof(json))
                        console.log('받은 result ' + json.result)
                        console.log('받은 age ' + json.age)
                        //$('#d1').append('- '+json+'<br>')
                    },
                    error : function () {
                        alert('통신 실패@@@@@')
                    }
                })//ajax
```

### map 사용
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    {% load static %}
    <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=키번호"></script>
    <script type="text/javascript" src="{% static 'out.js' %}"></script>
    <script type="text/javascript" src="{% static 'jquery-3.6.0.js' %}"></script>
    <script type="text/javascript">
        function map(lat, lng, divno) {
            var mapContainer = document.getElementById(divno), // 지도를 표시할 div
            mapOption = {
                center: new kakao.maps.LatLng(lat, lng), // 지도의 중심좌표
                level: 3 // 지도의 확대 레벨
            };

            var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

            // 마커가 표시될 위치입니다
            var markerPosition  = new kakao.maps.LatLng(lat, lng);

            // 마커를 생성합니다
            var marker = new kakao.maps.Marker({
                position: markerPosition
            });

            // 마커가 지도 위에 표시되도록 설정합니다
            marker.setMap(map);

            // 아래 코드는 지도 위의 마커를 제거하는 코드입니다
            // marker.setMap(null);
        }

        $(function () {
            //alert('jquery link성공.!!!@@@@@')
           // outCall()
            $('#b1').click(function () {
                $.ajax({
                  url : "http://127.0.0.1:5555/app5/target2",
                  success: function (json) {
                        console.log('내 서버로 ajax통신 성공.!!!')
                        console.log(json)
                        latValue = json.lat
                        lngValue = json.lng
                        map(latValue, lngValue, 'map1')
                    },
                    error : function () {
                        alert('내 서버로 ajax통신 실패.!!!')
                    }
                })
            })
            $('#b2').click(function () {
                $.ajax({
                  url : "http://127.0.0.1:5555/app5/target3",
                  success: function (json) {
                        console.log('내 서버로 ajax통신 성공.!!!')
                        console.log(json)
                        latValue = json.lat
                        lngValue = json.lng
                        map(latValue, lngValue, 'map2')
                    },
                    error : function () {
                        alert('내 서버로 ajax통신 실패.!!!')
                    }
                })
            })
        })
    </script>
</head>
<body>
<hr>
<button id="b1">AJAX Test(종로3가)</button><button id="b2">AJAX Test(동대문)</button>
<table>
    <tr>
        <td>(종로3가)</td> <td>(동대문)</td>
    </tr>
    <tr>
        <td><div id="map1" style="width:500px;height:350px;"></div></td>
        <td><div id="map2" style="width:500px;height:350px;"></div></td>
    </tr>
</table>


</body>
</html>
```
<img width="1042" alt="스크린샷 2022-01-11 오전 11 26 04" src="https://user-images.githubusercontent.com/89058117/148870452-f43d85bd-837d-457a-9431-c05983f2ac40.png">

### jquery안에서 태그가능!!
```
$('#comment').click(function () {
                $.ajax({
                  url : "http://127.0.0.1:5555/app5/target4",
                  success: function (json) {
                      console.log('내 서버로 ajax통신 성공.!!!')
                      console.log(json)
                      commentValue = json.comment
                      scoreValue = json.score
                      for (i=0;i<commentValue.length;i++){
                        $('#cmt').append("<img src='https://www.ikea.com/kr/ko/images/products/synnerby-tri-fold-mirror-grey__0956671_pe804760_s5.jpg?f=xl' style='height: 100px;width: 100px'>"
                           +commentValue[i]+' '+scoreValue[i]+'점'+'<br>')
                      }
                    },
                    error : function () {
                        alert('내 서버로 ajax통신 실패.!!!')
                    }
                })
            })
```

### 장고에서 sql문대신 사용할 수 있음!!
### python ./manage.py shell 
- from app5.models import Test
- Test.object.all()
    - <QuerySet [<Test: park, 011, mulae>, <Test: apple, 012, kangnam>, <Test: song, 013, shinchon>]>
- Test.objects.filter(addr = 'mulae')
    - <QuerySet [<Test: park, 011, mulae>]>
- Test.objects.filter(tel = '011', name = 'park')
    - <QuerySet [<Test: park, 011, mulae>]>
- Test.objects.filter(id='1')
    - <QuerySet [<Test: park, 011, mulae>]>
- Test.objects.filter(id ='1').delete()
    - (1, {'app5.Test': 1})
- Test.objects.all()
    - <QuerySet [<Test: apple, 012, kangnam>, <Test: song, 013, shinchon>]>
- Test.objects.exclude(addr='mulae')
    - <QuerySet [<Test: apple, 012, kangnam>, <Test: song, 013, shinchon>]>
- t1 = Test(name='kim', tel='014', addr='samsung')
- t1.save()
- Test.objects.all()
    - <QuerySet [<Test: apple, 012, kangnam>, <Test: song, 013, shinchon>, <Test: kim, 014, samsung>]>
- t2 = Test(name='kim', tel='015', addr='jonro')
- t2.save()
- Test.objects.all()
    - <QuerySet [<Test: apple, 012, kangnam>, <Test: song, 013, shinchon>, <Test: kim, 014, samsung>, <Test: kim, 015, jonro>]>
<img width="658" alt="스크린샷 2022-01-11 오후 2 51 52" src="https://user-images.githubusercontent.com/89058117/148888631-48891748-28d2-438f-a02e-39df5f5518f7.png">

### sql문을 통해 DB데이터를 views.py 에 함수 추가해줌
<img width="450" alt="스크린샷 2022-01-11 오후 3 21 36" src="https://user-images.githubusercontent.com/89058117/148891688-29e13f61-ca4d-4134-b203-60ded0715377.png">

### test.html(웹에 DB데이터)
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% if test_list %}
    {% for one in test_list %}
        회원id: {{ one.id }} <br>
        회원name: {{ one.name }} <br>
        회원tel: {{ one.tel }} <br>
        회원addr: {{ one.addr }} <br>
        <hr color="red">
    {% endfor %}
{% endif %}
</body>
</html>
```

### restful api로 상세페이지
<img width="475" alt="스크린샷 2022-01-11 오후 3 40 29" src="https://user-images.githubusercontent.com/89058117/148894938-9322f0a3-147e-4dd3-be9d-865d526f58fe.png">
<img width="449" alt="스크린샷 2022-01-11 오후 3 46 01" src="https://user-images.githubusercontent.com/89058117/148894944-aff7d130-b1d2-4d3c-b498-583629324891.png">
<img width="296" alt="스크린샷 2022-01-11 오후 3 50 12" src="https://user-images.githubusercontent.com/89058117/148894985-83223ffc-8495-460d-b54b-6bff7a681b93.png">
<img width="189" alt="스크린샷 2022-01-11 오후 3 50 19" src="https://user-images.githubusercontent.com/89058117/148894992-86fb26bf-cb46-453e-8fa7-9adf156b7478.png">
<img width="337" alt="스크린샷 2022-01-11 오후 3 50 26" src="https://user-images.githubusercontent.com/89058117/148894993-88d924c6-2e11-4d5f-bfe7-38f5bd54ca21.png">

### 회원가입, 수정, 삭제
<img width="493" alt="스크린샷 2022-01-11 오후 6 06 53" src="https://user-images.githubusercontent.com/89058117/148913240-d3787a2c-e3b3-413b-8f5a-ad1a561faf47.png">
<img width="669" alt="스크린샷 2022-01-11 오후 6 07 06" src="https://user-images.githubusercontent.com/89058117/148913248-f3056691-de09-467c-9e77-b5b06b2b8eb4.png">
<img width="522" alt="스크린샷 2022-01-11 오후 6 07 16" src="https://user-images.githubusercontent.com/89058117/148913255-7045ff72-8c55-45a7-a58b-4a697ac61dc9.png">
<img width="495" alt="스크린샷 2022-01-11 오후 6 07 25" src="https://user-images.githubusercontent.com/89058117/148913261-2e652c80-7cb3-44e5-804a-cfac64cd5e45.png">


- 회원목록페이지로, 회원가입페이지로 test.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<a href="/app5/member/create">
    <button style="background: red">회원가입 페이지로</button>
</a>
<hr>
{% if test_list %}
    {% for one in test_list %}
        <a href="/app5/test/{{ one.id }}">
        <button style="background: tan">회원상세페이지로</button>
        </a><br>
        회원id: {{ one.id }} <br>
        회원name: {{ one.name }} <br>
        회원tel: {{ one.tel }} <br>
        회원addr: {{ one.addr }} <br>
        <hr color="red">
    {% endfor %}
{% endif %}
</body>
</html>
```

- 회원가입 페이지 create.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        *{
            text-align: center;
        }
        .td1{
            width: 100px;
            background: aqua;
        }
        .td2{
            width: 250px;
            background: cornsilk;
        }
        button {
            color: red;
            background: white;
        }
        button:hover{
            font-weight: bold;
            background: red;
            color: white;
        }
    </style>
</head>
<body>
<form action="/app5/member/create2"  method="post">
    {% csrf_token %}
<table border="1">
    <tr>
        <td class="td1">항목</td>
        <td class="td2"><input name="name" value=" "></td>
    </tr>
    <tr>
        <td class="td2">입력값</td>
        <td class="td2"><input name="tel" value=" "></td>
    </tr>
    <tr>
        <td class="td3">입력값</td>
        <td class="td2"><input name="addr" value=" "></td>
    </tr>
    <tr>
        <td colspan="2">
            <button>가입</button>
        </td>
    </tr>
</table>

</form>

</body>
</html>
```

- 회원 상세페이지 person.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        body{
            background: lightsalmon;
        }
    </style>
</head>
<body>
{% if one %}
    회원id: {{ one.id }} <br>
    회원name: {{ one.name }} <br>
    회원tel: {{ one.tel }} <br>
    회원addr: {{ one.addr }} <br>
{% endif %}
<hr color="white">
<a href="/app5/test/del/{{ one.id }}">
    <button style="background: cadetblue">회원삭제페이지로</button>
</a>
<a href="/app5/test/up/{{ one.id }}">
    <button style="background: red">회원수정페이지로</button>
</a>
</body>
</html>
```


- 수정 update.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        *{
            text-align: center;
        }
        .td1{
            width: 100px;
            background: aqua;
        }
        .td2{
            width: 250px;
            background: cornsilk;
        }
        button {
            color: red;
            background: white;
        }
        button:hover{
            font-weight: bold;
            background: red;
            color: white;
        }
    </style>
</head>
<body>
<h1>내용을 수정해주세요.</h1>
<hr color="blue">
<form action="/app5/test/up2/go"  method="post">
    {% csrf_token %}
<table border="1">
    <tr>
        <td class="td1">항목</td>
        <td class="td2">입력값</td>
    </tr>
    <tr>
        <td class="td1">아이디</td>
        <td class="td2"><input name="id" value="{{ one.id }}" readonly></td>

    <tr>
        <td class="td1">이름</td>
        <td class="td2"><input name="name" value="{{ one.name }}"></td>
    </tr>
    <tr>
        <td class="td1">전화번호</td>
        <td class="td2"><input name="tel" value="{{ one.tel }}"></td>
    </tr>
    <tr>
        <td class="td1">주소</td>
        <td class="td2"><input name="addr" value="{{ one.addr }}"></td>
    </tr>
    <tr>
        <td colspan="2">
            <button>수정 완료</button>
        </td>
    </tr>
</table>

</form>
</body>
</html>
```
