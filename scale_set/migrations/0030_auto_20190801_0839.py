# Generated by Django 2.2.3 on 2019-08-01 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scale_set', '0029_auto_20190801_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infofields',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
