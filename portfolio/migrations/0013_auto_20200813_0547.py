# Generated by Django 3.1 on 2020-08-13 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_auto_20200813_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='company_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]