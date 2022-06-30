def printCharFromFile(filename):
    try:
        fp = open(filename,"r")
    except IOError:
        print("File cannot be opened")
    else:
        print("Content starting with I")
        for line in fp.readlines(): # the file object can be iterated on at the line level.
            if(line.startswith("I")):
                print(line) # line starts with f
        fp.close()

filename = input("Enter the filename = ")
printCharFromFile(filename)

