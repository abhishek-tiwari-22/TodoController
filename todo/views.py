from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import *
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def DemoView(request):
    permission_classes = [IsAuthenticated]
    return Response({"ok": "done"})

@api_view(['GET'])
def apiShow(request):
    api_urls={
        'get - get one':'get/id/',
        'getall - get all':'getall/',
        'put - update':'put/id/',
        ' - create': 'create/',
        'delete':'delete/id/',
    }
    return Response(api_urls)

@api_view(['GET'])
def get(request,pk):
    tasks=Task.objects.get(id=pk)
    serializer=TaskSerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getall(request):
    tasks=Task.objects.all()
    serializer=TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def put(request,pk):
    tasks=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=tasks,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer=TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response("Item Deleted")
