class Solution:
	# @param A : integer
	# @return a list of integers
	def getRow(self, A):
		if A == 0:
			return [1]
		#result = [0 for x in range(A)]
		result = [1]
		for i in xrange(0, A+1):
			arr = [0 for x in xrange(i+1)]
			for j in xrange(0, i+1):
				x = result[j] if j<len(result) else 0
				y = result[j-1] if j-1>=0 else 0
				arr[j] = x + y
			result = arr
		return result

if __name__ == '__main__':
    x = Solution()
    print x.getRow(2)

