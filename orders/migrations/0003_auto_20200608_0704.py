# Generated by Django 3.0.7 on 2020-06-08 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_pizza_topping_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerorder',
            name='dinnerplatter',
        ),
        migrations.RemoveField(
            model_name='customerorder',
            name='pasta',
        ),
        migrations.RemoveField(
            model_name='customerorder',
            name='pizza',
        ),
        migrations.RemoveField(
            model_name='customerorder',
            name='salad',
        ),
        migrations.RemoveField(
            model_name='customerorder',
            name='sub',
        ),
        migrations.AddField(
            model_name='customerorder',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerorder',
            name='size',
            field=models.CharField(blank=True, default=None, max_length=69),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='topping1',
            field=models.CharField(blank=True, default=None, max_length=69),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='topping2',
            field=models.CharField(blank=True, default=None, max_length=69),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='topping3',
            field=models.CharField(blank=True, default=None, max_length=69),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='type',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=69),
        ),
    ]
