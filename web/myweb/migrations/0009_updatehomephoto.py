# Generated by Django 2.1.5 on 2021-01-03 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0008_updateaboutphoto_desc4'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateHomePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(default='', upload_to='myweb/images')),
            ],
        ),
    ]
