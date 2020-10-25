w,h,a,b,m,c=list(map(int,input().split()))
if w%a==0:
    if h%b==0:
        totalBlocks=(w//a)*(h//b)
        service=0
    else:
        totalBlocks=(w//a)*(h//b+1)
        service=w*c
else:
    if h%b==0:
        totalBlocks=(w//a+1)*(h//b)
        service=h*c
    else:
        totalBlocks=(w//a+1)*(h//b+1)
        service=(w+h)*c

if totalBlocks%10==0:
    totalCost=m*(totalBlocks//10)+service
else:
    totalCost=m*(totalBlocks//10+1)+service
print(totalCost)