import sys,os
sys.path.append(os.path.join(os.getcwd(), "Command"))
from input import *
from command_factory import *

command = CommandFactory.create(parse_args())
if command is not None:
   output = command.execute()
   print(output)
