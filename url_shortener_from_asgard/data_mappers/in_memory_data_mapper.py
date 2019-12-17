from .data_mapper import DataMapper


class InMemoryDataMapper(DataMapper):
    def __init__(self):
        super(InMemoryDataMapper, self).__init__()
        self._data_store = {}

    @property
    def data_store(self):
        return self._data_store

    def get_next_id(self):
        next_id = self._current_id = self._current_id + 1
        return next_id

    def insert(self, entity):
        self._data_store[entity.id] = self._create_copy_of_entity(entity)

    def get_one_by_field_name(self, field_name, value):
        for item in self.data_store:
            if item[field_name] == value:
                return item

        return None

    def get_all_by_field_name(self, field_name, value):
        result = []

        for item in self.data_store:
            if item[field_name] == value:
                result.append(item)

        return result

    def update(self, entity):
        self._data_store[entity.id] = self._create_copy_of_entity(entity)
