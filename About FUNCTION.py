# default argument has a default value .ti will use in the absence of passing velue ayt the time of calling 
# # Ex= 
# def fun(x=10,y=30):
#     c=x+y
#     print(c)
# # fun(98,9) 
# fun()



# Keyword arguments is used to pass the value with name of variable so that we can pass values without bothering the sequence of parameters.
# # Ex=
# def fun(x,y):
#     c=x+y
#     print(c)
# fun(x=87,y=90)
# fun(y=40,x=30)


# Length arguments-
# In this we can pass arguments in different number of arguments in different function call.it will handle all the arguments using painter.
# ex=
# def fun(*x):
#     print(x)
# fun(1,2,4)
# fun()
# fun(5,7)

# def fun(*x):
#     for i in x:
#         print(i)
# fun(1,2,3,4)
# fun(4,5)
# fun("vikas","rahul")


# Keyword variable length arguments
def add(**num):
    k=num["a"]+num["b"]+num["c"]
    print(k)
add (a=5,b=2,c=4)    