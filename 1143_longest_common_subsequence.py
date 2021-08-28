def longestCommonSubsequence(text1: str, text2: str) -> int:
        
        
        m = len(text1)
        n = len(text2)
        if m < n:
            return longestCommonSubsequence(text2,text1)
        
        dp = [0 for i in range(n+1)]
        prevrowcol = 0
        prevrow = 0
        
        for i in range(m):
            prevrowcol = 0 #gotta renew them at 0 since every new row will be zero
            prevrow = 0
            for j in range(n):
                prevrowcol = prevrow #  since they are lost as we update the new columns
                prevrow = dp[j+1]   #   same reason
                if text1[i] == text2[j]:
                    dp[j+1] = prevrowcol + 1
                else:
                    dp[j+1] = max(dp[j],prevrow,prevrowcol)
                    
        return dp[-1]
                    
                
        ''' runtime = O(m*n) space = O(min(m,n))     '''   
        
        # m = len(text1) + 1
        # n = len(text2) + 1
        # creating a m*n matrix for 'edit distance'        
#         dp = [[0 for col in range(len(text2)+1)] for row in range(len(text1)+1)]
#         for i in range(len(text1)):
#             for j in range(len(text2)):
#                 if text1[i] == text2[j]:
#                     dp[i+1][j+1] = dp[i][j] + 1
#                 else:
#                     dp[i+1][j+1] = max(dp[i][j],dp[i][j+1],dp[i+1][j])
                        
#         return dp[len(text1)][len(text2)]
'''         runtime = O(m*n) space = O(m*n) '''


print(longestCommonSubsequence("bsbininm","jmjkbkjkv"))
print(longestCommonSubsequence("abcde","ace"))