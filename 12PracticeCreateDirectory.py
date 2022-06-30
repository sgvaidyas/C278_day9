# Python program to explain os.mkdir() method
# importing os module
import os
# Directory
directory = "IMHERE2"
# Parent Directory path
parent_dir = r"D:\US_278\day9"
# Path
path = os.path.join(parent_dir, directory)
# Create the directory
# 'IMHERE' in
# 'D:\US_278\day9'
os.mkdir(path)
print("Directory '% s' created" % directory)


