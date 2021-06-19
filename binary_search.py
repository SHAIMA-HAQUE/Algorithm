def binary_search(list,item):
    low = 0
    high = len(list) - 1

    while(low<=high):
        mid = low + high
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1
    return None



def main():
    list = [1,3,4,6,7,9]
    print(binary_search(list,3))
    print(binary_search(list,2))

if __name__ == "__main__":
    main()