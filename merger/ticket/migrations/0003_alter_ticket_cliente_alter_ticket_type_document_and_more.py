# Generated by Django 4.1.5 on 2023-02-18 10:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0002_rename_active_state_tickettype_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='cliente',
            field=models.ForeignKey(on_delete=models.SET('<django.db.models.query_utils.DeferredAttribute object at 0x000001B7FC13A890>'), related_name='cliente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='type_document',
            field=models.ForeignKey(on_delete=models.SET('<django.db.models.query_utils.DeferredAttribute object at 0x000001B7FC152440>'), related_name='ticket', to='ticket.tickettype'),
        ),
        migrations.AlterField(
            model_name='ticketmsg',
            name='autor',
            field=models.ForeignKey(on_delete=models.SET('<django.db.models.query_utils.DeferredAttribute object at 0x000001B7FC13A890>'), related_name='client', to=settings.AUTH_USER_MODEL),
        ),
    ]
