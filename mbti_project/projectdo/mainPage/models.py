from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    mood = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    mood_pic = models.CharField(max_length=500)
    detail_pic = models.CharField(max_length=500)
    mood1 = models.CharField(max_length=200, null=True)
    mood2 = models.CharField(max_length=200, null=True)
    mood3 = models.CharField(max_length=200, null=True)
    minimal = models.IntegerField()
    modern = models.IntegerField()
    natural = models.IntegerField()
    casual = models.IntegerField()
    romantic = models.IntegerField()
    individuality = models.IntegerField()
    useful = models.IntegerField()
    vintage = models.IntegerField()
    likes = models.IntegerField(null=True, blank=True)
    ENFJ = models.FloatField()
    ENFP = models.FloatField()
    ENTJ = models.FloatField()
    ENTP = models.FloatField()
    ESFJ = models.FloatField()
    ESFP = models.FloatField()
    ESTJ = models.FloatField()
    ESTP = models.FloatField()
    INFJ = models.FloatField()
    INFP = models.FloatField()
    INTJ = models.FloatField()
    INTP = models.FloatField()
    ISFJ = models.FloatField()
    ISFP = models.FloatField()
    ISTJ = models.FloatField()
    ISTP = models.FloatField()

    def __str__(self):
        return str(self.id) + ' , ' + self.name + ' , ' + self.category + ' , ' + self.mood_pic + ' , ' + self.detail_pic

class Board(models.Model):
    title = models.CharField(max_length=200) # 게시글 제목
    content = models.CharField(max_length=500) # 게시글 내용
    writer = models.CharField(max_length=200) # 게시글 작성자
    registered_date = models.DateTimeField(auto_now_add=True) # 게시글 작성시간
    like = models.IntegerField(null=True) # 게시글 좋아요
    img = models.ImageField(upload_to='images/', default='KakaoTalk_Photo_2022-01-18-15-42-07.jpeg', null=False)  # 게시글 사진 파일 이름

