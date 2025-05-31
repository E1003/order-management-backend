from rest_framework.permissions import BasePermission

class IsAdministrator(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Seller').exists()