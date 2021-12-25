n=int(input())
q=int(input())
full_list=[]
for i in range(n):
    x=int(input())
    full_list.append(x)
for j in range(q):
    k=int(input())
    l=int(input())
    a=int(input())
    b=int(input())
sub_list=full_list[k:l]
sum=sub_list.count(a)
for c in range(a+1,b+1):
    sum^=sub_list.count(c)
print(sum)

