from django.db import models
import uuid

# Create your models here.
class Base(models.Model):
	is_active = models.BooleanField(default=True)
	created_date = models.DateTimeField(auto_now=True)
	created_date = models.DateTimeField(auto_now_add=True)
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	is_state_available = models.BooleanField(default=True)
	

	class Meta:
		abstract=True

class Country(Base):
	name = models.CharField(max_length=10)
	slug = models.SlugField(unique=True)
	code = models.CharField(max_length=10,unique=True)
	flag = models.ImageField(upload_to = 'flag')
	
	def __str__(self):
		return self.name


class State(Base):
	name=models.CharField(max_length=100)
	slug=models.SlugField(unique=True)
	language=models.CharField(max_length=100)

	def __str__(self):
		return self.name

class City(Base):
	name=models.CharField(max_length=100)
	slug=models.SlugField(unique=True)

	def __str__(self):
		return self.name
	

	



