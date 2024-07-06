from django.db import models

# Create your models here.
# import the standard Django Model 
# from built-in library 
from django.db import models 

# declare a new model with a name "GeeksModel" 


class GeeksModel(models.Model): 
		# fields of the model 
	title = models.CharField(max_length=200) 
	description = models.CharField(max_length=500) 
	last_modified = models.DateTimeField(auto_now_add=True) 
	img = models.ImageField(upload_to= "quot images/")
	Example_age = models.IntegerField(null=True)
	vinay=models.CharField(max_length=100)
	ankit=models.CharField(max_length=100)
	Ritendra=models.CharField(max_length=100)
	marks=models.IntegerField(null=True)
	
	# renames the instances of the model 
	# with their title name 
	def __str__(self): 
		return self.title 
class DataApi(models.Model):
	name=models.CharField(max_length=200)
	id=models.IntegerField(primary_key=True)
	sal=models.FloatField(null=True)
class student(models.Model):
	student_name=models.CharField(max_length=50)
	id=models.IntegerField(primary_key=True)
	fee=models.IntegerField(null=True)
class emp(models.Model):
	empname=models.CharField(max_length=200)
	empid=models.IntegerField(primary_key=True)
	sal=models.FloatField(null=True)
	
class User_details(models.Model):                                                     #Table 1
    id = models.AutoField(primary_key=True, db_column='user_id')
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50)


class Extend_user_details(models.Model):                                              #Table 2
    user =models.ForeignKey(User_details, on_delete=models.CASCADE,db_column='user_id')
    mobile = models.BigIntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

	 
	
class displaydata1(models.Model):
	des= models.CharField(max_length=100 ,null=True)
	title=models.TextField()






	
    
