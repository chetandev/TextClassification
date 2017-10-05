import logging

class AppFilter(logging.Filter):

    def filter(self, record):
        try:
            record.userid = record.userid
        except Exception as e:
            record.userid = ""
        try:
            record.devicekey = record.devicekey
        except Exception:
            record.devicekey = ""
        try:
            record.hash = record.hash
        except Exception:
            record.hash = ""

        return True


logger = logging.getLogger('__logger__')
logger.setLevel(logging.INFO)
logger.addFilter(AppFilter())

fh = logging.FileHandler(filename='text-classification.log')
fh.setLevel(logging.INFO)


formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(userid)s] [%(devicekey)s] [%(hash)s] [%(message)s] ',datefmt='%d-%m-%Y %I:%M:%S')
fh.setFormatter(formatter)
logger.addHandler(fh)



