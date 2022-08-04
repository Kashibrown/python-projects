from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import Fruit
from .serializers import FruitSerializer


@api_view(['POST']) 
def post_item(request):
    serializer = FruitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def get_item(request):
    fruits = Fruit.objects.all()
    serializer = FruitSerializer(fruits ,many=True) 
    return Response(serializer.data)