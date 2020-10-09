# Generated by Django 2.2.12 on 2020-10-09 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0017_auto_20200909_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('comment', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('approved_comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='personal.Blog')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
