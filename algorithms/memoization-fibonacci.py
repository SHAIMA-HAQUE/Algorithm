def f_c_driver(n):
    f = [-1]*(n+1)
    f[0] = 0
    f[1] = 1
    return fib_c(n, f)

def fib_c(n, f):
    if f[n]  == -1:
        f[n] = fib_c(n-1, f) + fib_c(n-2, f)
    
    return f[n]

def main():
    n = int(input("Enter the value of n"))
    res = f_c_driver(n)
    print(res)

if __name__ == "__main__":
    main()