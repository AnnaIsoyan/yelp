import logging
import os
from os.path import exists


class Log:
    def __init__(self, path, file_name):
        self.__validate_path(path)
        logging.basicConfig(filename=path+'/'+file_name+'.log', encoding='utf-8', level=logging.DEBUG,
                            format='%(asctime)s %(message)s',
                            filemode='a')
        self.__logger = logging.getLogger()

    def write_debug(self, message):
        self.__logger.debug(message)

    @classmethod
    def __validate_path(cls, path):
        if not exists(path):
            raise ValueError("Wrong file path given")
        if not os.path.isdir(path):
            raise ValueError("there is no a folder by given path")
