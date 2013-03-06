from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    slug = models.SlugField()
    user = models.OneToOneField(User)

    image = models.FileField(upload_to="profiles/")

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    phone = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)

    description = models.TextField()

    def __unicode__(self):
        return self.first_name + " " + self.last_name

class Comment(models.Model):
    sender = models.OneToOneField(Profile, related_name="comment_from")
    to = models.OneToOneField(Profile, related_name="comment_to")

    comment = models.TextField()

    def __unicode__(self):
        return "A comment about %s from %s" % (self.to, self.sender)

class File(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

    file = models.FileField(upload_to="files/")

    def __unicode__(self):
        return self.title
