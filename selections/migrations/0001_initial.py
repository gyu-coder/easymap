# Generated by Django 3.0.8 on 2020-07-17 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bft', models.CharField(max_length=264)),
                ('act1', models.CharField(max_length=264)),
                ('act2', models.CharField(max_length=264)),
                ('lun', models.CharField(max_length=264)),
                ('act3', models.CharField(max_length=264)),
                ('act4', models.CharField(max_length=264)),
                ('din', models.CharField(max_length=264)),
            ],
        ),
    ]
