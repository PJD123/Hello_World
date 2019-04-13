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

srcset = set(src)
dstset = set(dst)
print("Converted to set")
print(srcset)


# Further comments
