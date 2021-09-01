from django.db import models

from Api import utility

# Create your models here.

class Leads(models.Model):
    first_name=models.CharField(max_length=20,verbose_name='First Name')
    last_name=models.CharField(max_length=20,verbose_name='Last Name')
    age=models.PositiveIntegerField(default=18)
    email=models.EmailField(max_length=50,blank=True,null=True)
    department=models.CharField(max_length=3,choices=utility.DEPARTMENT,verbose_name='Department')
    hospital=models.CharField(max_length=250,verbose_name='Hospital')
    product=models.ForeignKey('Products',on_delete=models.CASCADE,verbose_name='Product',blank=True,null=True)
    agent=models.ForeignKey('Agent',on_delete=models.CASCADE,verbose_name='Agent',blank=True,null=True)

    class Meta:
        verbose_name_plural='Leads'

    def __str__(self) :
        return self.first_name + ' ' + self.last_name




class Agent(models.Model):
    username=models.CharField(max_length=20,verbose_name='Username')




    def __str__(self) :
        return self.username


class Products(models.Model):

    name=models.CharField(max_length=20,verbose_name='Name')




    def __str__(self) :
        return self.name