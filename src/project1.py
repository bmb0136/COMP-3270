"""
COMP 3270 Intro to Algorithms Homework 1: Introduction to Python
install python (google it) and make sure you have python version 3.6+ 
"""

import random
import time

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
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
    def iter(self):
        current = self
        while current:
            yield current
            current = current.next
class mymap:
    def __init__(self):
        self.data = [None] * 1024
    def get(self, key):
        node = self._get_node(key)
        if node:
            return node.val
        return None
    def _get_node(self, key):
        current = self.data[self._hash(key)]
        while current:
            if current.key == key:
                return current
            current = current.next
        return None
    def insert(self, key, value):
        index = self._hash(key)
        if self.data[index] == None:
            self.data[index] = Node(key, value)
            return
        current = self.data[index]
        prev = None
        while current:
            if current.key == key:
                raise Exception("Key already exists")
            prev = current
            current = current.next
        prev.next = Node(key, value)
    def delete(self, key):
        index = self._hash(key)
        current = self.data[index]
        if not current:
            return
        if current.key == key:
            self.data[index] = current.next
            return
        prev = current
        current = current.next
        while current:
            if current.key == key:
                prev.next = current.next
                return
            prev = current
            current = current.next
    def iter(self):
        for x in self.data:
            if x:
                for y in x.iter():
                    yield (y.key, y.val)
    def _hash(self, x):
        if type(x) == str:
            n = int.from_bytes(x.encode('utf-8'), 'little')
        elif type(x) == int:
            n = x
        else:
            raise Exception(f"Type {type(x)} not supported")
        return n % len(self.data)


"""
Problem 2: Use your hashmap class to count the number of each substring of length k in a DNA sequence. 
Print out the repeated items and the number of times they were repeated
run it on string "ATCTTGGTTATTGCGTGGTTATTCTTGC" with k=4
"""
d = mymap()
s = "ATCTTGGTTATTGCGTGGTTATTCTTGC"
k = 4
for i in range(len(s) - k):
    sub = s[i : i + k]
    v = d.get(sub)
    if v != None:
        d.delete(sub)
        d.insert(sub, v + 1)
    else:
        d.insert(sub, 1)
for k, v in d.iter():
    print(k, v)

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
m = {}
for i, x in enumerate(A):
    y = target - x
    if y in m:
        print(f"Positions: {i}, {m[y]} | Values: {x}, {y}")
        break
    m[x] = i
print(f"O(n) version: {(time.time_ns() - start) / 1_000_000_000}")

start = time.time_ns()
A2 = sorted(A)
for i, x in enumerate(A2):
    left = 0
    right = len(A2) - 1
    broke = False
    while left <= right:
        mid = (left + right) // 2
        val = A2[mid]
        s = val + x
        if s == target:
            broke = True
            print(f"Positions*: {i}, {mid} | Values: {x}, {val}")
            print("*These will be different because the list was sorted")
            break
        elif s < target:
            left = mid + 1
        else:
            right = mid - 1
    if broke:
        break
print(f"O(n*log(n)) version: {(time.time_ns() - start) / 1_000_000_000}")

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
