# Generated by Django 3.1.2 on 2022-03-04 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='done',
            name='date_str',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]