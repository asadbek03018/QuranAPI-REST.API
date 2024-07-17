# Generated by Django 5.0.2 on 2024-02-27 07:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('profile_image', models.ImageField(upload_to='quran/arabic/author/image/')),
                ('t_yil', models.CharField(max_length=100)),
                ('about', models.TextField()),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authorlar',
            },
        ),
        migrations.CreateModel(
            name='Oyat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sura', models.CharField(max_length=150)),
                ('oyat_number', models.BigIntegerField(default=0)),
                ('tarjima', models.TextField(default='Tarjimasi')),
                ('audio', models.FileField(upload_to='quran/arabic/audio/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quran_arabic.author')),
            ],
            options={
                'verbose_name': 'Oyat',
                'verbose_name_plural': 'Oyatlar',
            },
        ),
        migrations.CreateModel(
            name='Sura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('jami_oyat', models.IntegerField(default=0)),
                ('written', models.CharField(blank=True, max_length=300, null=True)),
                ('oyat', models.ManyToManyField(related_name='oyat', to='quran_arabic.oyat')),
            ],
            options={
                'verbose_name': 'Sura',
                'verbose_name_plural': 'Suralar',
            },
        ),
    ]
