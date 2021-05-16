if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    a = max(arr)  # Prints the max elements in the list 
    c = arr.count(a)  # Count the list 
    for i in range(c):
        arr.remove(a)  #  Remove the max elemnet in the list 
        
    print(max(arr))  # Prints the second max element
