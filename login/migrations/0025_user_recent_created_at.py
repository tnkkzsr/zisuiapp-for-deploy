# Generated by Django 4.1.5 on 2023-03-15 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0024_alter_user_consecutive_zisui_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='recent_created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 15, 8, 39, 30, 227425, tzinfo=datetime.timezone.utc), editable=False, verbose_name='最後の投稿日'),
        ),
    ]
