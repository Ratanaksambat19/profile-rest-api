from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profile_api import serializers


# Create your views here.
class HelloApiView(APIView):
    """Test API views"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """Returns a list of APIVew features"""
        an_apiview = [
            'Users HTTP methods a function (get, post, patch, put, delete)',
            "Is similar to a traditional Django view",
            "Is mapped manually to URLs",
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({"method": 'PATCH'})

    def delete(self, request, pk = None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'user actions (list, create, retrieve, update, partila_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message':'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello messge"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk = None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk = None):
        """Handle update the object"""
        return Response({'http_method': "PUT"})

    def partial_update(self, request, pk = None):
        """Handle updating part ob object"""
        return Response({"http_method": 'PATCH'})

    def destroy(self, request, pk = None):
        """Handle removing object"""
        return Response({'http_method': "DELETE"})
