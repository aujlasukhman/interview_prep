def findduplicates(arr):
    n = len(arr)
    for i in range(n):
        arr[arr[i]%n] += n

    print(arr)
    
    for i in range(n):
        if arr[i] >= 2*n:
            print(i)

print(findduplicates([1,2,1,2]))
print(findduplicates([0,0,0,0,0,0,6]))