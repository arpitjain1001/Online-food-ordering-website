# Generated by Django 4.2.1 on 2023-08-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_order_odeer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='food',
            name='fimg',
            field=models.FileField(upload_to='food/'),
        ),
    ]