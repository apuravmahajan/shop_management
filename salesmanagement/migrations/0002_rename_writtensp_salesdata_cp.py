# Generated by Django 5.1.7 on 2025-03-08 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesdata',
            old_name='writtensp',
            new_name='cp',
        ),
    ]
