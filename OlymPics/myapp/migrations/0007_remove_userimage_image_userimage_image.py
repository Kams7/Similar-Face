# Generated by Django 4.2.3 on 2023-07-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_userimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userimage',
            name='Image',
        ),
        migrations.AddField(
            model_name='userimage',
            name='image',
            field=models.ImageField(default='user_images/No_Image_Available.jpg', upload_to='user_images'),
        ),
    ]
