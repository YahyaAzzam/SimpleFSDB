import functions
import input

args = parse_args()
if args.command == "create_dir":
    creates_dir(args.schema)
    exit()
elif args.command == "create":
    creates(args.schema, args.table, args.primary_key)
    exit()
elif args.command == "set":
    sets(args.database, args.table, args.primary_key, args.parameter, args.value)
    exit()
elif args.command == "get":
    m = gets(args.database, args.table, args.primary_key)
    if not m:
        print("Error, data not found")
    else:
        print(m)
    exit()
elif args.command == "delete":
    m = deletes(args.database, args.table, args.primary_key)
    if not m:
        print("Error, data not found")
    exit()


os.system("main.py -c  -sc Check-in-schema.json -db csed25 -t Seats -pk "+str(1)+".json")

