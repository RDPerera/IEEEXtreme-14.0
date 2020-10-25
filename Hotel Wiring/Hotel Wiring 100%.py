t=int(input())
for i in range (t):
    arr=[]
    m,n,k=list(map(int,input().split()))
    for j in range (m):
        c=int(input())
        arr.append(c)
    arr.sort(reverse=True)
    tot=0
    for q in range(0,len(arr)-k):
        tot+=arr[q]
    for p in range(len(arr)-k,len(arr)):
        tot+=(n-arr[p])
    print(tot)