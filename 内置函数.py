# (lambda n:print(n))(5)
calc = lambda n:print(n)
calc(5)
res = map(lambda n:n*2,range(10))
for i in res:
    print(i)

info={
    'name':'rui',
    'age':22

}

f = open("testjson.text","w")

# f.write(str(info))
# f.close()



data=eval(f.read())
f.close()
print(data['age'])
