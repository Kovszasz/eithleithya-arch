#https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37
#https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository
#https://github.com/deepmedic/deepmedic
#Export_labelmap_node_from_segmentation_node

from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializers import *
from .functions import *
from rest_framework.permissions import IsAuthenticated,AllowAny
# Create your views here.
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

class FileViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=(AllowAny,)
    
    def create(self,request):
        if User.objects.filter(email=request.data["email"]).exists():
            return Response({'message':False})
        else:
            customer=User.objects.create_user(email=request.data["email"])
            customer.save()
            address=Address.objects.create(
                user=customer, 
                first_name=request.data["first_name"], 
                last_name=request.data["last_name"], 
                address_line1=request.data["address_1"], 
                address_line2=request.data["address_2"], 
                city=request.data["city"],
                country=request.data["country"],
                ZIPcode=int(request.data["ZIP_code"])
                )
            address.save()
            package=Package.objects.get(id=request.data['package'])
            order=Order.objects.create(user=customer, file_3d_printing=request.FILES['US'],package=package)
            order.save()
            receipt=Receipt.objects.create(user=customer,order=order)
            #send_receipt(receipt)
            return Response({'message':True})
