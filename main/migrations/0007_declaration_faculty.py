# Generated by Django 2.0.5 on 2018-06-04 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180604_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='declaration',
            name='faculty',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='faculty'),
        ),
    ]
