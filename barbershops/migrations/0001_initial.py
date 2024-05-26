# Generated by Django 5.0.6 on 2024-05-26 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barbershop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(verbose_name=11)),
                ('email', models.EmailField(max_length=150)),
                ('password', models.CharField(max_length=255)),
                ('image_profile', models.ImageField(blank=True, null=True, upload_to='media/profile/')),
            ],
        ),
    ]
