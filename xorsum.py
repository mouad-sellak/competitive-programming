n=int(input())
result=[]
for i in range(n):
    d=int(input())
    s1=input()
    s2=input()
    count1=0
    count2=0
    for i in range(d):
        if s1[i] != s2[i]:
            count1+=1
        elif s1[i]==1 and s2[i]==1:
            count2+=1
    if count1==d:
        result.append("YES")
    elif count2==1:
        result.append("YSE")
    else:
        result.append("NO")
print("\n".join(result))
