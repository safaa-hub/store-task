import hashlib
from ..constant_file import SALT
from ..models.user_model import User
from ..common_file import Session


class UserRepository:
    def get_user_by_email(self, email):
        user_ = Session.query(User).filter_by(email=email).all()
        #  print(user_)
        if len(user_) > 0:
            return user_[0]
        else:
            return None

    def create_user(self, name, email, password, type):
        encoded_password = hashlib.md5((str(password) + SALT).encode('utf-8')).hexdigest()
        user = User(name=name, email=email, password=encoded_password, type=type)

        Session.add(user)
        Session.commit()
        Session.close()
