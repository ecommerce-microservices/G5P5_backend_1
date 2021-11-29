from rest_framework import views, status
from rest_framework.permissions import IsAuthenticated
import product
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.response import Response


class ProductAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all().order_by('id')
        products_serializer = ProductSerializer(products, many=True)
        
        if not products_serializer.data:
            return Response({"message":"La lista de productos se encuentra vacía"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(products_serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        data = request.data
        product_serializer = ProductSerializer(data=data)
        
        if product_serializer.is_valid(raise_exception=True):
            product_serializer.save()
            return Response({"message":"El producto se agregó exitosamente"}, status=status.HTTP_201_CREATED)
        #return Response({"message":"Petición incorrecta"}, status= status.HTTP_400_BAD_REQUEST)
        
class ProductDetailAPIView(views.APIView):
    def put(self, request, pk, *args, **kwargs):
        data = request.data
        product = Product.objects.filter(id=pk)
        
        if product.exists():
            product = product.first()
            product_serializer = ProductSerializer(product, data=data)        
        
            if product_serializer.is_valid(raise_exception=True):
                product_serializer.save()
                return Response({'message': 'El producto se actualizó exitosamente'}, status=status. HTTP_200_OK)
                
            #return Response({'message': 'No se pudo actualizar el producto'}, status=status. HTTP_200_OK)
                                
        return Response({'message':'No se econtró el registro'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk, *args, **kwargs):
        product = Product.objects.filter(id=pk)
        
        if product.exists():
            product = product.first()
            product.delete()
            return Response({'message': 'El producto se eliminó exitosamente'}, status=status.HTTP_200_OK)
        
        return Response({'message':'No se econtró el producto'}, status=status.HTTP_404_NOT_FOUND)