# Generated by Django 4.1.4 on 2023-01-18 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_viaggidafare_rename_viaggi_viaggifatti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaggidafare',
            name='Attivita',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='viaggifatti',
            name='Descrizione',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
