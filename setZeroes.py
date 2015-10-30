class Solution:
	# @param A : list of list of integers
	# @return the same list modified
	def setZeroes(self, A):
		row_flag = 0
		col_flag = 0
		for i in xrange(0, len(A[0])):
			if A[0][i] == 0:
				row_flag = 1
		for i in xrange(0, len(A)):
			if A[i][0] == 0:
				col_flag = 1
		for i in xrange(0, len(A)):
			for j in xrange(0, len(A[0])):
				if A[i][j] == 0:
					A[i][0] = 0
					A[0][j] = 0
		for i in xrange(1, len(A)):
			for j in xrange(1, len(A[0])):
				if A[i][0] == 0 or A[0][j] == 0:
					A[i][j] = 0
		if row_flag == 1:
			for i in xrange(0, len(A[0])):
				A[0][i] = 0
		if col_flag == 1:
			for i in xrange(0, len(A)):
				A[i][0] = 0

		return A


if __name__ == '__main__':
	x = Solution()
	print x.setZeroes( [ [0,1], [1,1] ] )
