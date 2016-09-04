""" Models for user profiles """

from django.db import models

class Profile(models.Model):
    """ Custom user profiles model """

    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
    username = models.CharField(max_length = 250)
    email = models.CharField(max_length = 250)
    about = models.TextField(blank = True, null = True)
    github_url = models.URLField(max_length = 250, blank = True, null = True)
    twitter_url = models.URLField(max_length = 250, blank = True, null = True)
    facebook_url =models.URLField(max_length = 250, blank = True, null = True)
    linkedin_url = models.URLField(max_length = 250, blank = True, null = True)
    website = models.URLField(max_length = 250, blank = True, null = True)
    skype_id = models.CharField(max_length = 250, blank = True, null = True)
    phone = models.CharField(max_length = 10, blank = True, null = True)
    template =  models.CharField(max_length='10', default = '1')
    extra = models.TextField(blank = True, null = True)


    class Meta:
        unique_together = ('email',)

    def __str__(self):
        return self.email