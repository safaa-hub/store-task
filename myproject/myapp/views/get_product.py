from django.http import Http404
from rest_framework import status
from ..repositories.product_repository import ProductRepository
from rest_framework.response import Response
from rest_framework import viewsets
from ..utils import NotLoggedIn, BadRequest

product_repository = ProductRepository()


class GetProduct(viewsets.ViewSet):
    def retrieve(self, request, pk):
        if pk:
            if request.session['user_id'] is not None:
                product = product_repository.get_product(pk)
                if product is None:
                    raise Http404
                else:
                    return Response(product, status=status.HTTP_200_OK)
            else:
                raise NotLoggedIn
        else:
            raise BadRequest
