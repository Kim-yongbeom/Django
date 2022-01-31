from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.CharField(max_length=200)
    userPw = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    mbti = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    like = models.CharField(max_length=200)
    heart = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ', ' + self.userId + ', ' + self.userPw + ', ' + self.nickname \
               + ', ' + self.mbti + ', ' + self.sex + ', ' + self.age + ', ' + self.job + ', ' + self.like \
               + ', ' + self.heart

# class Blog(models.Model):
#     text = models.TextField()