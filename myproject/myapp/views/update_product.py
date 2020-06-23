from rest_framework import status
from ..repositories.product_repository import ProductRepository
from rest_framework.response import Response
from rest_framework import viewsets
from ..utils import NoContent, NotLoggedIn

product_repository = ProductRepository()


class UpdateProduct(viewsets.ViewSet):
    def update(self, request, pk):
        global status_, quantity, price, name, detail
        if request.session['user_id'] is not None:
            if request.data:
                if request.data.get('name') is not None:
                    name = request.data.get('name')
                if request.data.get('price') is not None:
                    price = request.data.get('price')
                if request.data.get('quantity') is not None:
                    quantity = request.data.get('quantity')
                if request.data.get('status') is not None:
                    status_ = request.data.get('status')
                if request.data.get('detail') is not None:
                    detail = request.data.get('detail')

                product_repository.update_product(pk, name, price, quantity, status_, detail)
                return Response("updated Successfully", status=status.HTTP_200_OK)
            else:
                raise NoContent
        else:
            raise NotLoggedIn
