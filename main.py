from CommandsAndAdaptors.input import *
from CommandsAndAdaptors.command_factory import *
from CommandsAndAdaptors.parser_adaptor import *

try:
    input_array = ParsedInput.parse(parse_args())
    command = CommandFactory(input_array).create()
    output_message = command.execute()
    status = 0
except NoCommandError:
    status = 1
except WrongCommandError:
    status = 2
except NoSchemaError:
    status = 3
except WrongSchemaError:
    status = 4
except NoDatabaseError:
    status = 5
except WrongDatabaseError:
    status = 6
except NoTableError:
    status = 7
except WrongTableError:
    status = 8
except NoPrimaryKeyError:
    status = 9
except WrongPrimaryKeyError:
    status = 10
except NoParameterError:
    status = 11
except WrongParameterError:
    status = 12
except NoValueError:
    status = 13
except WrongValueError:
    status = 14
