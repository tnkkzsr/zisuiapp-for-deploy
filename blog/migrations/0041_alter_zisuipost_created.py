# Generated by Django 4.1.5 on 2023-03-24 23:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_alter_zisuipost_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zisuipost',
            name='created',
            field=models.DateTimeField(default=datetime.date(2023, 3, 25), verbose_name='作成日'),
        ),
    ]
