#!/bin/python3

import os
import sys


#
# Complete the mining function below.
#
A, B = [0], [0]
row = 0


def cut_cost(k, i ,j):
    if i == j:
        return 0
    return mines[k-1][0] * ((A[k] << 1) - A[i - 1] - A[j]) + \
                B[j] + B[i - 1] - (B[k] << 1)


def group_cost(k, j):
    return best[k + 1][j] + dp[(row - 1) & 1][k]


def solve_interval(L, R, fx, fy):
    if L > R:
        return
    M = (L + R) >> 1
    bi = max(fx, row)
    bx = min(fy, M)
    for i in range(bi, bx + 1):
        if cut_cost(bi, row, M) > cut_cost(i, row, M):
            bi = i
    best[row][M] = cut_cost(bi, row, M)
    if L != R:
        solve_interval(L, M - 1, fx, bi)
        solve_interval(M + 1, R, bi, fy)


def solve(L, R, fx, fy):
    if L > R:
        return
    M = (L + R) >> 1
    bi = max(fx, row - 1)
    bx = min(fy, M - 1)
    for i in range(bi, bx+1):
        if group_cost(bi, M) > group_cost(i, M):
            bi = i
    dp[row & 1][M] = group_cost(bi, M)
    if L != R:
        solve(L, M - 1, fx, bi)
        solve(M + 1, R, bi, fy)


def mining(k, mines):
    #
    # Write your code here.
    #
    global row
    for pos, wei in mines:
        A.append(A[-1] + wei)
        B.append(B[-1] + pos * wei)

    N = len(mines)
    for row in range(1, N+1):
        solve_interval(row, N, row, N)

    for x in range(1, N + 1):
        dp[1][x] = best[1][x]

    for row in range(2, k+1):
        dp[row & 1][row] = 0
        solve(row + 1, N, row - 1, N - 1)

    return dp[k & 1][N]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    mines = []

    for _ in range(n):
        mines.append(list(map(int, input().rstrip().split())))

    dp = []
    for i in range(2):
        dp.append([0]*(n+1))
    best = []
    for i in range(n+1):
        best.append([0]*(n+1))

    result = mining(k, mines)

    # print(result)
    fptr.write(str(result) + '\n')

    fptr.close()

