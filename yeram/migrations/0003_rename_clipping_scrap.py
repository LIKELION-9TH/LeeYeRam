# Generated by Django 3.2 on 2021-06-20 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yeram', '0002_rename_scrap_clipping'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clipping',
            new_name='Scrap',
        ),
    ]