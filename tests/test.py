from test_create import *
from test_set import *
from test_delete import *
from test_get import *
from test_clear import *


DATABASE_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'storage')
if os.path.exists(DATABASE_PATH):
    shutil.rmtree(DATABASE_PATH)
