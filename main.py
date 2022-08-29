from input import *
from command_factory import *

create = command_factory(parse_args())
create.execute()
