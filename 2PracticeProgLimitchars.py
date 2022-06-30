fp = open("file1","r")

content = fp.read(10)

print("Content in uppercase")
print(content.upper())
fp.close()
