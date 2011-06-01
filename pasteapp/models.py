from django.db import models

class Pastebin(models.Model):
    nick = models.CharField(max_length=20)
    date = models.DateField()
	#textTitle = models.CharField(max_length=20)
	#pasteText = models.CharField(max_length=10)
    expireDate = models.DateTimeField()    
    address = models.CharField(max_length=50)