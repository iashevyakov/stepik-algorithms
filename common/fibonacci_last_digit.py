def fib_digit(n):
    if n<=1:
        return n
    l = [0, 1]
    for i in range(2, n + 1):
        d = (l[i-1] + l[i-2]) % 10
        l.append(d)
    return l[n]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()