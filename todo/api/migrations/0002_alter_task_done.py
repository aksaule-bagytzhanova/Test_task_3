# Generated by Django 3.2.5 on 2021-07-19 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
