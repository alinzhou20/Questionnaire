# Generated by Django 3.0 on 2021-08-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Qn', '0004_auto_20210822_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='user_id',
        ),
        migrations.AddField(
            model_name='answer',
            name='username',
            field=models.CharField(blank=True, max_length=128, verbose_name='用户名'),
        ),
    ]