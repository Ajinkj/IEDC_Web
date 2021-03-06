# Generated by Django 3.0.3 on 2021-05-10 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='all_photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_name', models.CharField(default='IEDC-JECC', max_length=100)),
                ('photo', models.ImageField(upload_to='images/events')),
                ('photo_Desc', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_name', models.CharField(max_length=100)),
                ('Event_photo', models.ImageField(upload_to='images/events')),
                ('Event_short_Desc', models.TextField()),
                ('Event_Description', models.TextField()),
                ('Event_Register_Link', models.CharField(blank=True, max_length=300)),
                ('Photo_1', models.ImageField(blank=True, upload_to='images/events')),
                ('Photo_2', models.ImageField(blank=True, upload_to='images/events')),
                ('Photo_3', models.ImageField(blank=True, upload_to='images/events')),
            ],
        ),
        migrations.CreateModel(
            name='form_msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='iedcinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IEDC_Title', models.CharField(max_length=100)),
                ('IEDC_photo', models.ImageField(upload_to='images/info')),
                ('IEDC_Short_Desc', models.TextField()),
                ('IEDC_long_Desc', models.TextField()),
                ('photos', models.ManyToManyField(blank=True, to='web.all_photos')),
            ],
        ),
    ]
