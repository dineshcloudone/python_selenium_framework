import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir) + '\\logs\\automation.log'
        logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler=logging.FileHandler(filename=path, mode='a', encoding=None, delay=False)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logging.getLogger().addHandler(file_handler)
        #logger.removeHandler(logging.StreamHandler())
        return logger


import pdb

# class LogGen():
#     @staticmethod
#     def loggen():
#
#         path = os.path.abspath(os.curdir) + '\\logs\\automation.log'
#         #path = r'C:\Python\Test_Project\logs\automation.log'
#         #logging.basicConfig(filename='C:\\Python\\Test_Project\\logs\\automation.log',
#         #                    format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#
#         #path = os.path.join(os.curdir,'automation.log')
#         pdb.set_trace()
#         logging.basicConfig(filename=path, encoding='utf-8',datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
#
#         logger = logging.getLogger()
#         #logger.setLevel(logging.ERROR)
#         #logger.removeHandler(logging.StreamHandler())
#         return logger

