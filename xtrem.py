# a,b=input().split()
# if int(a)<int(b):
#     print(a+" "+b)   
# else:
#     print(b+" "+a)



# a,b=input().split()
# print(int(a)+int(b))   

# a=int(input())
# if a%2==0:
#     print("Bob")
# else:
#     print("Alice")  



# list=[]
# mod=[]
# for i in range(10):
#     a=int(input())
#     list.append(a)
#     m=a%42
#     if m not in mod:
#         mod.append(m)
# print(len(mod))



# def harshad_number(n):
#     old_n=n
#     t=0
#     while(n>0):
#         dig=n%10
#         t=t+dig
#         n=n//10
#     if oldN%t==0:
#         return old_n
#     else:
#         return harshad_number(old_n+1)
# n=int(input())
# print(harshad_number(n))



# result=[]
# n=int(input())
# for i in range(n):
#     a1,b1,c1=input().split()
#     a=int(a1)
#     b=int(b1)
#     c=int(c1)
#     if a+b==c or a-b==c or b-a==c or a*b==c or a/b==c or b/a==c:
#         result.append("Possible")
#     else:
#         result.append("Impossible")
# print("\n".join(result))

# n=int(input())
# for i in range(n):
#     k=i+1
#     print( str(k) + " Abracadabra")
        


# a,b=input().split()
# print(int(a)+int(b))



# a,b=input().split()
# print(2*int(b)-int(a))


# n=int(input())
# my_list=[]
# for i in range(n):
#     x=int(input())
#     my_list.append(x)
# for i in range(n):
#     j=i+1
#     print(my_list[-j])


# a,b=input().split()
# if int(a[::-1]) > int(b[::-1]):
#     print(a[::-1])
# else:
#     print(b[::-1])


# string=input()
# my_liste=list(string)
# first=[]
# second=[]
# third=[]
# for i in range(int(len(my_liste))):
#     if i<int(len(my_liste))/3:
#         first.append(my_liste[i])
#     elif i>=int(len(my_liste))/3 and i<2*int(len(my_liste))/3:
#         second.append(my_liste[i])
#     else:
#         third.append(my_liste[i])
# if first==second or first==third:
#     print("".join(first))
# elif second==third:
#     print("".join(second))



# a=int(input())
# print(int(str(bin(a)[2:])[::-1],2))


# s=input()
# print(s[::-1])



# x=int(input())
# sum=0
# for i in range(x):
#     n=int(input())
#     sum+=n
# print(sum)
