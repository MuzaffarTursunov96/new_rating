# Generated by Django 3.2.16 on 2022-12-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reytings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='owner_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
