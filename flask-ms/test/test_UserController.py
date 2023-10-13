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
    def test_userCreateTest(self):
        dbSession = MagicMock()
        dbSession.query.return_value.filter_by.return_value.count.return_value = 0
        uc = UserController(dbSession)
        code, _ = uc.createUser(fakeUserData())
        self.assertEqual(code, 200)

    def test_userCreateTestWithAlreadyExistingConflict(self):
        dbSession = MagicMock()
        dbSession.query.return_value.filter_by.return_value.count.return_value = 1
        uc = UserController(dbSession)
        code, _ = uc.createUser(fakeUserData())
        self.assertEqual(code, 409)


if __name__ == "__main__":
    unittest.main()
