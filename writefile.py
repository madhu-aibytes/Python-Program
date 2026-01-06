#Always close the file 
'''f = open("file.txt", "w")
f.write("Hello! This is a write operation.\n")
f.write("This will overwrite existing content if file exists.\n")
f.close()'''# overwrite mode


'''with open("file.txt", "w") as f:
   f.write("Writing using with-statement.\n")
   f.write("No need to manually close the file.\n")'''#close automatically

'''f = open("file.txt", "w")
f.write("Line 1\n")
f.write("Line 2\n")                       
f.write("Line 3\n")
f.close()'''                               #write line is not available so this can be used


'''lines = ["First line\n", "Second line\n", "Third line\n"]
f = open("file.txt", "w")
f.writelines(lines)
f.close()'''# will not close the file automatically

'''f = open("file.txt", "w")
f.write("Hello! This is a write operation.\n")
f.write("This will overwrite existing content if file exists.\n")
print(f)
f.close()'''


f = open("file.txt", "w+")
f.write("Python")     # cursor moves to end (position 6)
print(f.tell())       # shows cursor position → 6
f.seek(0)             # move cursor to beginning
print(f.read())       # reads from start
f.close()



''' thses are the cursor function seek() -> to move the cursor to a particular position
                                  tell() -> to know the current position of cursor'''

