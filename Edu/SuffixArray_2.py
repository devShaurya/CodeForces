def solve(string):
	string=string+'$'
	pairs=[[string[i],i] for i in range(len(string))]
	pairs.sort()
	classes=[0]*len(string)
	classes[pairs[0][1]]=0
	
	## k=0
	for i in range(1,len(pairs)):
		if(pairs[i][0]==pairs[i-1][0]):
			classes[pairs[i][1]]=classes[pairs[i-1][1]]
		else:
			classes[pairs[i][1]]=classes[pairs[i-1][1]]+1

	## k->k+1
	k=0
	while((1<<k)<len(string)):
		for i in range(len(string)):
			pairs[i]=[classes[i],classes[(i+(1<<k))%len(string)],i]

		pairs.sort()
		classes=[0]*len(string)
		for i in range(1,len(pairs)):
			if(pairs[i][0]==pairs[i-1][0] and pairs[i][1]==pairs[i-1][1]):
				classes[pairs[i][2]]=classes[pairs[i-1][2]]
			else:
				classes[pairs[i][2]]=classes[pairs[i-1][2]]+1
		k+=1
	return pairs

def main():
	# s=input()
	s="ababba"
	suffix_array=solve(s)
	for i in range(len(suffix_array)):
		print(suffix_array[i][2],end=' ')
		# print(s[suffix_array[i][2]:])

if __name__=="__main__":
	main()