# Generated by Django 3.1.1 on 2020-09-27 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20200927_1402'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formfieldpositions',
            options={'verbose_name_plural': 'Form Field Posiotions'},
        ),
        migrations.RenameField(
            model_name='formfieldpositions',
            old_name='from_name',
            new_name='form_name',
        ),
    ]
