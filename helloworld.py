import random

'''
chapter 1.3 分支结构
'''
if False:
    value = float(input('请输入长度：'))
    unit = input('请输入单位：')
    if unit == 'in' or unit == '英寸':
        print('%f英寸 = %f厘米' % (value, value *2.54))
    else:
        print("finish")

# chapter 1.4 循环结构
else:
    print("hello 1.4")
    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        number = int(input('请输入：'))
        if number < answer:
            print('大一点')
        elif number > answer:
            print("小一点")
        else:
            print("猜对啦")
            break
    print("你共猜对了%d" % counter)






