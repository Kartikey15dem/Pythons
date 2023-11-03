
for i in range(1,5):
    p=''
    for j in range(1,8):
        if j>=i and j<=8-i:
            p=p+str(5-i)+' '
        elif j==i-1 or j==9-i:
            p=p+str(6-i)+' '
        elif j==i-2 or j==10-i:
            p=p+str(7-i)+' '
        else:
            p=p+'4'+' '
    print(p)
for i in range(3,0,-1):
    p=''
    for j in range(1,8):
        if j>=i and j<=8-i:
            p=p+str(5-i)+' '
        elif j==i-1 or j==9-i:
            p=p+str(6-i)+' '
        elif j==i-2 or j==10-i:
            p=p+str(7-i)+' '
        else:
            p=p+'4'+' '
    print(p)