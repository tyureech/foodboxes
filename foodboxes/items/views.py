from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

import requests

from items.models import Items


@api_view(http_method_names=['GET'])
def function_based(request, id):
    response = requests.get('https://raw.githubusercontent.com'
                 '/stepik-a-w/drf-project-boxes/master'
                 '/foodboxes.json').json()
    try:
        return Response(response[id - 1])
    except IndexError:
        return Response(status=status.HTTP_404_NOT_FOUND)



