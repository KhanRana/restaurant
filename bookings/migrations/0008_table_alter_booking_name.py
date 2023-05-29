# Generated by Django 4.2.1 on 2023-05-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_booking_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField()),
                ('capaciy', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
