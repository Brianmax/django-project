# Generated by Django 4.1.7 on 2023-03-01 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('propertie', '0004_recibo_emmited_date_recibo_expired_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recibo',
            old_name='type',
            new_name='tipo',
        ),
    ]