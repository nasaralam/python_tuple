t=(('a',21),('b',37),('c',11),('d',29))
first = 0   
last = len(t)   
for k in range(0, last):   
    for l in range(0, last-k-1):   
        if (t[l][first] > t[l + 1][first]):   
            new_item = t[l]   
            t[l]= t[l + 1]   
            t[l + 1]= new_item   
print(t) 
