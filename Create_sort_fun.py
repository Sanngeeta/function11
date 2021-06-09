# sort function without using sort function

a=[6,33,23,12,4,7,10,11,5,77,24,1,56,87,32,2]
i=0
y=[]
while i<len(a):
    k=min(a)
    a.remove(k)
    y.append(k)
print(y)    

