# Generated by Django 4.1.5 on 2023-04-03 07:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_alter_zisuipost_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zisuipost',
            name='created',
            field=models.DateTimeField(default=datetime.date(2023, 4, 3), verbose_name='作成日'),
        ),
    ]
