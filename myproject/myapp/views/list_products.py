from rest_framework import status
from ..repositories.product_repository import ProductRepository
from rest_framework.response import Response
from rest_framework import viewsets
from ..utils import NotLoggedIn

product_repository = ProductRepository()


class ListProducts(viewsets.ViewSet):
    def list(self, request):
        if request.session['user_id'] is not None:
            products = product_repository.get_all_products()
            return Response(products, status=status.HTTP_200_OK)
        else:
            return NotLoggedIn
