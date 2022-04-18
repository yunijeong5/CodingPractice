def longestCommonSubsequence(text1, text2):
      # define table
      # dp[i][j] = length of the longest common subsequence for text1[0...i] and text2[0...j]
      
      # initialization
      # dp[...][0] = 0
      # dp[0][...] = 0. That is, first row and first column of table is 0. (length of common subsequence between some string and an empty string is 0)
      
      # fill 
      # if text1[i] == text2[j], dp[i][j] = dp[i-1][j-1] + 1
      # else, dp[i][j] = max(dp[i][j-1], dp[i-1][j])
      
      # return 
      # dp[len(text1)-1][len(text2)-1]
      
      m = len(text1)
      n = len(text2)
      
      dp = [[0 for i in range(n+1)] for j in range(m+1)]
      
      for i in range(1, m+1):
        for j in range(1, n+1):
          # current character of text1 and text2 matches
          if text1[i-1] == text2[j-1]: # 0 <= i <= m-1, 0 <= j <= n-1
            dp[i][j] = dp[i-1][j-1] + 1
          else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
      return dp[m][n]
            