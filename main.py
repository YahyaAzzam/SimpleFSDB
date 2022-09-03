from CommandsAndAdaptors.input import *
from CommandsAndAdaptors.command_factory import *
from CommandsAndAdaptors.parser_adaptor import *

try:
    input_array = ParsedInput(parse_args())
    command = CommandFactory(input_array).create()
    output_message = command.execute()
except NoParameterError:
    pass
