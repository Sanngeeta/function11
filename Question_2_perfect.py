# def perfect(num):
#     i=1
#     sum=0
#     while i<num:
#         if num%i==0:
#             sum=sum+i
#             if num==sum:
#                 print("Perfact Number=",num)
#             else:
#                 print("Not perfact number",num)        

#         i=i+1        
# num1=int(input("enter your perfact number:"))
# perfect(num1)           

def perfact(a):
    i=1
    sum=0
    while i<=1000:
        if a%i==0:
            sum=sum+i
            if a==sum:
                print("Perfact",i)
            else:
                print("not perfact",i)  
        i=i+1
num1=int(input("enter the number"))           
perfact(num1)                
