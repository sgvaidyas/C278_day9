
"""
0: sets the reference point at the beginning of the file

1: sets the reference point at the current file position

2: sets the reference point at the end of the file
"""
# Opening "GfG.txt" text file
import os
f = open("abc", "r")

# Second parameter is by default 0
# sets Reference point to twentieth
# index position from the beginning
f.seek(0, os.SEEK_END)              # seek to end of file; f.seek(0, 2) is legal
f.seek(f.tell() -30, os.SEEK_SET)   # go backwards 3 bytes
print("Current cursor after f.seek(f.tell() -30, os.SEEK_SET)  = " , f.tell())
print(f.read())
f.close()
