
f = open("abc", "rb")
f.seek(0,2)
print("End of file cursor = " ,f.tell())
#moved 20 chars from end of the filr
f.seek(-20, 2)
print("after f.seek(-20, 2)=", f.tell())
f.seek(-10, 1)
print("after f.seek(-10, 1)=", f.tell())
print(f.read().decode('utf-8'))

f.close()
