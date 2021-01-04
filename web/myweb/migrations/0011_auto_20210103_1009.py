# Generated by Django 2.1.5 on 2021-01-03 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0010_iam'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateSkillphoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc4', models.CharField(blank=True, max_length=500)),
                ('img', models.ImageField(default='', upload_to='myweb/images')),
            ],
        ),
        migrations.RemoveField(
            model_name='updateaboutphoto',
            name='desc4',
        ),
        migrations.RemoveField(
            model_name='updateaboutphoto',
            name='img',
        ),
        migrations.AddField(
            model_name='updateaboutphoto',
            name='img1',
            field=models.ImageField(default='', upload_to='myweb/images'),
        ),
    ]