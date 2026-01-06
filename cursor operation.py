f = open("file.txt","w+")
f.write("Hello")
print(f.tell())  
f.close()  # cursor position
