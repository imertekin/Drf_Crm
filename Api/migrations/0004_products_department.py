# Generated by Django 3.2.6 on 2021-09-02 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_auto_20210901_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='department',
            field=models.CharField(choices=[('GS', 'General_service'), ('NEU', 'Neurology'), ('ONC', 'Oncology'), ('PSY', 'Psychiatry'), ('PDT', 'Pediatrics'), ('DRT', 'Dermatology')], default='GS', max_length=3, verbose_name='Department'),
        ),
    ]