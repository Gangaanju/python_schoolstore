# Generated by Django 4.2.8 on 2023-12-26 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_form_orderform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderform',
            old_name='username',
            new_name='name',
        ),
    ]
