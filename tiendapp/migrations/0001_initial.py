# Generated by Django 5.1.4 on 2024-12-07 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=256)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='products_thumbs/')),
                ('image', models.ImageField(upload_to='products_images/')),
                ('create_date', models.DateField()),
                ('stock', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
