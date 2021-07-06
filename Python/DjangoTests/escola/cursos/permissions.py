from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    """
    O método que deve ser sobrescrito é o has_permission
    recebe uma requisição, e a view que está sendo trabalhada

    """
    def has_permission(self, request, view):
        # se o método vindo no request for 'DELETE'
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True
    """
    Com essa verificação, caso o método seja DELETE, só será possível deletar se for super usuário.
    Caso não, não poderá deletar. Se o método não for DELETE, o usuário poderá realizar os outros 
    métodos. A verificação só é feita para o método DELETE.
    """
