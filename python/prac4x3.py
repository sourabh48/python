i = -1
for x in range (4,0,-1):
    i= i+1
    for z in range (0,i):
        print(' ',end =' ')
    for y in range (0,x):
        print('*',end= ' ')
    for y in range (0,x):
        print('@',end= ' ')

    print()           

