# Generated by Django 4.0.3 on 2022-07-13 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
