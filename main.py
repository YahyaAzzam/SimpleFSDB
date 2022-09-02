from Command.input import *
from Command.command_factory import *

command = CommandFactory.create(parse_args())
if command is not None:
    output_message = command.execute()
    print(output_message)
