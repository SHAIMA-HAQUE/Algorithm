def fib(n):
    f = [None] * (100)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

def main():
    n = int(input())
    res = fib(n)
    print(res)

if __name__ == '__main__':
    main()