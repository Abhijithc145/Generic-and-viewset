
from rest_framework import serializers
from .models import *

class userserilaizer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

class dataserilaizer(serializers.ModelSerializer):
    class Meta:
        model = Datas
        fields = "__all__"

        

class SchoolSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"        