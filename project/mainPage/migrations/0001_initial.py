# Generated by Django 3.2.11 on 2022-01-14 06:33

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
                ('imgs', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('mood1', models.CharField(max_length=200)),
                ('mood2', models.CharField(max_length=200)),
                ('mood3', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
    ]
