import os,sys
BASIC_DIRS=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASIC_DIRS)
from src import script
script.run()