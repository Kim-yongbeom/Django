# Generated by Django 3.2.11 on 2022-01-24 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('imgs', models.CharField(max_length=200)),
                ('detail', models.CharField(max_length=200)),
                ('mood1', models.CharField(max_length=200)),
                ('mood2', models.CharField(max_length=200)),
                ('mood3', models.CharField(max_length=200)),
                ('like', models.IntegerField(max_length=10000)),
            ],
        ),
    ]
