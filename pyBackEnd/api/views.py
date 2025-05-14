import json

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


# 登陆
@api_view(['GET'])
def hello(request):
    # serializer_class = HelloSerializer

    data = User.objects.all()
    serializer = UserSerializer(data, many=True)
    print(serializer.data)
    return JsonResponse(
        {"message": "Hello from DRF API!", 
         "method": "GET", 
         "data": serializer.data},
        status=status.HTTP_200_OK,
        safe=False
    )


@api_view(['POST'])
def hello_post(request):
    data = json.loads(request.body)
    print(data)
    return Response(
        {"message": "Hello from DRF API!", "method": "POST"},
        status=status.HTTP_200_OK
    )
