from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Prelim(models.Model):
	name = models.CharField(max_length=30)
	bizname = models.CharField(max_length=30)
	email = models.EmailField()

class Item(models.Model):
	id = models.IntegerField(max_length=30, primary_key=True)
	name = models.CharField(max_length=30)
	price=models.DecimalField(decimal_places=2,max_digits=10)
	def __unicode__(self):
		return self.name
	class Admin:
		pass
		
#Defines general user
class UserProfile(models.Model):
	business = models.CharField(max_length=30)
	user = models.ForeignKey(User,unique=True)
	buyer = models.BooleanField(default=False)
	seller = models.BooleanField(default=False)
	catalog = models.ManyToManyField(Item)
	class Admin:
		pass
		
#class Catalog(models.Model):
	#user = models.ForeignKey(UserProfile, related_name='itemseller')
	#item = models.ForeignKey(Item)
	#class Admin:
		#	pass