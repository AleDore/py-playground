from utils.database import db
from model.UserModel import User


class UserController:
    def __init__(self) -> None:
        pass

    def createUser(self, userData):
        newUser = User(userData)
        findRes = db.session().query(User).filter_by(email=newUser.email).count()
        if findRes == 0:
            db.session().add(newUser)
            db.session().commit()
            return 200, newUser
        else:
            return 409, newUser
