# Generated by Django 3.0.6 on 2020-09-11 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20200912_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor_feedback',
            name='plasma_bank',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='hospital_feedback',
            name='plasma_bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
