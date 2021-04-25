from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    # user associated with profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')


    def __str__(self):
        return f'{ self.user.username } Profile'

    def save(self,  *args, **kwargs):
        super(Profile, self).save( *args, **kwargs)

        profile_image = Image.open(self.image.path)

        if profile_image.width > 200 or profile_image.height > 200:
            image_modified_size = (200, 200)
            profile_image.thumbnail(image_modified_size)
            profile_image.save(self.image.path)
