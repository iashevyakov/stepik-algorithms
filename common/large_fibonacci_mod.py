def fib_mod(n, m):
    if n <= 1:
        return n
    mods = [0, 1]
    fibs = [0, 1]
    for i in range(2, n + 1):
        fib = fibs[i - 1] + fibs[i - 2]
        mod = fib % m
        if mod == 0 and mods[i - 1] == 1:
            c = i
            break
        else:
            fibs.append(mod)
            mods.append(mod)
    else:
        return fibs[n] % m

    return mods[n % c]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()