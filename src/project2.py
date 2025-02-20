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
        while p1 < mid or p2 < R:
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
def _partition(A, L, R, pindex):
    if R - L <= 1:
        return
    low, high = L + 1, R - 1
    A[L], A[pindex] = A[pindex], A[L]
    pivot = A[L]
    while low <= high:
        while low < R and A[low] <= pivot:
            low += 1
        while high > L and A[high] > pivot:
            high -= 1
        if high > low:
            A[low], A[high] = A[high], A[low]
    A[high], A[L] = A[L], A[high]
    return high
def quick_sort1(A):
    def _sort(A, L, R):
        if R - L <= 1:
            return
        pindex = random.randint(L, R - 1)
        pindex = _partition(A, L, R, pindex)
        _sort(A, L, pindex)
        _sort(A, pindex, R)
    _sort(A, 0, len(A))
def quick_sort2(A):
    def _sort(A, L, R):
        if R - L <= 1:
            return
        
        i1, i2, i3 = None, None, None
        while True:
            if i1 == None:
                i1 = random.randint(L, R - 1)
            elif i2 == None or i2 == i1:
                i2 = random.randint(L, R - 1)
            elif i3 == None or i3 == i1 or i3 == i2:
                i3 = random.randint(L, R - 1)
            else:
                break

        v1, v2, v3 = A[i1], A[i2], A[i3]
        if v2 <= v1 <= v3 or v3 <= v1 <= v2:
            pindex = i1
        elif v1 <= v2 <= v3 or v3 <= v1 <= v2:
            pindex = i2
        else:
            pindex = i3
            
        pindex = _partition(A, L, R, pindex)
        _sort(A, L, pindex)
        _sort(A, pindex, R)


'''
Problem 3: Compare the runtime between merge sort, quick sort with random pivot, and quick sort with median of 3 random elements on lists ranging from 100k to 2m by increments of 100k 
use the time package to get the time, so use start = time.time() then after the algorithm runs end = time.time()
make a graph of this. I recommend the ggplot python port plotnine, but matplotlib would be fine as well
'''
#your code here
# inputs might look like A = [random.randint(0,1000000000) for i in range(100000)]


# TODO REMOVE ME BEFORE SUBMITTING
testing = False
for i in range(1 if testing else 1000):
    A = [random.randint(0,25 if testing else 1000000) for i in range(15 if testing else 1000)]
    A.sort()

    B = A.copy()
    merge_sort(B)
    #if testing:
        #print(A)
        #print(B)
    assert A == B, "Merge sort broken"

    B = A.copy()
    quick_sort1(B)
    #if testing:
        #print(A)
        #print(B)
    assert A == B, "Quick sort (random elem) broken"

    B = A.copy()
    quick_sort2(B)
    if testing:
        print(A)
        print(B)
    assert A == B, "Quick sort (3 median) broken"

