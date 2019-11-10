# Generated by Django 2.2.7 on 2019-11-10 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=8)),
                ('time', models.TimeField()),
                ('paid', models.BooleanField()),
                ('left', models.BooleanField()),
            ],
        ),
    ]