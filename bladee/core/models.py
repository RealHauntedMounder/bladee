from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse

class Information(models.Model):
    title = models.CharField(max_length=60 ,null=True, blank=True)
    description = models.TextField(null=False)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    video = models.FileField(null=True, blank=True, upload_to='videos/')
    is_bio = models.BooleanField(default=False)

    def __str__(self):
        return self.title if self.title else f'Information object ({self.pk})'
    
class Album(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='images/')
    color = ColorField(default='#FF0000')
    

    def __str__(self):
      return self.title
    
    def get_absolute_url(self):
        return reverse('album_detail', args=[str(self.pk)])
  

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='tracks/')
    
    def __str__(self):
        return self.title
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    liked_albums = models.ManyToManyField(Album, blank=True)
    def __str__(self):
        return self.user.username

class Comment(models.Model):
    album = models.ForeignKey(Album, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.album.title, self.commenter_name)




    


