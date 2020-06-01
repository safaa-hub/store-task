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
