# Generated by Django 4.1.5 on 2023-03-18 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0030_alter_user_recent_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='recent_created_at',
            field=models.DateTimeField(default=datetime.date(2023, 3, 18), editable=False, verbose_name='最後の投稿日'),
        ),
    ]