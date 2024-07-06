from .models import DataApi
from .models import student
from rest_framework import serializers
from .models import User_details
from .models import emp
from .models import Extend_user_details
from.models import displaydata1

class GeeksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=DataApi
        
        fields=["id","name",'sal']
class studentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=['student_name','id','fee']
class empserializer(serializers.ModelSerializer):
    class Meta:
        model=emp
        fields=['empname','empid','sal']
class user_details_serializer(serializers.ModelSerializer):
    class Meta:
        model=User_details
        fields=['id','username','first_name','last_name']
    
class show_data_serializer(serializers.ModelSerializer):
    class Meta:
        model=displaydata1
        fields=['des','title']
    