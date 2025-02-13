"""
COMP 3270 Intro to Algorithms Homework 1: Introduction to Python
install python (google it) and make sure you have python version 3.6+ 
"""

import random
import time
from collections.abc import Generator

"""
Problem 1: Make your own hashmap class from scratch (using only python lists). dicts not allowed. This problem will be 75% of this homework
Implement chaining in case of collisions. 
Use any hash function you like (such as those in the lecture notes). 
The underlying list may be fixed length. You do not have to account for the need to double its size when it is near capacity. Set it to 1024
Allow for types int and str (to convert an arbitrary str to a number you can use number = int.from_bytes(mystring.encode('utf-8'), 'little') and to recover the str you can use recoveredstring = number.to_bytes((number.bit_length() + 7) // 8, 'little').decode('utf-8').
For each key, there should be an associated value.
Implement insert(self, key, value), delete(self, key), get(self, key), and iter(self) which only loops through non-empty key, value pairs.
See https://www.w3schools.com/python/python_iterators.asp for how to implement an iterator in python
"""


class mymap[K, V]:
    data: list[list[tuple[K, V]]]
    def __init__(self):
        self.data = [[] * 1024]
    def get(self, key: K) -> V | None:
        pass
    def insert(self, key: K, value: V) -> None:
        pass
    def delete(self, key: K) -> None:
        pass
    def iter(self) -> Generator[tuple[K, V]]:
        for x in self.data:
            for y in x:
                yield y


"""
Problem 2: Use your hashmap class to count the number of each substring of length k in a DNA sequence. 
Print out the repeated items and the number of times they were repeated
run it on string "ATCTTGGTTATTGCGTGGTTATTCTTGC" with k=4
"""
expected = dict[str, int]()

d = mymap[str, int]()
s = "ATCTTGGTTATTGCGTGGTTATTCTTGC"
k = 4
for i in range(len(s) - k):
    sub = s[i : i + k]
    v = d.get(sub)
    if v:
        d.delete(sub)
        d.insert(sub, v + 1)
    else:
        d.insert(sub, 1)

    if sub in expected:
        expected[sub] += 1
    else:
        expected[sub] = 1
assert list(sorted(expected)) == list(sorted(d.iter()))

"""
Problem 3: Two sum. This time just use the python dict or set. 
Given an array, find two numbers that sum to a target number (don't worry about not reusing the same index this time). 
Code this two ways. Once brute force with nested for loops. And once using hashing. 
Use the input below. Bonus to code the sorting/binary search method. Feel free to use sort() or sorted() but code binary search yourself.
Compare the time taken between the implementations using the time package imported above.
"""
A = [random.randint(0, 1000000000) for _ in range(10000)]
target = A[random.randint(0, len(A) - 1)] + A[random.randint(0, len(A) - 1)]

start = time.time_ns()
for i in range(len(A)):
    broke = False
    for j in range(i + 1, len(A)):
        if A[i] + A[j] == target:
            broke = True
            print(f"Positions: {i}, {j} | Values: {A[i]}, {A[j]}")
            break
    if broke:
        break
print(f"O(n^2) version: {(time.time_ns() - start) / 1_000_000_000}")

start = time.time_ns()
m = dict[int, int]()
for i, x in enumerate(A):
    y = target - x
    if y in m:
        print(f"Positions: {i}, {m[y]} | Values: {x}, {y}")
        break
    m[x] = i
print(f"O(n) version: {(time.time_ns() - start) / 1_000_000_000}")
