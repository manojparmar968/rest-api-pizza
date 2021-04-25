from django.shortcuts import render
from webapp.models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import traceback
import json

# Create your views here.

class OrderViewSet(viewsets.ViewSet):

    def create(self, request, pk=None):
        try:
            Type = request.data.get('Type')
            Size = request.data.get('Size')
            Added = request.data.get('Added')
            if not Type:
                raise Exception("please enter pizza type")
            if not Size:
                raise Exception("please enter pizza size")
            if not Added:
                raise Exception("please enter pizza toppings")
            pizza_obj = OrderPizza.objects.get_or_create(Type=Type,Size=Size,Added=Added)
            # pizza_obj.save()
            return Response({"message":"Pizza order successfully","success":True},status=status.HTTP_200_OK)
        except Exception as error:
            traceback.print_exc()
            return Response({"message":str(error),"success":False},status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        try:
            pizza_list = [{"id":pizza_obj.id, "type":pizza_obj.Type, "size":pizza_obj.Size, "added":pizza_obj.Added} for pizza_obj in OrderPizza.objects.all()]
            return Response({"data":pizza_list,"success":True},status=status.HTTP_200_OK)
        except Exception as error:
            traceback.print_exc()
            return Response({"message":str(error),"success":False},status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            print("order id = ",pk)
            if not pk:
                raise Exception("please enter order id")
            piza_obj = OrderPizza.objects.get(id=pk)
            
            pizza_data = {
                "id":piza_obj.id,
                "Type":piza_obj.Type,
                "Size":piza_obj.Size,
                "Added":piza_obj.Added,
            }
            return Response({'pizza':pizza_data,"success":True},status=status.HTTP_200_OK)
        except Exception as error:
            traceback.print_exc()
            return Response({"message":str(error),"success":False},status=status.HTTP_200_OK)

    def put(self, request, pk=None, *args, **kwargs):
        try:
            Type = request.data.get('Type')
            Size = request.data.get('Size')
            Added = request.data.get('Added')
            if not Type:
                raise Exception("please enter pizza type")
            if not Size:
                raise Exception("please enter pizza size")
            if not Added:
                raise Exception("please enter pizza toppings")

            pizza_id = OrderPizza.objects.get(id=pk)
            pizza_id. Type = Type
            pizza_id.Added = Added
            pizza_id.Size = Size
            pizza_id.save()
            pizza_data = {
                "id":pizza_id.id,
                "Type":pizza_id.Type,
                "Size":pizza_id.Size,
                "Added":pizza_id.Added,
            }
            return Response({"message":pizza_data,"success":True},status=status.HTTP_200_OK)
        except Exception as error:
            traceback.print_exc()
            return Response({"message":str(error),"success":False},status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        try:
            print("deleted id = ",pk)
            if not pk:
                raise Exception("please enter pizza id")
            OrderPizza.objects.get(id=pk).delete() 
            return Response({"message":"Pizza Entry deleted successfully","success":True},status=status.HTTP_200_OK)
        except Exception as error:
            traceback.print_exc()
            return Response({"message":str(error),"success":False},status=status.HTTP_200_OK)

            