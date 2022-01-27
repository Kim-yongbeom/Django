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
    registered_date = models.DateTimeField() # 게시글 작성시간
    comment = models.CharField(max_length=200) # 게시글에 달린 댓글
    like = models.IntegerField() # 게시글 좋아요
    img = models.CharField(max_length=200)  # 게시글 사진 파일 이름

    # @property
    # def created_string(self):
    #     time = datetime.now(tz=timezone.utc) - self.registered_date
    #
    #     if time < timedelta(minutes=1):
    #         return '방금 전'
    #     elif time < timedelta(hours=1):
    #         return str(int(time.seconds / 60)) + '분 전'
    #     elif time < timedelta(days=1):
    #         return str(int(time.seconds / 3600)) + '시간 전'
    #     elif time < timedelta(days=7):
    #         time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
    #         return str(time.days) + '일 전'
    #     else:
    #         return False

class Comment(models.Model):
    bid = models.IntegerField()
    content = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
