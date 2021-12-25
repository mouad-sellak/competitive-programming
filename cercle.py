import math
n=int(input())
res=[]
for i in range(n):
    l=[]
    for i in range(6):
        x=int(input())
        l.append(x)
    x_ab=l[2]-l[0]
    y_ab=l[3]-l[1]
    x_ac=l[4]-l[0]
    y_ac=l[5]-l[1]
    n_ab=math.sqrt(x_ab**2+y_ab**2)
    n_ac=math.sqrt(x_ac**2+y_ac**2)
    if n_ab>n_ac:
        if n_ab%n_ac==0:
            res.append("Impossible")
        else:
            res.append("Possible")
    else:
        if n_ac%n_ab==0:
            res.append("Impossible")
        else:
            res.append("Possible")
print("\n".join(res))


    