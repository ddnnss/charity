# Generated by Django 3.0.2 on 2020-02-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0002_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isBest',
            field=models.BooleanField(default=False, verbose_name='Лучший покупатель?'),
        ),
    ]
