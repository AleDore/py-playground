from model.UserModel import User


class UserController:
    def __init__(self, dbSession) -> None:
        self.session = dbSession
        pass

    def createUser(self, userData):
        newUser = User(userData)
        findRes = self.session.query(User).filter_by(email=newUser.email).count()
        if findRes == 0:
            self.session.add(newUser)
            self.session.commit()
            return 200, newUser
        else:
            return 409, newUser

    def getUser(self, userId: int):
        findRes = self.session.get(User, userId)
        if findRes:
            return 200, findRes
        else:
            return 404, None

    def getUsers(self):
        results = self.session.query(User).all()
        return 200, results
