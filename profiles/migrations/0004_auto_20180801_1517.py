# Generated by Django 2.0.7 on 2018-08-01 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20180801_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/None/no-img.jpg', upload_to='media/%Y/%m/%d/'),
        ),
    ]