# Generated by Django 3.2.11 on 2022-02-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0003_delete_comment_remove_board_comment_alter_board_like_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='img',
            field=models.ImageField(default='KakaoTalk_Photo_2022-01-18-15-42-07.jpeg', upload_to='images/'),
        ),
    ]