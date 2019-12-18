from url_shortener_from_asgard.entities.base import BaseEntity
from url_shortener_from_asgard.data_mappers.data_mapper_registry import (
    DataMapperRegistry,
)


def get_random_available_word(source):
    available_words_for_source_data_mapper = DataMapperRegistry.get(
        AvailableWordsForSource
    )
    return available_words_for_source_data_mapper.get_random_available_word_from_source(
        source
    )


def get_random_available_asgardian_word():
    available_words_for_source_data_mapper = DataMapperRegistry.get(
        AvailableWordsForSource
    )

    return available_words_for_source_data_mapper.get_random_available_asgardian_word()


def get_remaining_available_words_count(source):
    available_words_for_source_data_mapper = DataMapperRegistry.get(
        AvailableWordsForSource
    )

    return available_words_for_source_data_mapper.get_available_words_count()


class AvailableWordsForSource(BaseEntity):

    field_mapping = {
        "source": "source",
        "available_words_for_source": "available_words_for_source",
    }

    @staticmethod
    def get_random_available_asgardian_word():
        return get_random_available_asgardian_word()

    @staticmethod
    def get_remaining_asgardian_words_count():
        return get_remaining_available_words_count("asgard")

