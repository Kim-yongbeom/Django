# jquery UI, 비밀번호입력, 결제시스템 외부API

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
    var IMP = window.IMP; // 생략가능
    IMP.init('iamport'); // 'iamport' 대신 부여받은 "가맹점 식별코드"를 사용
    IMP.request_pay({
        pg : 'inicis', // version 1.1.0부터 지원.
        pay_method : 'card',
        merchant_uid : 'merchant_' + new Date().getTime(),
        name : '주문명:결제테스트',
        amount : 1000,
        buyer_email : 'iamport@siot.do',
        buyer_name : '구매자이름',
        buyer_tel : '010-1234-5678',
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
<img width="1213" alt="스크린샷 2022-01-10 오전 10 45 23" src="https://user-images.githubusercontent.com/89058117/148710013-b5b336f1-c0b6-4f1b-8850-4cb3f6fb974b.png">
