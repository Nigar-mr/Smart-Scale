# Generated by Django 2.2.3 on 2019-07-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scale_set', '0002_auto_20190718_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infofields',
            name='weight',
            field=models.IntegerField(max_length=55, null=True),
        ),
    ]