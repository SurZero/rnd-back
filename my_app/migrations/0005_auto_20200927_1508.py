# Generated by Django 3.1.1 on 2020-09-27 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20200927_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addresspositions',
            old_name='Country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='addresspositions',
            old_name='Postcode',
            new_name='postcode',
        ),
    ]
