from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=40)
	subtitle = models.CharField(max_length=80)
	text = models.TextField()
	date = models.DateField()
	topics = models.CharField(max_length=80)
