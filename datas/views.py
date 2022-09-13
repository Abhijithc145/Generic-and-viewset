from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serilizer import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.authentication import BaseAuthentication,SessionAuthentication
# view sets 

from rest_framework.viewsets import ViewSet,ModelViewSet
# Create your views here.

class sample(APIView):
    def get(self,request):
        datas = Person.objects.all()
        serializer = userserilaizer(datas,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer =userserilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   


class sampledata(APIView):
    def get(self,request,pk):
        datas = Person.objects.get(id=pk)
        serializer = userserilaizer(datas)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        datas = Person.objects.get(id=pk)

        serializer =userserilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    def delete(self,request,pk):
        Person.objects.get(id = pk).delete()
        return Response(status=status.HTTP_200_OK)   

class DataList(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Datas.objects.all()
    serializer_class = dataserilaizer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)   

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)     

class DataLists(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset = Datas.objects.all()
    serializer_class = dataserilaizer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)  

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)  

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

# view sets 

# class SchoolViewset(ViewSet):
#     print("0000000000000000000000000000000000")
#     def list(self,request):
#         print("pppppppppppppppppppppppppppppppp")
#         courses = Student.objects.all()
#         serializers = SchoolSerilizer(courses,many = True)
#         return Response(serializers.data)


#     def retrieve(self,request,pk):
#         course = Student.objects.all()
#         serializers = SchoolSerilizer(course)
#         return Response(serializers.data)
        
class SchoolViewsets(ModelViewSet):
    # def list(self,request):
    #     courses = Student.objects.all()
    #     serializers = SchoolSerilizer(courses,many = True)
    #     return Response(serializers.data)


    # def retrieve(self,request,pk):
    #     course = Student.objects.all()
    #     serializers = SchoolSerilizer(course)
    #     return Response(serializers.data)

        


    queryset = Student.objects.all()
    serializer_class = SchoolSerilizer


    # authentication_classes
# .............................................    
    # authentication_classes = [BaseAuthentication]
    # permission_classes = [IsAuthenticated]

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
