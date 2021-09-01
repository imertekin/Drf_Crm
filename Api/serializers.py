from django.db.models import fields
from rest_framework import serializers

from Api import models



class LeadsSerializer(serializers.ModelSerializer):
    

    class Meta:
        model=models.Leads
        fields=['id','first_name','last_name','age','email','department','hospital','product','agent']




class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Agent
        fields=['username']




class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Products
        fields=['name']