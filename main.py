# a,b=input().split()
# print((int(a)*int(b))/2)

# n=int(input())
# sum=0
# for i in range(n):
#     a=int(input());
#     p=a%10
#     a=int(a/10)
#     sum+=pow(a,p)
# print(sum)


# t=int(input())
# result=""
# for i in range(t):
#     l=[]
#     p=int(input())
#     for j in range(p):
#         a,b=input().split()
#         if int(a) not in l:
#             l.append(int(a))
#         else:
#             l.append(int(b))
#     if len(set(l))!=p:
#         result+="impossible"+"\n"
#     else:
#         l=[str(i) for i in l]
#         result+=" ".join(l)
#         result+="\n"
# print(result)



# import random
# r,c=input().split()
# l=[]
# for i in range(int(r)):
#     for j in range(int(c)):
#         l.append(random.randint(0,20))
# print(l)


# string="Hi"
# string1 =" Every one"
# print(f'{string}blabla')


# x=3
# x+=4
# print(x)

# l=[1,2,3]
# string=""
# print(" ".join(str(l)))


# strin="hi one"
# print(strin[1])

# def teams():
#     list = []
#     T = int(input("T:"))
#     for i in range(T):
#         N = int(input("N:"))
#         M = int(input("M:"))
#         for j in range(N):
#             list.append(input("student" + str(j+1) + ": "))
   
#         count = 0
#         for i in range(N):
#             for j in range(i+1, N):
#                 for k in range(j+1, N):
#                     niceTeam = True
#                     for l in range(M):
#                         if(list[i][l]=='n' and list[j][l]=='n' and list[k][l]=='n'):
#                             niceTeam = False
#                             break
#                     if(niceTeam):
#                         count += 1
#         print(count)

# teams()


# def teams():
# list = []
# teams_list = []
# T = int(input())
# for t in range(T):
#     N,M = input().split()
#     N,M=int(N),int(M)
#     for j in range(N):
#         list.append(input())
#     count = 0
#     for i in range(N):
#         for j in range(i+1, N):
#             for k in range(j+1, N):
#                 niceTeam = True
#                 for l in range(M):
#                     if(list[i][l]=='n' and list[j][l]=='n' and list[k][l]=='n'):
#                         niceTeam = False
#                         break
#                 if(niceTeam):
#                     count += 1
#     teams_list.append(count)
# for item in teams_list:
#     print(item)
# teams()


# l=[1,4]
# k=[3,4]
# print(l+k)


# string="1AA"
# S=string.replace('A', '2')
# print(S)
# print(int(string)+3)

# list=['f','f']
# print(list)

# l=[1,2]
# l.append(4)
# print(l)

# courses=["Laravel","Html","css","VueJs"]
# prices=[25,45,40,60]
# instructors=["Mohmad","Fouad","Soufiane"]
# result=zip(courses,prices,instructors)
# # print(list(result))
# print((result))

# t=(1,4)
# t.append(3)
# print(t)

# l=[1,3]
# print(*l,sep="\n")

t=("Team 1","Knapsackers@UNT","MoraSeekers","SurpriseTeam","CuSAT","DongskarPedongi","cofrades","viRUs","TeamName","TeamEPFL1","whatevs","WildCornAncestors","TheCornInTheFields","Aurora")
win=input()
for i in range(len(t)):
    if t[i]==win:
        print(i+1)
        break














