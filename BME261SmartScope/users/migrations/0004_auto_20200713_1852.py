# Generated by Django 3.0.3 on 2020-07-13 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_mails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mails',
            name='document',
            field=models.FileField(null=True, upload_to='documents', verbose_name=''),
        ),
    ]
