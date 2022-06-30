def printCharFromFile(filename,num):
    try:
        fp = open(filename,"r")
    except IOError:
        print("File cannot be opened")
    else:
        print("Content in uppercase")
        for i in range(num):
            content = fp.readline()
            print(content.upper(),end="")
        fp.close()

filename = input("Enter the filename = ")
numLines = int(input("Enterthe number of lines"))
printCharFromFile(filename,numLines)
