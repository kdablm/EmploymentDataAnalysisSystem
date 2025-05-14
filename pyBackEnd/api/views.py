import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


@api_view(['GET'])
def hello(request):
    # serializer_class = HelloSerializer
    return Response(
        {"message": "Hello from DRF API!", "method": "GET"},
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def hello_post(request):
    data=json.loads(request.body)
    print(data)
    return Response(
        {"message": "Hello from DRF API!", "method": "POST"},
        status=status.HTTP_200_OK
    )
