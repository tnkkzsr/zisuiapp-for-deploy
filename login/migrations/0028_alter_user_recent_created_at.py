# Generated by Django 4.1.5 on 2023-03-16 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0027_alter_user_recent_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='recent_created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 16, 20, 33, 21, 428466), editable=False, verbose_name='最後の投稿日'),
        ),
    ]
