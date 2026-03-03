from __future__ import annotations
import sys
from typing import List


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

    # f[1]..f[n], f[0] unused
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


def print_table(keyword: str, fvals: List[int]) -> None:
    print(f"keyword = {keyword}")
    print("s   : " + " ".join(f"{i:>2}" for i in range(1, len(fvals) + 1)))
    print("f(s): " + " ".join(f"{v:>2}" for v in fvals))


def self_test() -> None:
    k = "ababaa"
    expected = [0, 0, 1, 2, 3, 1]
    got = failure_function_fig319(k)
    assert got == expected, f"Expected {expected}, got {got}"
    print("Self-test OK.")


def main(argv: List[str]) -> int:
    if len(argv) >= 2 and argv[1] == "--test":
        self_test()
        return 0

    if len(argv) < 2:
        print("Usage:")
        print("  python failure_function_fig319.py <keyword> [--table]")
        print("  python failure_function_fig319.py --test")
        return 2

    keyword = argv[1]
    fvals = failure_function_fig319(keyword)

    if "--table" in argv:
        print_table(keyword, fvals)
    else:
        print(fvals)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))