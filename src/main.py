import sys
import os
sys.path.append(os.path.join(os.getcwd().replace("tests", ''), "src", "input_adaptors"))
sys.path.append(os.path.join(os.getcwd().replace("tests", ''), "src", "commands"))
sys.path.append(os.path.join(os.getcwd().replace("tests", ''), "src", "output"))
from input import *
from command_factory import *
from parser_adaptor import *
from output_message import *


try:
    input_adaptor = ParsedInput(parse_args())
    command = CommandFactory(input_adaptor).create()
    result = command.execute()
    output_object = OutputMessage(command_name=input_adaptor.command, result=result)
except Exception as e:
    output_object = OutputMessage(exception=e)

print(json.dumps(output_object.__dict__))
