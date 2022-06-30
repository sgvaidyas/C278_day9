import os
import time
fp = open("test_file.txt","w")
fp.close()
time.sleep(5)

os.remove("test_file.txt") #we are deleting the file from the previous example.
print("The file test_file.txt deleted successfully.")


