# Generated by Django 3.2 on 2021-05-13 17:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0004_auto_20210513_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
