# Generated by Django 3.0.2 on 2020-02-18 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_fond_isother'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fond',
            name='isOther',
        ),
    ]