from input import *
from command_factory import *

command = CommandFactory.create(parse_args())
output = command.execute()
print(output)
