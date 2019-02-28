USER='ABC'
AA='BB'
import os,sys
from src.files import ret,git_ret
BASIC_DIRS=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASIC_DIRS)

HOSTNAME=None
MODE='AGENT'
PORT=22
USERNAME='root'
PASSWORD='root'
DEBUG=False
PLUGINS_DICT= ret
print(git_ret)#git_ret为更新gitlab的结果
API='http://171.8.71.18:8404/api/asset.html'
CERT_PATH=os.path.join(BASIC_DIRS,'config','cert')
OPENKEY='FSADFSDAFSD'
DATA_KEY='dfdsdfsasdfdsdfs'
