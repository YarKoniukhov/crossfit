# Generated by Django 4.0.6 on 2022-07-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='closed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='opened_at',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
