# Generated by Django 3.1.1 on 2021-06-17 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='post',
        ),
    ]
