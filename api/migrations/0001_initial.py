# Generated by Django 3.0.1 on 2020-02-14 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parkir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=20, null=True)),
                ('booking_place', models.CharField(max_length=10)),
                ('book_status', models.BooleanField(null=True)),
            ],
        ),
    ]
