from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view
from .serializers import *


def purchase_list(request):
    purchases = Purchase.objects.all()
    context = {'purchases':purchases}
    return render(request,'api/purchase.html',context)


@api_view(['GET'])
def purchaseList(request):
    purchases = Purchase.objects.all()
    serializer = PurchaseSerializer(purchases,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def purchaseCreate(request):
    serializer =PurchaseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def purchaseDetailList(request,pk):
    purchase = Purchase.objects.get(id=pk)
    serializer = PurchaseSerializer(purchase,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def purchaseUpdate(request,pk):
    purchase = Purchase.objects.get(id=pk)
    serializer = PurchaseSerializer(instance=purchase,data=request.data,many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def purchaseDelete(request,pk):
    purchase = Purchase.objects.get(id=pk)
    serializer = PurchaseSerializer(instance=purchase,data=request.data,many=False)
    if serializer.is_valid():
        purchase.delete()
    return Response(serializer.data)


@api_view(['POST'])
def purchaseStatus(request):
    purchase = Purchase.objects.filter(status=True)
    serializer = PurchaseSerializer(instance=purchase,data=request.data,many=True)
    return Response(serializer.data)



# @api_view(['POST'])
# def accountRegister(request):
#     if request.method =='POST':
#         serializer = AccountSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
#
#






