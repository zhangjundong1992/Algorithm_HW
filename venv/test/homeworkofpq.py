def isNum(str):
    try:    #增加代码健壮性，处理异常的字符串输入
        res = eval(str)
        if type(res) == int or type(res) == float or type(res) == complex:
            print('True')
        else:
            print('False')
    except:
        print('False')


isNum('123')
isNum('12.work3')
isNum('1+2j')
isNum('丫儿嘞')
isNum('"西财最美程序媛"')


def isNum2(str):
    try:
        res = eval(str)
        print('true')
    except NameError:
        print('false')


def isNum3(str):
    # 判断是不是整数
    try:
        res = int(str)
        print('True')
        return
    except ValueError:
        pass

    # 判断是不是浮点数
    try:
        res = float(str)
        print('True')
        return
    except ValueError:
        pass

    # 判断是不是复数
    try:
        res = complex(str)
        print('True')
        return
    except ValueError:
        pass

    print('False')

# isNum2('123')
# isNum2('1.23')
# isNum2('1+2j')
# isNum2("彭勤是瓜皮")
# print('------------')
# isNum3('123')
# isNum3('1.23')
# isNum3('1+2j')
# isNum3("彭勤是瓜皮")
