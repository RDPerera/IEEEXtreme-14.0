c,n,p,w=list(map(int,input().split()))

ans=(w//c)
if c<p and ans>n-(w//p):
    ans=n-(w//p)
print(ans)