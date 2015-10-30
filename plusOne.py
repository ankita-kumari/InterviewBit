class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
    	counter = 0
    	for i in A:
    		if i == 0:
    			counter += 1
    		else:
    			break
    	A = A[counter :]
    	s = 0
    	c = 1
    	for i in xrange(len(A)-1, -1, -1 ):
    		n = A[i]
    		s = (n + c)%10
    		c = (n + c)/10
    		A[i] = s
    	if c == 1:
    		return [c] + A
    	return A

if __name__ == '__main__':
    x = Solution()
    print x.plusOne( [ 3, 0, 6, 4, 0 ] )


