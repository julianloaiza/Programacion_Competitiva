#!/usr/bin/env python3

import sys
import math
import os

sys.setrecursionlimit(10**7)
DEBUG = os.environ.get("DEBUG") is not None

def debug(*args):
    if DEBUG:
        print(*args, file=sys.stderr)

INF = 10**15
EPS = 1e-9

def input_data():
    return sys.stdin.readline().rstrip("\n")

def print_data(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return (a // gcd(a, b)) * b

def mod_exp(base, exp, mod):
    result = 1 % mod
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

def solve():
    pass

def main():
    if 'LOCAL' in os.environ:
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')

    t = 1
    # t = int(input_data())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
