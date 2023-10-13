from typing import Any
from unittest.mock import MagicMock
import unittest
from controllers.UserController import UserController
from model.UserModel import User
from utils.database import db


def fakeUserData() -> Any:
    userData = {
        "id": 1,
        "email": "email",
        "firstname": "firstname",
        "lastname": "lastname",
    }
    return userData


class UserControllerTest(unittest.TestCase):
    def test_userCreateTestWithAlreadyExistingConflict(self):
        dbSession = MagicMock()
        uc = UserController(dbSession)
        dbSession.query(User).filter_by().count = MagicMock(returnValue=1)
        code, _ = uc.createUser(fakeUserData())
        self.assertEqual(code, 409)


if __name__ == "__main__":
    unittest.main()
