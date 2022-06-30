def printCharFromFile(filename):
    try:
        fp = open(filename,"r")
    except IOError:
        print("File cannot be opened")
    else:
        print("Content in uppercase")
        for line in fp: # the file object can be iterated on at the line level.
            print(line) # with each iteration, line contains the current line.
        print("============ ",fp.read()) #returns nothing
        fp.close()

filename = input("Enter the filename = ")
printCharFromFile(filename)

