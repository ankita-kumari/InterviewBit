class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
    	num = set([])
    	for i in xrange(0, len(A)):
    		if A[i] in num:
    			return A[i]
    		else:
    			num.add(A[i])
    	return A[0]

if __name__ == '__main__':
	x = Solution()
	print x.repeatedNumber( [3,4,1,4,1] )

