# Generated by Django 2.2.3 on 2019-07-25 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itic', '0006_auto_20190720_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='matter',
            name='semestre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
