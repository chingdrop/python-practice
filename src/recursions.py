# File - recursions.py
# Latest Version - Chapter 13
# A collection of simple recursive functions (Some also include looping counterparts).


def fact(n):
    # returns factorial of n
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def reverse(s):
    # returns reverse of string s
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]


def anagrams(s):
    # returns a list of all anagrams of string s
    if s == "":
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            for pos in range(len(w) + 1):
                ans.append(w[:pos] + s[0] + w[pos:])
        return ans


def loop_power(a, n):
    # returns a rasied to int power n
    ans = 1
    for i in range(n):
        ans = ans * a
    return ans


def rec_power(a, n):
    # returns a raised to int power n
    if n == 0:
        return 1
    else:
        factor = rec_power(a, n / 2)
        if n % 2 == 0:  # n is even
            return factor * factor
        else:
            return factor * factor * a


def loop_fib(n):
    # returns the nth Fibonacci number
    curr = 1
    prev = 1
    for i in range(n - 2):
        curr, prev = curr + prev, curr
    return curr


def rec_fib(n):
    # returns nth Fibonacci number
    # Note: this algorithm is exceedingly inefficient!
    if n < 3:
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)
