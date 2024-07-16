from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50)
    pwd = models.CharField(max_length=15)
    class Meta:
        db_table = "user"
class admin(models.Model):
    name = models.CharField(max_length=50)
    pwd = models.CharField(max_length=15)
    class Meta:
        db_table = "admin"
class verify(models.Model):
    name = models.CharField(max_length=50)
    pwd = models.CharField(max_length=15)
    class Meta:
        db_table = "verify"
        
class AudioFile(models.Model):
    filename = models.CharField(max_length=50)
    fileurl = models.CharField(max_length=200)

    class Meta:
        db_table = "audio_files"

class rockfile(models.Model):
    filename = models.CharField(max_length=50)
    fileurl = models.CharField(max_length=200)

    class Meta:
        db_table = "rockfile"

class kksongs(models.Model):
    filename = models.CharField(max_length=50)
    fileurl = models.CharField(max_length=200)

    class Meta:
        db_table = "kksongs"

class usersongs(models.Model):
    filename = models.CharField(max_length=50)
    fileurl = models.CharField(max_length=200)

    class Meta:
        db_table = "usersongs"