from time import perf_counter
import math
import random

def integer_operations(n):
    for j in range(n):
        for i in range(n):
            math.comb(i, j)
            math.factorial(i+j)
            math.perm(i, j)
            (j+i)*(j+j)*(j+n)*(i+i)*(i+j)*(i+n)*(n+i)*(n+j)*(n+n)

def floating_point_operations(n, r):
    for j in range(n):
        for i in range(n):
            r+n
             


time_start = perf_counter()
integer_operations(100)
time_end = perf_counter()

time_duration = time_end - time_start
print(f'[integer] Took {time_duration} seconds')

r = 0.38791489303425963
floating_point_operations(100, r)