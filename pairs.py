n=int(input())
res=[]
for i in range(n):
    a=int(input())
    b=int(input())
    if a%b==0:
        res.append("YES")
    else:
        res.append("NO")
print("\n".join(res))

