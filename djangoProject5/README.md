# ajax

### ajax0.html
- target은 통신시 데이터, 텍스트를 넘겨주는 느낌인것 같다.
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

