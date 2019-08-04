# 输入一个数判断是不是素数
num = int(input("大于1的数"))
if num > 1:
    for i in range(2,num):
        if num%i == 0:
            print (num,"不是质数")
            break
    else:
        print (num,"是质数")

