import logging


logging.warning('This is a warning message')
logging.error('This is an error message')


getattr(logging, 'warning')('This is a warning message')
