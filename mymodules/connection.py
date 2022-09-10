from pymongo import MongoClient


class Connection:

    def __init__(self, db_name, collection_name, url_initial):
        self.__db_name = db_name
        self.__collection_name = collection_name
        self.__url_initial = url_initial

        self.__collection = None
        self.__database = None

    def open(self):
        self.__init_client()
        self.__database = self.__client[self.__db_name]
        self.__collection = self.__database[self.__collection_name]

    def close(self):
        self.__client.close()
        self.__reset()

    def insert_one(self, record, id_key=''):
        if not isinstance(record, dict):
            raise TypeError('record is not a dictionary')

        if id_key and not id_key.isspace():
            record = self.__set_id(record, id_key)

        try:
            i = self.__collection.insert_one(record)
            return i.inserted_id
        except Exception as e:
            raise e.__context__

    def exist_one(self, key, value):
        if self.__collection.count_documents({key: value}, limit=1) != 0:
            return True
        else:
            return False

    def __reset(self):
        self.__client = None
        self.__collection = None
        self.__database = None

    def __init_client(self):
        if self.__url_initial == 'review':
            self.__client = MongoClient(
                "mongodb+srv://[user_name]:review@cluster.[password].mongodb.net/?retryWrites=true&w=majority")
        elif self.__url_initial == 'user':
            self.__client = MongoClient(
                "mongodb+srv://[user_name]:user@cluster.[password].mongodb.net/?retryWrites=true&w=majority")
        elif self.__url_initial == 'business':
            self.__client = MongoClient(
                "mongodb+srv://[user_name]:business@cluster.[password].mongodb.net/?retryWrites=true&w=majority")
        else:
            raise ValueError('wrong collection name given')

    @classmethod
    def __set_id(cls, record, id_key):
        try:
            record['_id'] = record[id_key]
        except KeyError as error:
            raise error.__context__

        return record
