# Generated by Django 2.2.7 on 2021-05-13 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ponics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('ponics_type', models.CharField(max_length=255, verbose_name='Тип поники')),
                ('size', models.CharField(max_length=255, verbose_name='Размеры')),
                ('volume_back', models.CharField(max_length=255, verbose_name='Объем бака')),
                ('color', models.CharField(max_length=255, verbose_name='Цвет корпуса')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PartsFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('type_parts', models.CharField(max_length=255, verbose_name='Тип детали для каркаса')),
                ('lenght', models.CharField(max_length=255, verbose_name='Длина')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
