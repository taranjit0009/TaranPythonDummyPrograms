row = 5 #Numbers of row

for i in range (1,row+1):
    for j in range(i):
        print('*',end='')
    print()


for i in range(row-1,0,-1):
    for j in range(i):
        print('*',end='')
    print()


for i in range(1,row+1):
    for col in range(row-i):
        print(' ',end='')
    for col in range(2 * i -1):
        print('*',end='')
    print()

#Upper
for i in range(1,row+1):
    for col in range(row-i):
        print(' ',end='')
    for col in range(2 * i -1):
        print('*',end='')
    print()

#Lower
for i in range(row-1,0,-1):
    for j in range(row-i):
        print(" ",end='')
    for k in range(2*i-1):
        print('*',end='')
    print()



