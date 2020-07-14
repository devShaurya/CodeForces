'''
1. This is implementation of suffix array algorithm
2. It uses equivalence classes and comparision between smaller subtrings of size 2^k (using equivalence class) for comparision
	b/w strings of length 2^(k+1). It uses inbuilt sorting algorithm of python which is TimSort
3. its time complexity is nlog^2(n).

4. Key takeaway to use equivalence classes for comaprision b/w strings. and for code addition > bit shifting. So do bit shifting first 
then addition.
'''

def solve(string):
	## k=0
	## string_starts are for pairs and start indices
	## classes is for equivalence classes
	string=string+'$'

	pairs=[]
	for i in range(len(string)):
		pairs.append([string[i],i])
	
	pairs.sort()
	
	classes=[0]*len(string)
	classes[pairs[0][1]]=0
	for i in range(1,len(string)):
		if(pairs[i][0]!=pairs[i-1][0]):
			classes[pairs[i][1]]=classes[pairs[i-1][1]]+1
		else:
			classes[pairs[i][1]]=classes[pairs[i-1][1]]
	# print(pairs,classes)
	#### do for k+1
	k=0
	while (1<<k)<len(string):
		## calculate pairs of a.right and a.left of length 2**k
		for i in range(len(string)):
			pairs[i]=[classes[i],classes[(i+(1<<k))%len(string)],i,(i+(1<<k))%len(string)]
		
		pairs.sort()
		## make equivalence classes
		classes[pairs[0][2]]=0
		for i in range(1,len(string)):
			if (pairs[i][0]==pairs[i-1][0] and pairs[i][1]==pairs[i-1][1]):
				classes[pairs[i][2]]=classes[pairs[i-1][2]]
			else:
				classes[pairs[i][2]]=classes[pairs[i-1][2]]+1
		k+=1
		# print(pairs,classes)
	return pairs

def main():
	s=input()
	# s="shaurya"
	suffix_array=solve(s)
	for i in range(len(suffix_array)):
		# print(suffix_array[i][2],s[suffix_array[i][2]:])
		print(suffix_array[i][2],end=' ')

if __name__=="__main__":
	main()
