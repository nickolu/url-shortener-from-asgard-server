import copy


class DataMapper(object):
    def get_next_id(self):
        pass

    def insert(self, entity):
        pass

    def find_by_id(self, id_):
        pass

    def update(self, entity):
        pass

    def delete(self, entity):
        pass

    def _create_copy_of_entity(self, entity):
        return copy.deepcopy(entity)
