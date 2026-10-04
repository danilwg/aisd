import time
import math

def def1(a, n):
    if n < 2:
        return []
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for p in range(2, int(math.isqrt(n)) + 1):
        if s[p]:
            for i in range(p * p, n + 1, p):
                s[i] = False
    return [i for i in range(max(2, a), n + 1) if s[i]]

def def2(a, n):
    if n < 2:
        return []
    limit = int(math.isqrt(n))
    base_s = [True] * (limit + 1)
    base_s[0] = base_s[1] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if base_s[p]:
            for i in range(p * p, limit + 1, p):
                base_s[i] = False
    base_primes = [i for i, is_p in enumerate(base_s) if is_p]

    start = max(a, 2)
    if start > n:
        return []

    segment = [True] * (n - start + 1)
    for p in base_primes:
        base = max(p * p, (start + p - 1) // p * p)
        for j in range(base, n + 1, p):
            segment[j - start] = False

    return [start + i for i, is_p in enumerate(segment) if is_p and (start + i) >= a]

tests = [
    (2, 10_000),
    (1_000, 10_000),
    (2, 100_000),
    (10_000, 100_000)
]

for a, n in tests:
    t0 = time.perf_counter()
    def1(a, n)
    t1 = time.perf_counter() - t0

    t0 = time.perf_counter()
    def2(a, n)
    t2 = time.perf_counter() - t0

    print(f"[{a}..{n}] | Def1: {t1:.6f}s | Def2: {t2:.6f}s")