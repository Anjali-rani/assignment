# Generated by Django 3.0.5 on 2020-08-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(max_length=64)),
                ('sub1', models.CharField(max_length=64)),
                ('sub2', models.CharField(max_length=64)),
                ('sub3', models.CharField(max_length=64)),
                ('sub4', models.CharField(max_length=64)),
                ('sub5', models.CharField(max_length=64)),
                ('sub6', models.CharField(max_length=64)),
                ('sub7', models.CharField(max_length=64)),
                ('sub8', models.CharField(max_length=64)),
            ],
        ),
    ]