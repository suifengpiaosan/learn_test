salary=input("请输入你的工资")
if salary.isdigit():
    salary=int(salary)
    shopinglist=[("iphone",5000),("tesla",30000),("hamburge",20),("xiaomi",1000)]
    print("你的余额:",salary)
    for i in shopinglist:
        print(shopinglist.index(i),i[0],i[1])
    # for index,item in enumerate(shopinglist):
    #     print(index,item)
    while True:
    choice = input("输入你要买的商品:")

    if choice.isdigit():
        choice=int(choice)

        choice_list=[]
        if choice >=0 and choice<len(shopinglist):
            item = shopinglist[choice]
            if salary>= item[1]:
                print("OK")
                choice_list.append(item)
            else:
                print("买不起")
        else:
            print("不存在")
    elif choice=="q":
        break
    else:
        print("非合法输入")

    print(choice_list)
else:
    print("非合法输入")