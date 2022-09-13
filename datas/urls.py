from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("value/",sample.as_view(),name="value"),
    path("value/<int:pk>",sampledata.as_view(),name="values"),
    path("data/",DataList.as_view()),
    path("data/<int:pk>",views.DataLists.as_view()),
    
]