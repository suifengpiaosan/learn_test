
def sayhi():
    pass

info={
    'name':'rui',
    'age':22,
    'func':32,

}
f = open("testjson.text","wb")
import json
import pickle
#f.write(pickle.dumps(info))
pickle.dumps(info,"testjson.text")
f.close()
