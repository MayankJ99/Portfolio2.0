# Generated by Django 2.2.12 on 2020-09-09 10:25

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0016_auto_20200904_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
