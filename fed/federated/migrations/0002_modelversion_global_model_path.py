# Generated by Django 3.2.5 on 2025-01-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('federated', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelversion',
            name='global_model_path',
            field=models.CharField(blank=True, default='media/global_model.pkl', max_length=255, null=True),
        ),
    ]
