# Generated by Django 3.2.7 on 2021-09-06 22:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='created',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
