
def findLongestPalindromicString(text): 
	N = len(text) 
	if N == 0: 
		return
	N = 2*N+1 
	L = [0] * N 
	L[0] = 0
	L[1] = 1
	C = 1	 
	R = 2	
	i = 0 
	iMirror = 0	 
	maxLPSLength = 0
	maxLPSCenterPosition = 0
	start = -1
	end = -1
	diff = -1

	for i in xrange(2,N): 
	
		iMirror = 2*C-i 
		L[i] = 0
		diff = R - i 
		if diff > 0: 
			L[i] = min(L[iMirror], diff) 

		try: 
			while ((i + L[i]) < N and (i - L[i]) > 0) and (((i + L[i] + 1) % 2 == 0) or (text[(i + L[i] + 1) / 2] == text[(i - L[i] - 1) / 2])): 
				L[i]+=1
		except Exception as e: 
			pass

		if L[i] > maxLPSLength:	
			maxLPSLength = L[i] 
			maxLPSCenterPosition = i 
 
		if i + L[i] > R: 
			C = i 
			R = i + L[i] 
 
	start = (maxLPSCenterPosition - maxLPSLength) / 2
	end = start + maxLPSLength - 1
	return end-start+1,text[start:end+1], 
 

t=int(input())
for i in range(t):
    st = raw_input()
    l = findLongestPalindromicString(st)
    if l[0]==len(st):
        sub1=findLongestPalindromicString(st[0:-1])
        sub2=findLongestPalindromicString(st[1:])
        print(max(sub1[0],sub2[0])+1)
    else:
        st = st.replace(l[1],'12')
        l2 = findLongestPalindromicString(st)
        print(l[0]+l2[0])