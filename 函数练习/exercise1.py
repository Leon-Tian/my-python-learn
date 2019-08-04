# 递归实现： fabonaci数列（1,1,2,3,5,8,13...）
n = int(input("第几项"))

def f(n):    
    if  1<= n <=2 :
        return 1
    else:
        return f(n-1) + f(n-2)

print (f(n))