class Solution:
	# @param A : integer
	# @return a list of list of integers
	def generate(self, A):
		if A == 0:
			return []
		elif A == 1:
			return [[1]]
		#result = [0 for x in range(A)]
		result = []
		result.append([1])
		for i in xrange(1, A):
			arr = [0 for x in xrange(i+1)]
			for j in xrange(0, i+1):
				x = result[i-1][j] if j<len(result[i-1]) else 0
				y = result[i-1][j-1] if j-1>=0 else 0
				arr[j] = x + y
			result.append(arr)
		return result

if __name__ == '__main__':
    x = Solution()
    print x.generate(1)

