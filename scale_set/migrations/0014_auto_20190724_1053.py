# Generated by Django 2.2.3 on 2019-07-24 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scale_set', '0013_auto_20190724_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infofields',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
