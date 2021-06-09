 
# n = 10
# def a(n):
#     return n+4

# print (a(4) )   


# def sum1(n):
#     if (n==0):
#         return 0
#     return sum1(n-1) + n

# print (sum1(6) )


def febo_s(num):
    if num==1: 
        return[1,1]
    else:    
        a=febo_s(num-1)
        return [a[0]+a[1]]+a
print(febo_s(10))        

