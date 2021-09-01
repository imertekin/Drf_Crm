from rest_framework import permissions


class LeadAgent(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):



        return obj.agent==request.agent
