# Generated by Django 3.0 on 2021-08-23 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Qn', '0006_auto_20210822_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='submit',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='答卷是否有效'),
        ),
    ]