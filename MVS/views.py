from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datas.models import *
from datas.serilizer import *
from rest_framework.viewsets import ViewSet,ModelViewSet



# class SchoolViewsets(ModelViewSet):
#     # def list(self,request):
#     #     courses = Student.objects.all()
#     #     serializers = SchoolSerilizer(courses,many = True)
#     #     return Response(serializers.data)


#     # def retrieve(self,request,pk):
#     #     course = Student.objects.all()
#     #     serializers = SchoolSerilizer(course)
#     #     return Response(serializers.data)

        


#     queryset = Student.objects.all()
#     serializer_class = SchoolSerilizer
