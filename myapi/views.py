from django.shortcuts import render, redirect
from crud.models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.core import serializers


# Create your views here.
class TracksListView(viewsets.ModelViewSet):
    queryset = Tracks.objects.all()
    serializer_class = TracksSerializer


class StudentsListView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def studentview(request, sid):
    try:
        student = Students.objects.get(id=sid)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        student.delete()
        return Response({'msg': f'user deleted'})

    elif request.method == 'GET':
        res = StudentsSerializer(student, context={'request': request})
        return Response(res.data)

    elif request.method == 'PUT':
        req_serialize = StudentsSerializer(student,data=request.data, context={'request': request})
        if req_serialize.is_valid():
            req_serialize.save()
            return Response(req_serialize.data)
        else:
            return Response(req_serialize.errors)
    else:
        return Response({'msg': 'nup'})
