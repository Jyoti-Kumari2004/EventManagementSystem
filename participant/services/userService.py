from models.user import User
from repos.userRepo import UserRepo


class UserService:
    userRepo: UserRepo

    def __init__(self, userRepo: UserRepo):
        self.userRepo = userRepo

    def getbyid(self, id) -> User:
        return self.userRepo.get(id)

    def createUser(self, User):
        self.userRepo.createUser(User)

    def updateUser(self, id, user):
        return self.userRepo.updateUser(id, user)

    def deleteUser(self, id):
        return self.userRepo.deleteit(id)
