import json,pickle
f = open("testjson.text","rb")
data = pickle.loads(f.read())

print(data["func"])