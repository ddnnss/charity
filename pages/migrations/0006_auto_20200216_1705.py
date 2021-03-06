# Generated by Django 3.0.2 on 2020-02-16 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_fond_image_big'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fond',
            name='deviz',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Девиз'),
        ),
        migrations.AlterField(
            model_name='fond',
            name='image',
            field=models.ImageField(blank=True, upload_to='fond/', verbose_name='Лого фонда (225x110)'),
        ),
        migrations.AlterField(
            model_name='fond',
            name='image_big',
            field=models.ImageField(blank=True, upload_to='fond/', verbose_name='Картинка на страницу фонда (1240х600)'),
        ),
    ]
