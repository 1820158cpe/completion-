# Generated by Django 3.2.10 on 2022-06-21 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_alter_entry_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='photo_add',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
