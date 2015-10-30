class Solution:
	# @param A : integer
	# @return a list of list of integers
	def generateMatrix(self, A):
		result = [[0 for x in range(A)] for x in range(A)]
		## Actual code to populate result
		t = 0
		b = A - 1
		l = 0
		r = A - 1
		d = 0
		counter = 1
		while t<=b and l<=r:
			if d == 0:
				for i in xrange(l, r+1):
					result[t][i] = counter
					counter+=1
				t+=1
			elif d == 1:
				for i in xrange(t, b+1):
					result[i][r] = counter
					counter+=1
				r-=1
			elif d == 2:
				for i in xrange(r, l-1, -1):
					result[b][i] = counter
					counter+=1
				b-=1
			elif d == 3:
				for i in xrange(b, t-1, -1):
					result[i][l] = counter
					counter+=1
				l+=1
			d = (d+1)%4
		return result

