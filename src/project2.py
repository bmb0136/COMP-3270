'''
COMP 3270 Intro to Algorithms Homework 1: Introduction to Python
install python (google it) and make sure you have python version 3.6+ 
'''
import random
import time

'''
Problem 1: Implement merge sort
'''
def merge_sort(A):
    def _merge(A, L, mid, R):
        temp = [None] * (R - L)
        p1, p2 = L, mid
        pt = 0
        while p1 < mid and p2 < R:
            p1_in = p1 < mid
            p2_in = p2 < R
            if p1_in and not p2_in:
                temp[pt] = A[p1]
                p1 += 1
            elif not p1_in and p2_in:
                temp[pt] = A[p2]
                p2 += 1
            elif A[p1] < A[p2]:
                temp[pt] = A[p1]
                p1 += 1
            else:
                temp[pt] = A[p2]
                p2 += 1
            pt += 1
        for i in range(len(temp)):
            A[L + i] = temp[i]
    def _sort(A, L, R):
        if R - L <= 1:
            return
        mid = (L + R) // 2
        _sort(A, L, mid)
        _sort(A, mid, R)
        _merge(A, L, mid, R)
        pass
    _sort(A, 0, len(A))


'''
Problem 2: Implement quick sort 2 ways. 1 using a random element as the pivot. 2nd using the median of 3 random elements as the pivot
'''
#your code here



'''
Problem 3: Compare the runtime between merge sort, quick sort with random pivot, and quick sort with median of 3 random elements on lists ranging from 100k to 2m by increments of 100k 
use the time package to get the time, so use start = time.time() then after the algorithm runs end = time.time()
make a graph of this. I recommend the ggplot python port plotnine, but matplotlib would be fine as well
'''
#your code here
# inputs might look like A = [random.randint(0,1000000000) for i in range(100000)]


