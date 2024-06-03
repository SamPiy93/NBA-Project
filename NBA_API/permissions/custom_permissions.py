from rest_framework import permissions

"""
    Custom permission class handling auth for endpoints related to admin group
"""


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated & request.user.groups.all().filter(name='admin').exists()


"""
    Custom permission class handling auth for endpoints related to coach group
"""


class CoachPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated & request.user.groups.all().filter(name='coach').exists()


"""
    Custom permission class handling auth for endpoints related to player group
"""


class PlayerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated & request.user.groups.all().filter(name='player').exists()
