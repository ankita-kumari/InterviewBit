class Solution:
	# @param X : list of integers
	# @param Y : list of integers
	# Points are represented by (X[i], Y[i])
	# @return an integer
	def coverPoints(self, X, Y):
		steps = 0
		for i in xrange(1, len(X)):
			r = abs( X[i] - X[i-1] )
			c = abs( Y[i] - Y[i-1] )
			step = r if r>c else c
			steps += step
		return steps

if __name__ == '__main__':
    x = Solution()
    print x.coverPoints( [1,3,0], [1,2,3] )
