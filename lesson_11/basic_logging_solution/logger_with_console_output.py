import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

logger.debug('Це повідомлення рівня DEBUG')
logger.info('Це повідомлення рівня INFO')
logger.warning('Це повідомлення рівня WARNING')
logger.error('Це повідомлення рівня ERROR')
logger.critical('Це повідомлення рівня CRITICAL')