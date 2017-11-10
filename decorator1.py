def foo():
    print('in the foo')
    bar()
foo()
def bar():
    print('in the bar')
calc = lambda x:x*3

print(calc(3))