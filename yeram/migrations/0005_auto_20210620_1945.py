# Generated by Django 3.2 on 2021-06-20 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yeram', '0004_remove_scrap_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrap',
            name='author',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
