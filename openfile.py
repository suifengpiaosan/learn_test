# #-*-coding:utf-8-*-
# f = open("情已逝","r",encoding="utf-8")
# f_new = open("newqingyishi","a",encoding="utf-8")
# for line in f:
#     f_new.write(line)
#     print(line.strip())
# f.close()
# f_new.close()
# num = 90
# with open("newqingyishi","r",encoding="utf-8") as se:
#     for line in se:
#         print(line)
# import sys
# print(sys.getdefaultencoding())
# def test(x):
#     "the test function"
#     x+=1
#     return x
# print(test.__doc__)
# print("%s hi"%numd
def add(**kwargs):
    print(kwargs)
    print(kwargs['name'])
add(name = 'hr',age=8)
