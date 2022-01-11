# ajax, DB

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


