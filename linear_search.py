def main():
    len = int(input("Enter the length of the list: "))
    list = []
    for i in range(len):
        elem = int(input())
        list.append(elem)
    query = int(input("Enter the query: "))

    print(locate_query(list,query))

def locate_query(list,query):
    position = 0
    while position < len(list):
        if list[position] == query:
            return position
        position += 1

        if position == len(list):
            return -1

if __name__ == "__main__":
    main()
