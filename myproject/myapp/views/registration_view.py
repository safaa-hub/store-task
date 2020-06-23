from rest_framework import status
from ..repositories.user_repository import UserRepository
from rest_framework.response import Response
from rest_framework import viewsets
from ..utils import InvalidEmail, NoContent
from ..decorators.data_type import check_type

user_repository = UserRepository()


class RegisterViewSet(viewsets.ViewSet):
    @check_type
    def create(self, request):
        data = request.data
        if data:
            name = request.data.get('name')
            email = request.data.get('email')
            password = request.data.get('password')
            type_ = request.data.get('type')
            if user_repository.get_user_by_email(email) is None:
                user_repository.create_user(name, email, password, type_)
                return Response("Created", status=status.HTTP_201_CREATED)
            else:
                raise InvalidEmail
        else:
            raise NoContent
