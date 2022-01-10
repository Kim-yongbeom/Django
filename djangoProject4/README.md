# jquery UI, 비밀번호입력

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

