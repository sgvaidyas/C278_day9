try:
    fp = open(r"C:\Users\sgvai\OneDrive\Desktop\abc.txt","r")
except:
    print("File cannot be opened")
else:
    content = fp.read()
    print("Content in uppercase")
    print(content.upper())
    fp.close()
