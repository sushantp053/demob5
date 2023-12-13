from rest_framework import serializers 
from home.models import *

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['name', 'roll', 'city', 'marks' ]