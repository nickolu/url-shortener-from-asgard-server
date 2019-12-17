import logging

from url_shortener_from_asgard.data_mappers.url_pair_data_mapper import (
    UrlPairMongoDbDataMapper,
)
from url_shortener_from_asgard.data_mappers.user_data_mapper import (
    UserMongoDbDataMapper,
)
from url_shortener_from_asgard.data_mappers.data_mapper_registry import (
    DataMapperRegistry,
)
from url_shortener_from_asgard.data_mappers.available_words_for_source_data_mapper import (
    AvailableWordsForSourceMongoDbDataMapper,
)
from url_shortener_from_asgard.entities.available_words_for_source import (
    AvailableWordsForSource,
)
from url_shortener_from_asgard.entities.url_pair import UrlPair
from url_shortener_from_asgard.entities.user import User

logger = logging.getLogger(__name__)


def configure_data_mapper_registry():
    logger.debug("Configuring data mapper registry")

    DataMapperRegistry.register(
        AvailableWordsForSource, AvailableWordsForSourceMongoDbDataMapper()
    )
    DataMapperRegistry.register(UrlPair, UrlPairMongoDbDataMapper())
    DataMapperRegistry.register(User, UserMongoDbDataMapper())
