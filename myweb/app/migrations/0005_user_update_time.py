# Generated by Django 4.0.6 on 2022-07-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_user_update_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='update_time',
            field=models.DateField(max_length=32, null=True, verbose_name='修改日期'),
        ),
    ]