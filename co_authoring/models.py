from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


class user_detail(models.Model):
    profile_id = models.OneToOneField(to=User, on_delete=CASCADE)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_profile = models.CharField(max_length=100)




class file_record(models.Model):
    user_detail_id = models.ForeignKey(to=User, on_delete=CASCADE)
    title = models.CharField(max_length=500, null=True)
    authors = models.CharField(max_length=500, null=True)
    abstract = models.CharField(max_length=5000, null=True)
    key_words = models.CharField(max_length=300, null=True)
    introduction = models.CharField(max_length=5000, null=True)
    methods = models.CharField(max_length=5000, null=True)
    results = models.CharField(max_length=5000, null=True)
    conclusion = models.CharField(max_length=5000, null=True)
    references = models.CharField(max_length=5000, null=True)



class user_access(models.Model):
    file_record_access_id = models.ForeignKey(to=file_record, on_delete=CASCADE)
    user_name = models.CharField(max_length=250, null=True)
    owner_name = models.CharField(max_length=250, null=True)
    owner_id = models.IntegerField(null=True)
    paper_title = models.CharField(max_length=1000, null=True)
    access_type = models.CharField(max_length=100, null=True)
    suggestion = models.CharField(max_length=3000, null=True)