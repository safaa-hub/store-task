from rest_framework import status
from ..repositories.user_repository import UserRepository
from rest_framework.response import Response
from rest_framework import viewsets
from ..utils import InvalidEmail, IncorrectPassword, NoContent


user_repository = UserRepository()


class LoginView(viewsets.ViewSet):
    def create(self, request):
        data = request.data
        if data:
            email = request.data.get("email")
            password = request.data.get("password")
            user = user_repository.get_user_by_email(email)
            if user is None:
                raise InvalidEmail
            else:
                if user.password == password:
                    request.session['user_id'] = user.id
                    request.session['user_type'] = user.type
                    return Response("logged in Successfully", status=status.HTTP_200_OK)
                else:
                    raise IncorrectPassword
        else:
            raise NoContent
