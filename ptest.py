print()
print("**************** Starting ***************")
print()
import os, sys, shutil
srcPath = 'C:/Users/User/Documents'
dstPath = 'C:/Users/User/testcopy'

src = os.listdir(srcPath)
dst = os.listdir(dstPath)

# for file in src:
#     print(file)

for index, file in enumerate(src):
    print(index, file)

# Versions control is not a substitute for documentation

# need to make the whole backslash problem invisible
# Further comments

for file in srcset:
    if file in dstset:
        print(file, " Exists")
    else:
        print(file," does not exist")
        if os.path.isfile(file):
            print("file: ", file, " is a file")
            fullFileName = os.path.join(srcPath,file)
            print(file,"  ", fullFileName)
            print("Destination Path: ",dstPath)
            # shutil.copyfile(file,dstPath)
