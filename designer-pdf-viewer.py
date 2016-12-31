#!/bin/python
"""
https://www.hackerrank.com/challenges/designer-pdf-viewer
"""
import sys

WIDTH = 1

h = map(int,raw_input().strip().split(' '))
word = raw_input().strip()

height = 0
for char in word:
    index = ord(char)-ord('a')
    if h[index] > height:
        height = h[index]

print height * (WIDTH * len(word))
