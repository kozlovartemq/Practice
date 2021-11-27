if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))       #Filling the 'arr' list with input elements (lists)
        
    k = int(input())
    arr = sorted(arr, key = lambda sortedby: sortedby[k]) # Sorting the list by k element [0:M-1]
    for i in range(n):
        print(*arr[i])                                    # Unpacking and printing sorted elements
