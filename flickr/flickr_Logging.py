"""Logging tool"""
import logging
import sys


def configure_logging():
    """Configure the loggers"""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname).1s %(name)-10s %(message)s',
        datefmt='%y%m%d%H%M%S',
        stream=sys.stdout
    )
    for logger in ('urllib3', 'requests_oauthlib', 'oauthlib'):
        logging.getLogger(logger).setLevel(logging.INFO)


def get_logger(name):
    """Get a logger"""
    configure_logging()
    return logging.getLogger(name)


if __name__ == '__main__':
    get_logger('test').debug('hello')
