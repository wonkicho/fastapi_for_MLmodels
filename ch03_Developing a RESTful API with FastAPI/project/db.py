from typing import Dict

from project.models.user import User
from project.models.post import Post


class DummyDatabase:
    users: Dict[int, User] = {}
    posts: Dict[int, Post] = {}


db = DummyDatabase()