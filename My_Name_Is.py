

# num=input("enter the name:=")

# i=0
# while i<len(num):
#        i=i+1   
# print(num.title(),end="") 
               



def my_name(*a):
    k=" "
    i=1
    while i<len(a):
        k=k+a[-i]
        i=i+1
        print(k)
my_name("sangeeta","paswan")    


