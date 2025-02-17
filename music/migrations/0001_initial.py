# Generated by Django 5.1.4 on 2024-12-09 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]
