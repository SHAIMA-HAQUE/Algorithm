#An application of D&C(Divide and Conquer)

def quicksort(array):
    # array with length 0 and 1 do not need to be sorted
    if len(array)<2:
        return array
    else:
        pivot = array[0] #Considering a pivot
        less = [i for i in array[1:] if i <= pivot] # creating subarray of all elements less than the pivot
        greater = [i for i in array[1:] if i > pivot] # creating subarray of all elements greater than the pivot

        return quicksort(less) + [pivot] + quicksort(greater)

def main():
    print(quicksort([3,4,8,9,2]))

if __name__ == '__main__':
    main()