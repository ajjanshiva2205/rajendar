# Generated by Django 2.0.2 on 2019-11-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminMOdel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_email', models.EmailField(max_length=254)),
                ('a_idno', models.IntegerField()),
                ('a_password', models.CharField(max_length=20)),
            ],
        ),
    ]
