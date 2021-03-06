# Generated by Django 3.0.6 on 2020-07-21 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_zzim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zzim',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zzims', to='app.Post'),
        ),
        migrations.AlterField(
            model_name='zzim',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zzims', to=settings.AUTH_USER_MODEL),
        ),
    ]
