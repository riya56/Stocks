# Generated by Django 4.0.3 on 2022-04-06 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneymarket', '0008_profile_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_stocks',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='my_stocks',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
