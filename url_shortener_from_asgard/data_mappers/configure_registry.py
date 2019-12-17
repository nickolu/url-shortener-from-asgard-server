from __future__ import absolute_import, unicode_literals

import logging

from .url_pair_data_mapper import UrlPairMongoDbDataMapper
from .user_data_mapper import UserMongoDbDataMapper
from .data_mapper_registry import DataMapperRegistry
from .available_words_for_source_data_mapper import (
    AvailableWordsForSourceMongoDbDataMapper,
)
from ..entities.available_words_for_source import AvailableWordsForSource
from ..entities.url_pair import UrlPair
from ..entities.user import User

logger = logging.getLogger(__name__)


def configure_data_mapper_registry():
    logger.debug("Configuring data mapper registry")

    DataMapperRegistry.register(
        AvailableWordsForSource, AvailableWordsForSourceMongoDbDataMapper()
    )
    DataMapperRegistry.register(UrlPair, UrlPairMongoDbDataMapper())
    DataMapperRegistry.register(User, UserMongoDbDataMapper())
