from rest_framework import viewsets
from ..repositories.product_repository import ProductRepository
from rest_framework.response import Response
from rest_framework import status
from ..utils import NoContent, UnAuthorized

product_repository = ProductRepository()


class AddProduct(viewsets.ViewSet):
    def create(self, request):
        if request.data:
            if request.session['user_type'] == "seller":
                user_id = request.session['user_id']
                name = request.data.get("name")
                price = request.data.get("price")
                quantity = request.data.get("quantity")
                status_ = request.data.get("status")
                detail = request.data.get("detail")
                product_repository.add_product(name, price, quantity, status_, detail, user_id)
                return Response("product added successfully", status=status.HTTP_200_OK)
            else:
                raise UnAuthorized
        else:
            raise NoContent
