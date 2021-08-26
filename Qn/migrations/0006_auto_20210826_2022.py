# Generated by Django 3.0 on 2021-08-26 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Qn', '0005_auto_20210826_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='has_num_limit',
            field=models.BooleanField(default=False, verbose_name='是否有额度限制'),
        ),
        migrations.AddField(
            model_name='option',
            name='num_limit',
            field=models.PositiveIntegerField(default=0, verbose_name='最大额度'),
        ),
        migrations.AddField(
            model_name='option',
            name='remain_num',
            field=models.PositiveIntegerField(default=0, verbose_name='剩余额度'),
        ),
        migrations.AddField(
            model_name='question',
            name='has_image',
            field=models.BooleanField(default=False, verbose_name='包含图片'),
        ),
        migrations.AddField(
            model_name='question',
            name='has_video',
            field=models.BooleanField(default=False, verbose_name='包含视频'),
        ),
        migrations.AddField(
            model_name='question',
            name='image_url',
            field=models.URLField(default='', verbose_name='图片链接'),
        ),
        migrations.AddField(
            model_name='question',
            name='isVote',
            field=models.BooleanField(default=False, verbose_name='是投票题'),
        ),
        migrations.AddField(
            model_name='question',
            name='video_url',
            field=models.URLField(default='', verbose_name='视频链接'),
        ),
    ]
