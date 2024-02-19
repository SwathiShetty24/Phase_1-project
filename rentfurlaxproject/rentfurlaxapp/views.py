from django.shortcuts import render
from django.http import JsonResponse
from .models import Register, Category, Product, Invoice 
from .serializers import RegisterSerializer, CategorySerializer, ProductSerializer, InvoiceSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        try:
            if Register.objects.get(username=request.data.get('username')):
                return Response({'message': 'username exists', 'data': 'username is already exists try new username'}, status=status.HTTP_200_OK)
        except Register.DoesNotExist:
            serializer= RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'success', 'data': serializer.data}, status=200)
            else:
                return Response({'message': 'error', 'data': serializer.errors}, status=400)
        except:
            return Response({'message':'error','data':serializer.errors},status=500)
        
class LoginView(APIView):
    def post(self,request):
        username= request.data.get('username')
        password= request.data.get('password')
        try:
            user= Register.objects.get(username= username, password=password)
            return Response({'message': 'Login Successful'}, status=200)
        except Register.DoesNotExist:
            return Response({'message': 'Invalid username or password'}, status=400)


class add_category(APIView):
    #permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer= CategorySerializer(data= request.data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success', 'data': serializer.data}, status=200)
        else:
            return Response({'message': 'error', 'data': serializer.errors}, status=400)
        
  
class add_product(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success', 'data': serializer.data}, status=200)
        else:
            return Response({'message': 'error', 'data': serializer.errors}, status=400)


class get_category(APIView):
    def get(self, request):
        categories= Category.objects.all()
        serializer= CategorySerializer(categories, many=True)
        return Response({'message': 'success', 'data': serializer.data}, status=200)
    

class get_products_by_category(APIView):
    def get(self, request, *args, **kwargs):
        by_category= kwargs.get("category")
        
        try:
            id= Category.objects.get(type=by_category).id
            category= Product.objects.filter(category=id)
            if category:
                serializer= ProductSerializer(category, many=True)
            else:
                return Response({'message':'Not Found','description':f'No Products Found on this category'})
            return Response({'message': 'success', 'data': serializer.data}, status=200)
        except Category.DoesNotExist:
            return Response({'message': 'error', 'data': 'Invalid Category'}, status=400)

class CreateInvoiceView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if request.method == 'POST':
            serializer = InvoiceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

class GetInvoicesView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            orderstatus = kwargs.get("orderstatus")
            if orderstatus:
                invoices = Invoice.objects.filter(status=orderstatus)
                if invoices:
                    serializer = InvoiceSerializer(invoices, many=True)
                    return Response(serializer.data, status=200)
            else:
                result = Invoice.objects.all()
                serializer = InvoiceSerializer(result,many=True)
                return Response({'message':'success','data':serializer.data}, status=200)

        except Invoice.DoesNotExist:
            return Response({"message": f"No invoices with status '{orderstatus}' found."}, status=404)
        except Exception as e:
           return Response({"message": str(e)}, status=500)
        else:
            return Response({"message":"failed","data":f"No Invoice is {orderstatus}"})