import logging

logger = logging.getLogger('wordpicker')
logging.basicConfig(format='%(asctime)-15s %(message)s', filename='/var/log/wordpicker/log', level=logging.DEBUG)
