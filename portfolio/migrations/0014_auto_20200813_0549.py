# Generated by Django 3.1 on 2020-08-13 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_auto_20200813_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='company_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
