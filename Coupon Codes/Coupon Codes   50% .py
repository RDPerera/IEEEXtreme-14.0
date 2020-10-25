def hamming_distance(string1, string2):
	dist_counter = 0
	for n in range(len(string1)):
		if string1[n] != string2[n]:
			dist_counter += 1
	return dist_counter

n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
count=0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if hamming_distance(arr[i],arr[j])==1:
            count+=1
print(count) 
