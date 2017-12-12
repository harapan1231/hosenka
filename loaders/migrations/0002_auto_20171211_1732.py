# Generated by Django 2.0 on 2017-12-11 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loaders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='form_id',
        ),
        migrations.AddField(
            model_name='agency',
            name='commission_form',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='loaders.CommissionForm'),
        ),
    ]