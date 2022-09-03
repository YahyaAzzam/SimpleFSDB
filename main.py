from Commands_Adaptors.input import *
from Commands_Adaptors.command_factory import *
from Commands_Adaptors.parser_adaptor import *
from Commands_Adaptors.CommandStatus import *


input_array = parsed_input.parse(parse_args())
command = CommandFactory.create(input_array)
if command != 1 and command != 2:
    output_message = status(command.execute()).name
else:
    output_message = status(command).name
