from django.db import models

class Pastebin(models.Model):
	nick = models.CharField(max_length=20)    
	date = models.DateTimeField()
	textTitle = models.CharField(max_length=120)
	pasteText = models.TextField(max_length=100000)
	expireDate = models.DateTimeField()