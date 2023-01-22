import logging

log_format = "%(asctime)s::%(levelname)s::%(name)s::%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(level = logging.INFO, format=log_format)
log = logging.getLogger(__name__)

def main():
   log.info("main(): Template Project in Python")

if __name__ == '__main__':
   main()