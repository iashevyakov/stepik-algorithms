def fib(n):
    if n <= 1:
        return n
    l = [0, 1]
    for i in range(2, n + 1):
        l.append(l[i - 1] + l[i - 2])
    return l[n]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()