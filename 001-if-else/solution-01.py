#!/bin/python3

N = int(input())

if (N%2 == 1) or (N%2 == 0 and 6 <= N <=20):
    print('Weird')
else:
    print('Not Weird')
