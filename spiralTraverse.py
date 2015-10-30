class Solution:
# @param A : tuple of list of integers
# @return a list of integers
    def spiralOrder(self, A):
        result = []
        ## Actual code to populate result
        t = 0
        b = len( A ) - 1
        l = 0
        r = len( A[0] ) - 1
        d = 0
        while t<=b and l<=r:
            if d == 0:
                for i in xrange(l, r+1): 
                    result.append( A[t][i] )
                t+=1    
            elif d == 1:
                for i in xrange(t, b+1):
                    result.append( A[i][r] )
                r-=1    
            elif d == 2:
                for i in xrange(r, l-1, -1):
                    result.append( A[b][i] )
                b-=1    
            elif d == 3:
                for i in xrange(b, t-1, -1):
                    result.append( A[i][l] )
                l+=1    
            d = (d+1)%4        
        return result
