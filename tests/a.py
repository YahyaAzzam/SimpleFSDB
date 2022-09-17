import os
for f in os.listdir(os.getcwd()):
    if ".json" in str(f):
        print(f)
