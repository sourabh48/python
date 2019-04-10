i=3
for x in range (0,4,1):
    for z in range (0,i):
        print(' ',end =' ')
    for y in range (0,x):
        print('*   ',end= '')
    i=i-1        
    print()
i=i+2
for x in range (3,1,-1):
    for z in range (0,i):
        print(' ',end =' ')
    for y in range (x-1,0,-1):
        print('*   ',end= '')
    i=i+1        
    print()


     
