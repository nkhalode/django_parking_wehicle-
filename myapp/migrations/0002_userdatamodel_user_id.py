# Generated by Django 3.1.7 on 2021-12-10 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdatamodel',
            name='user_id',
            field=models.CharField(max_length=150, null=True),
        ),
    ]