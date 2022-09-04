import json

from commands_and_adaptors.input import *
from commands_and_adaptors.command_factory import *
from commands_and_adaptors.parser_adaptor import *
from commands_and_adaptors.output_message import *


try:
    input_adaptor = ParsedInput(parse_args())
    command = CommandFactory(input_adaptor).create()
    result = command.execute()
    output_object = OutputMessage(command_name=input_adaptor.command, result=result)
except Exception as e:
    output_object = OutputMessage(command_name=input_adaptor.command, exception=e)

print(json.dumps(output_object.__dict__))
