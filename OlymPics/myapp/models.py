from django.db import models

# Create your models here.
# kams1234 - admin_password


class UserImage(models.Model):
    name = models.CharField(max_length=100, default='user')
    image = models.ImageField(upload_to='user_images',
                              default='user_images/No_Image_Available.jpg')

    class Meta:
        verbose_name_plural = 'User Images'
