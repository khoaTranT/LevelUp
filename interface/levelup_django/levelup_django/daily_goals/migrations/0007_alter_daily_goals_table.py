# Generated by Django 5.1.6 on 2025-03-01 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily_goals', '0006_alter_daily_goals_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='daily_goals',
            table='healthgoals',
        ),
    ]
