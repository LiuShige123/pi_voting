# Generated by Django 2.1.5 on 2019-03-08 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='quesiton',
            new_name='question',
        ),
    ]
