from ..utils import InvalidName, InvalidPassword, InvalidUserType


def check_type(function):
    def inner(request, *args, **kwargs):
        request = request.request
        type_ = request.data.get('type')
        if not isinstance(request.data.get("name"), str):
            raise InvalidName
        elif not (str(type_) == str('seller')) and not (str(type_) == 'customer'):
            raise InvalidUserType
        elif not isinstance(request.data.get("password"), str):
            raise InvalidPassword
        else:
            return function(request, *args, **kwargs)

    return inner
