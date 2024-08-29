import sys
sys.dont_write_bytecode = True

import os
from time import perf_counter
import math
import numpy as np
import pyfracgen as pf
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colormaps

import matrixes
import custom_disk

def integer_operations(n):
    for j in range(n):
        for i in range(n):
            math.comb(i, j)
            math.factorial(i+j)
            math.perm(i, j)
            (j+i)*(j+j)*(j+n)*(i+i)*(i+j)*(i+n)*(n+i)*(n+j)*(n+n)*(j-200)*(j+j)*(-500+n)*(-1200+i)*(i+j)*(i+n)*(n+i)*(n+j)*(n+n)

def floating_point_operations(n):
    # 53.656732595121234
    r = math.pi * math.e * math.tau
    for j in range(n):
        for i in range(n):
            math.sqrt(j+i+r)
            math.cbrt(j+i+r)
            math.exp(r / (1+j+i))
            math.exp2(r / (1+j+i))
            math.log(j+i+r)
            math.log2(j+i+r)
            math.cos(j+i+r)
            math.sin(j+i+r)
            math.tan(j+i+r)
            math.tanh(j+i+r)
            (r * (i+1) + (j+1)) / ((i+1) * r - (j+1))

def matrix_operations(A, B, n):
    for i in range(n):
        np.dot(A, B)
        np.dot(np.transpose(A), np.transpose(B))
        np.dot(A, A)
        np.dot(np.transpose(A), np.transpose(A))
        np.dot(B, B)
        np.dot(np.transpose(B), np.transpose(B))

def graphical_operations():
    string = "AAAAAABBBBBB"
    xbound = (2.5, 3.4)
    ybound = (3.4, 4.0)
    res = pf.lyapunov(string, xbound, ybound, width=4, height=3, dpi=300, ninit=2000, niter=2000)
    pf.images.markus_lyapunov_image(res, colormaps["bone"], colormaps["bone_r"], gammas=(8, 1))
    plt.savefig("lyapunov.png")

def disk_operations(source_file, n):
    for i in range(n):
        custom_disk.copy_file(source_file, f"copy_{i}_{source_file}")

        if not custom_disk.compare_files(source_file, f"copy_{i}_{source_file}"):
            print("[file {i}] mismatched")
        else:
            print(f"[file {i}] ok")


# Tempo de execução de operações inteiras
time_start = perf_counter()
integer_operations(1000)
time_end = perf_counter()

time_duration = time_end - time_start
print(f'[integer] {time_duration} seconds')

# Tempo de execução de operações ponto flutuante
time_start = perf_counter()
floating_point_operations(1000)
time_end = perf_counter()

time_duration = time_end - time_start
print(f'[float] {time_duration} seconds')

# Tempo de execução de operações matriciais
A = matrixes.A
B = matrixes.B
time_start = perf_counter()
matrix_operations(A, B, 10000)
time_end = perf_counter()

time_duration = time_end - time_start
print(f'[matrix] {time_duration} seconds')

# Tempo de execução de operações gráficas
time_start = perf_counter()
graphical_operations()
time_end = perf_counter()

time_duration = time_end - time_start
print(f'[graphical] {time_duration} seconds')

# Tempo de execução de operações de disco
time_start = perf_counter()
disk_operations("100000000B.txt", 10)
time_end = perf_counter()

time_duration = time_end - time_start
print(f'[disk] {time_duration} seconds')