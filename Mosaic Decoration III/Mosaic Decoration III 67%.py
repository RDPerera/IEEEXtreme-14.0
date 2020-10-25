H,W,h,w=list(map(int,input().split()))
tmp=0
for i in range(h):
    line=list(map(int,input().split()))
    tmp+=sum(line)
print(tmp*(H//h)*(W//w))