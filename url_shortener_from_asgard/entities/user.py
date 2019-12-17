import json

from bson import ObjectId

from url_shortener_from_asgard.data_mappers.data_mapper_registry import (
    DataMapperRegistry,
)
from url_shortener_from_asgard.entities.base import BaseEntity


def get_user_by_id(user_id):
    user_data_mapper = DataMapperRegistry.get(User)
    document = user_data_mapper.get_by_id(user_id)

    if document:
        return User(document)

    return None


def insert_user(user):
    user_data_mapper = DataMapperRegistry.get(User)
    document = user_data_mapper.create_user(user)


class User(BaseEntity):
    field_mapping = {"name": "name"}

    @staticmethod
    def create_new():
        user = User()
        insert_user(user)

        return user

    @staticmethod
    def get_by_id(user_id):

        user = get_user_by_id(str(user_id))

        return user

    @property
    def id(self):
        user_id = self._document["_id"]

        return str(user_id)
