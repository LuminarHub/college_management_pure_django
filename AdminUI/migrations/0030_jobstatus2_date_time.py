# Generated by Django 5.0.2 on 2024-03-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminUI', '0029_jobstatus2_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobstatus2',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
