# Generated by Django 4.1.5 on 2023-03-16 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_alter_zisuipost_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zisuipost',
            name='created',
            field=models.DateTimeField(default=datetime.date(2023, 3, 16), editable=False, verbose_name='作成日'),
        ),
        migrations.AlterField(
            model_name='zisuipost',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.date(2023, 3, 16), editable=False, null=True, verbose_name='更新日'),
        ),
    ]