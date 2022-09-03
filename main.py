from commands_and_adaptors.input import *
from commands_and_adaptors.command_factory import *
from commands_and_adaptors.parser_adaptor import *
from commands_and_adaptors.output_message import *


try:
    input_adaptor = ParsedInput(parse_args())
    command = CommandFactory(input_adaptor).create()
    output_message = command.execute()
    output_object = OutputMessage.success(output_message, str(command)[1])
except Exception as e:
    error = str(e.__class__)
    output_object = OutputMessage.fail(error[15:len(error)-2])
