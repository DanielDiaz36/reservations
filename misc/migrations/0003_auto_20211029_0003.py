# Generated by Django 3.2.8 on 2021-10-29 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0002_reservation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='locator',
            field=models.CharField(max_length=16, unique=True, verbose_name='locator'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pendent', 'pendent'), ('approved', 'approved'), ('rejected', 'rejected'), ('executed', 'executed'), ('not_executed', 'not executed')], max_length=12, verbose_name='status'),
        ),
    ]
