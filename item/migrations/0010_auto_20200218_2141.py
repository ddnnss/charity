# Generated by Django 3.0.2 on 2020-02-18 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_fond_isother'),
        ('item', '0009_auto_20200216_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='fond',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.Fond', verbose_name='Перечислить в фонд'),
        ),
    ]
