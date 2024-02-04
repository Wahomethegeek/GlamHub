# Generated by Django 5.0.1 on 2024-02-03 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_images_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('waiting_approval', 'Waiting approval'), ('active', 'Active'), ('deleted', 'Deleted')], default='active', max_length=50),
        ),
    ]