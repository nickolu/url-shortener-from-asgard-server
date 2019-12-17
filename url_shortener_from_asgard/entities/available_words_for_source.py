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


class AvailableWordsForSource(BaseEntity):

    field_mapping = {
        "source": "source",
        "available_words_for_source": "available_words_for_source",
    }

    @property
    def get_random_available_word(self):
        return get_random_available_word(self._document["source"])

