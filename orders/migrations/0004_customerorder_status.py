# Generated by Django 3.0.7 on 2020-06-08 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200608_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='status',
            field=models.CharField(blank=True, default=None, max_length=69),
        ),
    ]
