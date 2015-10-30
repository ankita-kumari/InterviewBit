class Solution:
        # @param A : list of integers
        # @return a list of integers
        def maxset(self, A):
            prev_start = 0
            prev_len = 0
            prev_sum = 0
            curr_sum = 0
            curr_start = 0
            curr_len = 0

            for i in xrange(len( A )):
                if A[i] >= 0:
                    curr_sum += A[i]
                    curr_len++
                if A[i] < 0 or i == len( A )-1:
                    if prev_sum < curr_sum:
                        prev_sum = curr_sum
                        prev_start = curr_start
                        prev_len = curr_len
                    elif prev_sum == curr_sum:
                        if prev_len < curr_len:
                            prev_len = curr_len
                            prev_start = curr_start
                        elif prev_len == curr_len:
                            if A[prev_start] > A[curr_start]:
                                prev_start = curr_start
                    curr_sum = 0
                    curr_len = 0
                    curr_start = i+1
            return A[prev_start:prev_start + prev_len]
