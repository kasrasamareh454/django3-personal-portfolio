# Generated by Django 3.0.3 on 2020-03-03 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloginfo',
            old_name='urls',
            new_name='url',
        ),
    ]