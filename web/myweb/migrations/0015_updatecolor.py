# Generated by Django 2.1.5 on 2021-01-03 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0014_delete_updateskillphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col', models.CharField(max_length=50)),
            ],
        ),
    ]