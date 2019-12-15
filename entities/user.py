from .base import BaseEntity


class User(BaseEntity):
    field_mapping = {"name": "name"}

    def __init__(self):
        pass

    @staticmethod
    def create_new(name):
        user = User()

        return user
