# Generated by Django 2.2.1 on 2019-05-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yb_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='isComplete',
            field=models.BooleanField(default=False),
        ),
    ]
