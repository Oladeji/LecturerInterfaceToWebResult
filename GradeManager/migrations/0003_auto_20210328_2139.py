# Generated by Django 3.1 on 2021-03-28 21:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('GradeManager', '0002_auto_20210328_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedscores',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 21, 39, 12, 270032, tzinfo=utc), verbose_name='upload date'),
        ),
    ]
