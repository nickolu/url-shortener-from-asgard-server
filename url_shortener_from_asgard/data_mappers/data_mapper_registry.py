# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class DataMapperRegistry(object):
    """
    This singleton acts as the registry for all configured concrete data mappers.
    It maps entity classes to their appropriate concrete data mappers. Whenever
    a piece of code needs to interact with a data mapper, it should
    ask this registry for the concrete implementation to use. Concrete data
    mappers should be registered upon program start up.

    Example:

    # During program startup, add concrete data mappers
    DataMapperRegistry.register(Website, MongoDbWebsiteDataMapper)
    DataMapperRegistry.register(Person, MySqlPersonDataMapper)

    # Elsewhere in the codebase ...
    website_data_mapper = DataMapperRegistry.get(Website)
    website = website_data_mapper.find_by_url('http://www.example.com/')
    """

    _data_mappers = {}

    @classmethod
    def register(cls, entity_class, data_mapper):
        cls._data_mappers[entity_class] = data_mapper

    @classmethod
    def get(cls, entity_class):
        if entity_class not in cls._data_mappers:
            raise KeyError("Data mapper not found for {}".format(entity_class))

        return cls._data_mappers[entity_class]

    @classmethod
    def clear(cls):
        cls._data_mappers = {}
