# f = open("operation.py", "r") 
#print(f.read())               
#f.close()


#f = open("operation.py", "r")
#line1 = f.readline()  
#print(line1)
#line2 = f.readline()  
#print(line2)
#f.close()
               
'''f = open("operation.py", "r")
lines = f.readlines()  
print(lines)           
f.close()'''


'''f = open("operation.py", "r")
data = f.read()
f.close()
words = data.split()
for w in words:
    print(w)'''


'''f = open("operation.py", "r")
data = f.read()
f.close()
words = data.split()
for w in words:
    for ch in w:
        if ch.isalnum():
            print(ch, end="")
    print()'''

