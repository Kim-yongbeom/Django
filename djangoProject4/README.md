# jquery UI, 비밀번호입력, 결제시스템 외부API, DB데이터 연결, 지도API

## jquery UI 다양한 기능이 있다!! 페이지에 코드 그대로 복사할 수 있음

### jquery UI Dialog
```
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>jQuery UI Dialog - Default functionality</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.13.0/themes/base/jquery-ui.css">
  <link rel="stylesheet" href="/resources/demos/style.css">
  <script src="https://code.jquery.com/jquery-3.6.0.js"></script>
  <script src="https://code.jquery.com/ui/1.13.0/jquery-ui.js"></script>
  <script>
  $( function() {
    $( "#dialog" ).dialog();
  } );
  </script>
</head>
<body>

<div id="dialog" title="Basic dialog">
  <p>This is the default dialog which is useful for displaying information. The dialog window can be moved, resized and closed with the &apos;x&apos; icon.</p>
</div>


</body>
</html>
```
<img width="595" alt="스크린샷 2022-01-10 오전 9 37 32" src="https://user-images.githubusercontent.com/89058117/148707725-34676609-831f-4be5-96c6-dd6e360c17c0.png">

### 비밀번호확인, 더하기
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="https://code.jquery.com/jquery-3.6.0.js"></script>
{#    위 코드랑 똑같음 !! #}
{#    {% load static %}#}
{#    <script src="{% static 'jquery-3.6.0.js' %}"></script>#}
    <script type="text/javascript">
        $(function () {
            $('#b2').click(function () {
                {#value는 input태그에만 사용해준다#}
                pw1Value = $('#pw1').val()
                pw2Value = $('#pw2').val()
                pwResult = pw1Value == pw2Value
                if (pwResult){
                    $('#result').html('동일합니다')
                }
                else{
                    $('#result').html('동일하지 않습니다')
                }
            })

            {#keyup은 비밀번호 입력할때마다 동일한지 확인해줌#}
            $('#pw2').keyup(function () {
                pw1Value = $('#pw1').val()
                pw2Value = $('#pw2').val()
                pwResult = pw1Value == pw2Value
                if (pwResult){
                    $('#result').html('동일합니다')
                }
                else{
                    $('#result').html('동일하지 않습니다')
                }
            })
        })
        function pay() {
            {#value는 input태그에만 사용해준다#}
            priceValue = parseInt(document.getElementById('price').value)
            countValue = parseInt(document.getElementById('count').value)
            payValue = priceValue*countValue
            document.getElementById('result').innerText = payValue
        }
    </script>
</head>
<body>
하나당 가격: <input id="price" value="1111"><br>
물건의 개수: <input id="count" value="5"><br>
<button id="b1" onclick="pay()">결제하기</button>
<hr>
{#패스워드는 jquery로#}
패스워드1: <input id="pw1" value="1111"><br>
패스워드2: <input id="pw2" value="1111"><br>
<button id="b2">패스워드 체크</button>
<hr>
<div id="result" style="background: yellow; color: red; font-size: 20px"></div>
</body>
</html>
```
<img width="280" alt="스크린샷 2022-01-10 오전 10 24 08" src="https://user-images.githubusercontent.com/89058117/148709156-49ca0ead-037d-4a18-ba66-819dd2e4843b.png">

### 결제시스템 외부 API
```
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript" src="https://code.jquery.com/jquery-1.12.4.min.js" ></script>
<script type="text/javascript" src="https://cdn.iamport.kr/js/iamport.payment-1.1.5.js"></script>
<script type="text/javascript">
$(function() {
    $('button').click(function() {
        payValue = parseInt($('#price').val()) * parseInt($('#count').val())
        var IMP = window.IMP; // 생략가능
        IMP.init('iamport'); // 'iamport' 대신 부여받은 "가맹점 식별코드"를 사용
        IMP.request_pay({
            pg : 'inicis', // version 1.1.0부터 지원.
            pay_method : 'card',
            merchant_uid : 'merchant_' + new Date().getTime(),
            name : $('#field').val(),
            amount : payValue,
            buyer_email : $('#email').val(),
            buyer_name : $('#userName').val(),
            buyer_tel : $('#contact').val(),
            buyer_addr : '서울특별시 강남구 삼성동',
            buyer_postcode : '123-456',
            m_redirect_url : 'www.yourdomain.com/payments/complete'
        }, function(rsp) {
            if ( rsp.success ) {
                var msg = '결제가 완료되었습니다.';
                msg += '고유ID : ' + rsp.imp_uid;
                msg += '상점 거래ID : ' + rsp.merchant_uid;
                msg += '결제 금액 : ' + rsp.paid_amount;
                msg += '카드 승인번호 : ' + rsp.apply_num;
            } else {
                var msg = '결제에 실패하였습니다.';
                msg += '에러내용 : ' + rsp.error_msg;
            }
            alert(msg);
        });

    })
})
</script>
</head>
<body>
물건의 종류(신발/휴대폰/커피 중 선택): <input id="field" value="신발"><br>
구매자 이름: <input id="userName" value="홍길동"><br>
구매자 연락처: <input id="contact" value="010-4914-2996"><br>
구매자 이메일: <input id="email" value="acllifiw@naver.com"><br>
하나당 가격: <input id="price" value="1000"><br>
물건의 개수: <input id="count" value="5"><br>
<button type="button">결제하기</button>
</body>
</html>


```
<img width="1155" alt="스크린샷 2022-01-10 오전 11 07 26" src="https://user-images.githubusercontent.com/89058117/148710900-86aad01a-2adf-4fe3-97e5-9f7ed9d20321.png">




### DB에서 데이터 가져오기
- app5 views.py에서 db연동 결과를 검색해서 가지오 온다.
```
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript" src="https://code.jquery.com/jquery-1.12.4.min.js" ></script>
<script type="text/javascript" src="https://cdn.iamport.kr/js/iamport.payment-1.1.5.js"></script>
<script type="text/javascript">
$(function() {
    $('button').click(function() {
        var IMP = window.IMP; // 생략가능
        IMP.init('iamport'); // 'iamport' 대신 부여받은 "가맹점 식별코드"를 사용
        IMP.request_pay({
            pg : 'inicis', // version 1.1.0부터 지원.
            pay_method : 'card',
            merchant_uid : 'merchant_' + new Date().getTime(),
            {#string으로 만들어 주기 위해 '' 붙여줌#}
            name : '{{ field }}',
            amount : {{ payValue }},
            buyer_email : '{{ email }}',
            buyer_name : '{{ userName }}',
            buyer_tel : '{{ contact }}',
            buyer_addr : '서울특별시 강남구 삼성동',
            buyer_postcode : '123-456',
            m_redirect_url : 'www.yourdomain.com/payments/complete'
        }, function(rsp) {
            if ( rsp.success ) {
                var msg = '결제가 완료되었습니다.';
                msg += '고유ID : ' + rsp.imp_uid;
                msg += '상점 거래ID : ' + rsp.merchant_uid;
                msg += '결제 금액 : ' + rsp.paid_amount;
                msg += '카드 승인번호 : ' + rsp.apply_num;
            } else {
                var msg = '결제에 실패하였습니다.';
                msg += '에러내용 : ' + rsp.error_msg;
            }
            alert(msg);
        });

    })
})
</script>
</head>
<body>

<button type="button">결제하기</button>
</body>
</html>

```
<img width="447" alt="스크린샷 2022-01-10 오전 11 12 24" src="https://user-images.githubusercontent.com/89058117/148711563-f81317ea-6f81-4da8-b08f-fa55ba81d635.png">
<img width="205" alt="스크린샷 2022-01-10 오전 11 21 08" src="https://user-images.githubusercontent.com/89058117/148711565-d31a4894-3f4e-414f-9e34-d2b3769ff46f.png">

### DB데이터 형태에 따라 불러오는법, for문 사용법
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script type="text/javascript" >
        $(function (){
            $('#b1').click(function (){
                result = {{ site }}[0] + {{ site }}[1] + {{ site }}[2]
                $('div').text(result)
            })

            {#for문 쓰는법!!#}
            names = ''
            {% for one in name %}
                names = names + ' ' + '{{ one }}'
            {% endfor %}
            alert(names)

            {#버튼글씨 DB데이터 넣는법#}
            $('#b2').text('{{ url.u1 }}')
            $('#b3').text('{{ url.u1 }}')
            $('#b4').text('{{ url.u1 }}')
        })
    </script>
</head>
<body>
<button id="b1">나를 눌러요!</button>
<button id="b2"></button>
<button id="b3"></button>
<button id="b4"></button>
<hr color="blue">
<div style="color: indianred"></div>
</body>
</html>
```
<img width="285" alt="스크린샷 2022-01-10 오후 12 26 50" src="https://user-images.githubusercontent.com/89058117/148715168-8d6bb576-f1df-4b4f-947a-a793039d9873.png">


### 카카오맵 API
```
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>마커 생성하기</title>

</head>
<body>
<div id="map" style="width:100%;height:350px;"></div>

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=발급받은 APP KEY를 사용하세요"></script>
<script>
var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng({{ do }}[0],{{ do }}[1]), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

// 마커가 표시될 위치입니다
var markerPosition  = new kakao.maps.LatLng({{ do }}[0],{{ do }}[1]);

// 마커를 생성합니다
var marker = new kakao.maps.Marker({
    position: markerPosition
});

// 마커가 지도 위에 표시되도록 설정합니다
marker.setMap(map);

// 아래 코드는 지도 위의 마커를 제거하는 코드입니다
// marker.setMap(null);
</script>
</body>
</html>
```
<img width="349" alt="스크린샷 2022-01-10 오후 2 13 28" src="https://user-images.githubusercontent.com/89058117/148720907-7b108361-821a-46e6-9ca5-82762f5b78fc.png">
