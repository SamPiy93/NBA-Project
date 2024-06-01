from rest_framework import permissions

"""
    Custom permission handling class for Admin
"""
class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated & request.user.groups.all().filter(name='admin').exists()


"""
    Custom permission handling class for Coach
"""
class CoachPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated & request.user.groups.all().filter(name='coach').exists()


"""
    Custom permission handling class for Player
"""
class PlayerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated & request.user.groups.all().filter(name='player').exists()
