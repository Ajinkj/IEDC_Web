# Generated by Django 3.0.3 on 2021-05-10 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20210510_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='photos',
        ),
        migrations.AddField(
            model_name='events',
            name='photos',
            field=models.ManyToManyField(blank=True, to='web.photos'),
        ),
    ]
