def fact(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * fact(x-1)

def main():
    x = int(input("Enter the number: "))
    print(fact(x))

if __name__ == "__main__":
    main()