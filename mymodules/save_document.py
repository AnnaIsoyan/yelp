import os
from os.path import exists
import json
from mymodules import connection, log


class SaveDocument:

    def __init__(self, path, collection_list):
        self.__validate_path(path)
        self.__path = path
        self.__collection_list = collection_list

    def save(self):
        dir_list = os.listdir(self.__path)
        for file in dir_list:
            istrue, file_name, data = self.__get_data(file)

            if not istrue:
                continue

            collection_name = file_name.rsplit('_', 1)[-1]

            log_to_file = log.Log('var/log/', collection_name)
            conn = connection.Connection(collection_name, collection_name, collection_name)
            conn.open()

            for record in data:
                i = conn.insert_one(record, collection_name + '_id')
                log_to_file.write_debug(i)

            conn.close()

            print(f"finished inserting in {collection_name}")

    @classmethod
    def __validate_path(cls, path):
        if not exists(path):
            raise ValueError("Wrong file path given")
        if not os.path.isdir(path):
            raise ValueError("there is no a folder by given path")

    def __get_data(self, file):
        file_path = self.__path + '/' + file
        if not os.path.isfile(file_path):
            return False, '', []

        extracted = os.path.splitext(file)
        file_name = extracted[0]
        file_ext = extracted[1]

        if file_name.rsplit('_', 1)[-1] not in self.__collection_list:
            return False, '', []
        if not file_ext == '.json':
            return False, '', []

        data = []
        with open(file_path, encoding="utf8") as f:
            for line in f:
                data.append(json.loads(line))

        return True, file_name, data
