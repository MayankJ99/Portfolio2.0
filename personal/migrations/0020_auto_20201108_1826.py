# Generated by Django 3.1.2 on 2020-11-08 18:26

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0019_userprofile_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=markdownx.models.MarkdownxField(blank=True, null=True),
        ),
    ]
