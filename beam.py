import logging
import random
import time
import ConfigParser


Config = ConfigParser.RawConfigParser()
Config.read('beam.cfg')

# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


messages = ["hello", "test","woohoo","pizdabol"]


def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


loglevel = ConfigSectionMap("default")['loglevel']
print loglevel

while True:
  if loglevel == 'error':
    logger.error(messages[random.randint(0, 3)])
  else:
    logger.info(messages[random.randint(0, 3)])
  time.sleep(3)
