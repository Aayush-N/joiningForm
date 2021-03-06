# Generated by Django 2.0.5 on 2018-06-25 19:31

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20180605_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='conference',
            name='total_experience',
        ),
        migrations.AddField(
            model_name='user',
            name='declared',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='awards',
            name='Spec_awards_particulars',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Particulars'),
        ),
        migrations.AlterField(
            model_name='awards',
            name='international',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='International'),
        ),
        migrations.AlterField(
            model_name='awards',
            name='national',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='National'),
        ),
        migrations.AlterField(
            model_name='awards',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ifsc',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='IFSC'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=cloudinary.models.CloudinaryField(default='na', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='permanent_address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
