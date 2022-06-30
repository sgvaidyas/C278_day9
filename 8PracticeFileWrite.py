try:
    #creates the file if it doesnt exist
    #throws error if it exists
    f = open("fil2_write4.txt", "x")
except:
    print("File already exist")
else:
    print("File got created")
    f.close()
# after running this script, check that the file was created. 
