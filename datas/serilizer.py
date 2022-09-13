
from rest_framework import serializers
from .models import *

class userserilaizer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

class dataserilaizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Datas
        fields = "__all__"

        

class SchoolSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"        

class valueSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Valus
        fields = "__all__"           