# Generated by Django 3.0.7 on 2020-06-08 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200608_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='status',
            field=models.CharField(blank=True, choices=[('P', 'Pending'), ('A', 'Approved'), ('D', 'Delivering'), ('Dd', 'Delivered')], max_length=2, null=True),
        ),
    ]