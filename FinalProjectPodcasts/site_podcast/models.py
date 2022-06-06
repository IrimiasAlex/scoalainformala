from django.db import models


class Podcasts(models.Model):
    podcasts = models.CharField(max_length=100, default='Some String')
    searching = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='podcasts', null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    web = models.URLField(max_length=100, null=True, blank=True)


    def __str__(self):
        return f"{self.podcasts}"