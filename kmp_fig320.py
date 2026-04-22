from __future__ import annotations
import sys
from typing import List


# ====== Assignment 1 (Fig. 3.19): Failure function ======

def failure_function_fig319(keyword: str) -> List[int]:
    """
    Dragon Book (2nd ed.) Fig. 3.19 failure function, implemented with 1-based indexing.
    Returns a list such that result[s-1] = f(s), for s = 1..n.
    """
    n = len(keyword)
    if n == 0:
        return []

    # 1-based indexing: b[1]..b[n]
    b = [""] + list(keyword)

    # f[1]..f[n], f[0] unused in this function
    f = [0] * (n + 1)

    t = 0
    f[1] = 0

    # s = 1..n-1  (we compute f[s+1])
    for s in range(1, n):
        while t > 0 and b[s + 1] != b[t + 1]:
            t = f[t]

        if b[s + 1] == b[t + 1]:
            t += 1
            f[s + 1] = t
        else:
            f[s + 1] = 0

    return f[1:]


def build_f_array(keyword: str) -> List[int]:
    """
    Builds an array f such that f[s] = failure value for s = 0..n.
    We define f[0] = 0 and f[1..n] from Fig. 3.19.
    """
    fvals = failure_function_fig319(keyword)  # length n, corresponds to f(1)..f(n)
    return [0] + fvals


# ====== Assignment 2 (Fig. 3.20): KMP algorithm ======

def kmp_fig320(text: str, keyword: str) -> str:
    """
    Dragon Book Fig. 3.20: tests whether 'text' contains 'keyword' as a substring.
    Returns "yes" or "no" exactly like the book.
    """
    m = len(text)
    n = len(keyword)

    if n == 0:
        return "yes"  # empty keyword is always a substring

    # 1-based indexing for keyword: b[1]..b[n]
    b = [""] + list(keyword)

    # f[s] for s = 0..n
    f = build_f_array(keyword)

    s = 0  # number of matched characters so far

    # for (i = 1; i <= m; i++)
    for i in range(1, m + 1):
        ai = text[i - 1]  # a[i] in 1-based world

        # while (s > 0 && ai != b[s+1]) s = f(s)
        while s > 0 and ai != b[s + 1]:
            s = f[s]

        # if (ai == b[s+1]) s = s + 1
        if ai == b[s + 1]:
            s += 1

        # if (s == n) return "yes"
        if s == n:
            return "yes"

    return "no"


def main(argv: List[str]) -> int:
    if len(argv) < 3:
        print("Usage:")
        print("  python kmp_fig320.py <text> <keyword>")
        print("Examples:")
        print("  python kmp_fig320.py abababaab ababaa")
        return 2

    text = argv[1]
    keyword = argv[2]

    result = kmp_fig320(text, keyword)
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))