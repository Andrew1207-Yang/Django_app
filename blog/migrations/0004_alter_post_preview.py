# Generated by Django 3.2.3 on 2021-06-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210616_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='preview',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
