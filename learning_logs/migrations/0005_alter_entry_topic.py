# Generated by Django 3.2.10 on 2022-06-20 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_topic_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_logs.topic'),
        ),
    ]
