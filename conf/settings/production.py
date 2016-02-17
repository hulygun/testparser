from conf.settings.common import *

DEBUG = False
ALLOWED_HOSTS = ['*']

'''
    For safety reasons, it is recommended to make STATIC_ROOT and MEDIA_ROOT outside the  project. eg
    STATIC_ROOT = os.path.join(PROJECT_ROOT, '..', 'public', 'static')
    MEDIA_ROOT = os.path.join(PROJECT_ROOT, '..', 'public', 'media')
'''