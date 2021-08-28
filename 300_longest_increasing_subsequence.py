def lengthLIS(array):
    dp = [1]*len(array)

    for i in range(1,len(array)):
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[i],dp[j]+1)
    
    return max(dp)


print(lengthLIS([10,9,2,5,3,7,101,18]))
print(lengthLIS([0,1,0,3,2,3]))
print(lengthLIS([7,7,7,7,7,7,7]))
