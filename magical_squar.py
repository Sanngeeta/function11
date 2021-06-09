def magic_squar(magic):

    i=0
    s=0
    while i<len(magic):
        col=0
        while col<len(magic):
            s=s+magic[i][col]  
            col=col+1
        j=0
        s1=0
        while j<len(magic):
            row=0
            while row<len(magic):
                s1=s1+magic[i][row]
                row=row+1
            j=j+1   
            k=0
            s2=0
            while k<len(magic):
                dig=0
                while dig<len(magic):
                    s2=s2+magic[i][dig]
                    dig=dig+1
                k=k+1
        i=i+1        
    print(s1) 
    print(s)   
    print(s2) 
    if s==s1==s2:
        print("its magical squar")
    else:
        print("its not magical squar ")    


a = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
] 
magic_squar(a)
  



















