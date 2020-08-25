from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    """Test API views"""

    def get(self, request, format = None):
        """Returns a list of APIVew features"""
        an_apiview = [
            'Users HTTP methods a function (get, post, patch, put, delete)',
            "Is similar to a traditional Django view",
            "Is mapped manually to URLs",
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
