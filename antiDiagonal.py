class Solution:
	# @param A : list of list of integers
	# @return a list of list of integers
	def diagonal(self, A):
		result = []
		for i in xrange(0, len( A )):
			j = 0
			arr = []
			if i == j:
				arr.append( A[j][i] )
			else:
				while j < len(A) and i >= 0:
					arr.append( A[j][i] )
					j+=1
					i-=1
			result.append( arr )
		for i in xrange(1, len( A )):
			j = len(A) - 1
			arr = []
			if i == j:
				arr.append( A[i][j] )
			else:
				sum = i+j
				while i+j == sum and i < len(A) and j < len(A):
					arr.append(A[i][j])
					i+=1
					j-=1
			result.append( arr )
		return result

if __name__ == '__main__':
    x = Solution()
    print x.diagonal( [[1, 2], [3, 4]] )
