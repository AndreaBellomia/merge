# Generated by Django 4.1.5 on 2023-01-31 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_rename_stato_appointments_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointments',
            old_name='active',
            new_name='stato',
        ),
    ]
