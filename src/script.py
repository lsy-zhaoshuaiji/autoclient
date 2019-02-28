from lib.conf.config import settings
from src.cilent import Agent,SSHSALT,Base
def run():
    if settings.MODE=='AGENT':
        obj=Agent()
    else:
        obj=SSHSALT()
    obj.execute()
if __name__ == '__main__':
    run()