'''import json
data = {"name": "Alice", "age": 20, "marks": [85, 90]}
with open("data.json", "w") as f:
    json.dump(data,f,indent=4)'''
 
 
 
 
    
import json
with open("data.json", "r") as f:
    data = json.load(f) 
print(data)
    
