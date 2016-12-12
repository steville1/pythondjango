from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Assignment(models.Model):
	names=models.CharField(max_length=100)
	email=models.CharField(max_length=100)

	def __str__ (self):
		return self.names + '-' +self.email

	#def __unicode__(self):
		#return self.names + '-' +self.email
