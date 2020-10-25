n=int(input())
main=[]
for i in range(1,n+1):
    main.append(i)
s=list(map(int,input().split()))
dic={}
count=0
while (True):
    pl=len(main)
    for i in range(len(main)):
        main[i]=s[main[i]-1]
    main=list(dict.fromkeys(main))
    l=len(main)
    if(pl==l):
        break
    count+=1
    dic[l]=count


t=int(input())
for i in range(t):
    x=int(input())
    if x in dic.keys():
        print(dic[x])
    else:
        print(-1)