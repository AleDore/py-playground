from utils.database import db
from dataclasses import dataclass


@dataclass
class User(db.Model):
    id: int
    firstname: str
    lastname: str
    email: str

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, userData) -> None:
        super().__init__()
        self.firstname = userData["firstname"]
        self.lastname = userData["lastname"]
        self.email = userData["email"]
