# Generated by Django 3.2.6 on 2021-08-13 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0003_auto_20210811_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='nome',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
