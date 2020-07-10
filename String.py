# chapter 1.7 字符串
def strTest():
    list1 = [1, 3, 5, 7, 100]
    # 通过循环用下标遍历列表元素
    for index in range(len(list1)):
        print(list1[index])
    # 通过for循环遍历列表元素
    for elem in list1:
        print(elem)
    # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
    for index, elem in enumerate(list1):
        print(index, elem)
    # 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
    if 3 in list1:
        list1.remove(3)
    print(list1)  # [1, 400, 5, 7, 100, 200, 1000, 2000]
    # 从指定的位置删除元素
    list1.pop(0)
    print(list1)
    # 清空列表元素
    list1.clear()
    print(list1)  # []
    # 字符串
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)  # apple strawberry waxberry
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
    fruits4 = fruits[-3:-1]
    print(fruits4)  # ['pitaya', 'pear']
    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)  # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
    f = [x for x in range(1, 10)]
    print(f)


if __name__ == '__main__':
    strTest()
