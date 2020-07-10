import random

'''
chapter 1.3 分支结构
'''
if False:
    value = float(input('请输入长度：'))
    unit = input('请输入单位：')
    if unit == 'in' or unit == '英寸':
        print('%f英寸 = %f厘米' % (value, value * 2.54))
    else:
        print("finish")

# chapter 1.4 循环结构
elif False:
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

# chapter 1.5
elif False:
    print("hello 1.5")
    print("%f" % (11 // 10))
    # 正整数的反转
    num = int(input('num = '))
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    print(reversed_num)
    # 《百钱百鸡》问题
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if x * 5 + y * 3 + z / 3 == 100:
                print("公鸡 %d 母鸡 %d 小鸡 %d" % (x, y, z))


# chapter 1.6 函数的模块与使用
def main():
    # Todo: Add your code here
    print("hello new world!")
    pass


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


if __name__ == '__main__':
    main()
    strTest()
    for val in fib(20):
        print(val)
