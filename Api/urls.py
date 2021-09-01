from django.urls import path,include

from rest_framework.routers import DefaultRouter

from Api.views import LeadViewSet




urlpatterns = [
    
    path('leads/',LeadViewSet.as_view({
        'get': 'lead_list'
    })),
    path('leads/create/',LeadViewSet.as_view({
        'post':'create_lead'
    })),

    path('leads/<int:pk>/',LeadViewSet.as_view({
        'get': 'retrive_lead'
    })),

     path('leads/update/<int:pk>/',LeadViewSet.as_view({
        'put': 'update_lead'
    })),

     path('leads/delete/<int:pk>/',LeadViewSet.as_view({
        'delete': 'delete_lead'
    })),

]