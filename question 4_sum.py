def add_numbers(number1,number2):
    print(number1+number2)
add_numbers(56,12)       




def add_numbers(number1,number2):
    i=0
    sum=0
    while i<len(number1):
        a=0
        while a<len(number2):
            sum=number1[i]+number2[i]
            a=a+1
        
        print(sum)
        i=i+1
add_numbers([50,60,10],[10,20,13])   



































# def add_numbers(a,b):
#     return(a+b)
#     print(a+b)
#     # return 
# print(add_numbers(12,8))
