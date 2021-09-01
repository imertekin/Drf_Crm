

from rest_framework import generics, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets,mixins

from Api.serializers import LeadsSerializer,AgentSerializer

from Api.models import Leads,Agent,Products


# Create your views here.

class LeadViewSet(viewsets.ViewSet):
    
    def lead_list(self,request):
        queryset = Leads.objects.all()
        serializer= LeadsSerializer(queryset,many=True)
        return Response(serializer.data)

    def create_lead(self,request):
        serializer=LeadsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'message':'Wrong data '},status=status.HTTP_400_BAD_REQUEST)


    def retrive_lead(self,request,pk):
        queryset=Leads.objects.filter(pk=pk)

        if  not queryset:
            return Response({'message':'Lead Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer=LeadsSerializer(queryset.get(id=pk))
        return Response(serializer.data,status=status.HTTP_200_OK)



    def update_lead(self,request,pk):
        queryset=Leads.objects.filter(pk=pk)

        if  not queryset:
            return Response({'message':'Lead Not Found'},status=status.HTTP_404_NOT_FOUND)

        serializer=LeadsSerializer(instance=queryset.first(),data=request.data)
        
      

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response({'message':'Wrong data'},status=status.HTTP_400_BAD_REQUEST)
        
    def delete_lead(self,request,pk):
        queryset=Leads.objects.filter(pk=pk)

        if  not queryset:
            return Response({'message':'Lead Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        queryset.get(pk=pk).delete()
        
        return Response({'message':'Lead Deleted'},status=status.HTTP_200_OK)

















    