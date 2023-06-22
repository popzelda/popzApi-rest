from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from .models import Product
from rest_framework.decorators import api_view
from .serialezers import ProductSerializers
@api_view(['GET'])
def api_view(request):
    
    #query= Product.objects.all().order_by('?').first()
    query= Product.objects.all().order_by('?').first()
    data={}
    if query:
        data= ProductSerializers(query).data
        #data['name']=query.name
        #data['content']=query.content
        #data['price']=query.price
    return Response(data)
