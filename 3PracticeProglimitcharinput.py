def printCharFromFile(filename,num):
    try:
        fp = open(filename,"r")
    except IOError:
        print("File cannot be opened")
    else:
        content = fp.read(num)
        print("Content in uppercase")
        print(content.upper())
        fp.close()

filename = input("Enter the filename = ")
numChars = int(input("Enterthe number of chars"))
printCharFromFile(filename,numChars)
