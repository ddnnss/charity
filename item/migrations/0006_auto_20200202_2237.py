# Generated by Django 3.0.2 on 2020-02-02 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20200130_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='atIndex',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='image',
        ),
    ]