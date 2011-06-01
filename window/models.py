from django.db import models

class Pastebin(models.Model):
    nick = models.CharField(max_length=20)
    date = models.DateField()
	title = models.CharField(max_length=200)
	pasteText = models.CharField(max_length=100000)
    expireDate = models.DateTimeField()    
    address = models.CharField(max_length=50)