import os

optional_dev_tag = ''
if os.getenv('DEV_BUILD'):
    optional_dev_tag = '.dev' + os.getenv('DEV_BUILD')

__version__ = f'0.8.3{optional_dev_tag}'
