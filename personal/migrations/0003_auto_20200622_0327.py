# Generated by Django 2.2.12 on 2020-06-22 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personal', '0002_auto_20200622_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='quote',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='cover',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='work',
            name='company',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='work',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='full_description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='work',
            name='position',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(default='', max_length=255)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
