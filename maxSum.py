class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
    	max_sum_so_far = A[0]
    	sum_so_far = A[0]
    	for i in xrange(1, len(A)):
    		if A[i] > (A[i] + sum_so_far):
    			sum_so_far = A[i]
    		else:
    			sum_so_far += A[i]
    		if sum_so_far > max_sum_so_far:
    			max_sum_so_far = sum_so_far
    	return max_sum_so_far

if __name__ == '__main__':
    x = Solution()
    print x.maxSubArray( [1, -1, 10] )


