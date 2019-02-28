import os,importlib
from . import global_settings
class Settings(object):
    def __init__(self):
        for name in dir(global_settings):
            if name.isupper():
                value=getattr(global_settings,name)
                setattr(self,name,value)

        settings_module=os.environ.get('USER_SETTINGS')
        if not settings_module:
            return
        m=importlib.import_module(settings_module)
        for name in dir(m):
            if name.isupper():
                value=getattr(m,name)
                setattr(self,name,value)
settings=Settings()