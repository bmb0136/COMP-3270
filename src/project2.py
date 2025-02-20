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
import sys
import queue
import threading
def test(func, sizes, runs=3):
    times = [0 for _ in sizes]
    tasks = queue.Queue()
    done = queue.Queue()
    complete = [0 for _ in sizes]

    print(f"Testing {func.__name__}:")
    for i, n in enumerate(sizes):
        if i == 0:
            print("\x1b[s", end="");
        print(f"\tN={n} (0/{runs})")

    def _thread(t, d, f):
        import time
        while (item := t.get()) != None:
            i, n = item
            A = [random.randint(0, 1000000000) for i in range(n)]
            start = time.time()
            f(A)
            total = time.time() - start

            d.put_nowait((i, total))
            t.task_done()

    threads = [None] * 4
    for i in range(len(threads)):
        threads[i] = threading.Thread(target=_thread, args=(tasks, done, func))
        threads[i].start()

    for t in ([(i, x) for i, x in enumerate(sizes)] * runs):
        tasks.put_nowait(t)

    while True:
        all_done = True
        for x in complete:
            if x < runs:
                all_done = False
                break
        if all_done:
            break
        i, time = done.get()
        done.task_done()

        complete[i] += 1
        times[i] += time

        print(f"\x1b[u\x1b[s", end="")
        if i > 0:
            print(f"\x1b[{i}B", end="")
        print(f"\tN={sizes[i]} ({complete[i]}/{runs})", end="")
        sys.stdout.flush()

        if complete[i] >= runs:
            times[i] /= runs
            print(f" [Average: {times[i]:.3f}s]")
    """
    for i, n in enumerate(sizes):
        print(f"\tN={n}: (\x1b[s", end="")
        total = 0
        for j in range(runs):
            print(f"\x1b[u{j + 1}/{runs})", end="")
            sys.stdout.flush()
            A = [random.randint(0, 1000000000) for i in range(n)]
            start = time.time()
            func(A)
            total += time.time() - start
            assert _is_sorted(A), f"{func.__name__} failed to sort. Got {A}, but expected {sorted(A)}"
        times[i] = total / runs

        print(f" [Average: {times[i] * 1000:.3f}ms]")
    """
    return times

sizes = list(range(100000, 2000001, 100000))
t_merge_sort = test(merge_sort, sizes)
t_quick_sort1 = test(quick_sort1, sizes)
t_quick_sort2 = test(quick_sort2, sizes)

import matplotlib.pyplot as plt

plt.plot(sizes, t_merge_sort, label="Merge Sort", color="red")
plt.plot(sizes, t_quick_sort1, label="Quick Sort (Random)", color="green")
plt.plot(sizes, t_quick_sort2, label="Quick Sort (Median)", color="blue")

plt.title("Sorting Times")
plt.xlabel("Array Size (items)")
plt.ylabel("Time (s)")

plt.legend()

plt.show()
