# Generated by Django 3.1.1 on 2020-09-10 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200715_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(default='published', max_length=10),
        ),
    ]
