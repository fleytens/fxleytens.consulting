import os
import shutil

# folder path
dir_path = r'/home/fxleytens/GITPerso/fxleytens.consulting/CoresoETL/UCT_Source/'
processed_path = r'/home/fxleytens/GITPerso/fxleytens.consulting/CoresoETL/UCT_Processed/'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

for uctFile in res:
    shutil.move(dir_path + uctFile, processed_path)
    print(uctFile)