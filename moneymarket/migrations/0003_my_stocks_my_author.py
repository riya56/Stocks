# Generated by Django 4.0.3 on 2022-04-03 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moneymarket', '0002_remove_stock_uid_stock_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_stocks',
            name='my_author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='my_uid', to=settings.AUTH_USER_MODEL),
        ),
    ]
