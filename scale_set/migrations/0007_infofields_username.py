# Generated by Django 2.2.3 on 2019-07-22 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scale_set', '0006_infofields_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='infofields',
            name='username',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
