### use Radix sort to sort the pairs, by using counting sort twice. First on right class then on left class
### Algorthm is of complexity O(nlogn)


def radix_sort(pairs):

	## sort according to a.right
	right_counts=[0]*len(pairs)

	for i in range(len(pairs)):
		right_counts[pairs[i][1]]+=1

	right_indexes=[0]*len(pairs)
	for i in range(1,len(pairs)):
		right_indexes[i]=right_counts[i-1]+right_indexes[i-1]

	sort_right_pairs=[0]*len(pairs)
	for i in range(len(pairs)):
		sort_right_pairs[right_indexes[pairs[i][1]]]=pairs[i]
		right_indexes[pairs[i][1]]+=1

	# copy array
	pairs=sort_right_pairs.copy()
	
	# sort acc to left elements
	left_counts=[0]*len(pairs)

	for i in range(len(pairs)):
		left_counts[pairs[i][0]]+=1

	left_indexes=[0]*len(pairs)
	for i in range(1,len(pairs)):
		left_indexes[i]=left_counts[i-1]+left_indexes[i-1]

	sort_left_pairs=[0]*len(pairs)
	for i in range(len(pairs)):
		sort_left_pairs[left_indexes[pairs[i][0]]]=pairs[i]
		left_indexes[pairs[i][0]]+=1
	
	return sort_left_pairs

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
		### make pairs
		for i in range(len(string)):
			pairs[i]=[classes[i],classes[(i+(1<<k))%len(string)],i]
		### sort pairs using radix sort
		pairs=radix_sort(pairs)
		## make equivalence classes 
		classes=[0]*len(string)
		for i in range(1,len(pairs)):
			if(pairs[i][0]==pairs[i-1][0] and pairs[i][1]==pairs[i-1][1]):
				classes[pairs[i][2]]=classes[pairs[i-1][2]]
			else:
				classes[pairs[i][2]]=classes[pairs[i-1][2]]+1
		k+=1
	return pairs

def main():
	s=input()
	# s="ababba"
	suffix_array=solve(s)
	for i in range(len(suffix_array)):
		print(suffix_array[i][2],end=' ')
		# print(s[suffix_array[i][2]:])

if __name__=="__main__":
	main()