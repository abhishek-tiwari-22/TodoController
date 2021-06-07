from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiShow,name='API-overview'),
    path('get/<str:pk>/',views.get,name='get'),
    path('getall/',views.getall,name='getall'),
    path('put/<str:pk>/',views.put,name='put'),
    path('create/',views.create,name='create'),
    path('delete/<str:pk>/',views.delete,name='delete'),
    path('demo/', views.DemoView),
]
