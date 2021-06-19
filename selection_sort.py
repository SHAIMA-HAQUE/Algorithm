def find_smallest(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(len(list)):
        if list[i]<list[smallest_index]:
            smallest_index = i
            smallest = list[i]
    return smallest_index

def selection_sort(list):
    new_list = []
    for i in range(len(list)):
        smallest = find_smallest(list)
        new_list.append(list.pop(smallest))
    return new_list

def main():
    list = [1,3,2,9,5,0]
    print(selection_sort(list))

if __name__ == "__main__":
    main()


