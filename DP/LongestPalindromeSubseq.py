def longestPalindromeSubseq(s):
      # define table (n by n)
      # dp[i][j] : length of the longest palendrome subsequence for s[i...j] for 0 <= i <= j <= len(s)-1
      
      # initialize
      # dp[0][0] = 0
      # dp[i][i] = 1 for 0 <= i <= len(s)-1 --- length 1 palindrome
      # if s[i] != s[i+1], dp[i][i+1] = 1. else, dp[i][i+1] = 2 --- length 2 palindrome
      
      # fill
      # i > j is invalid (below main diagonal)
      # after initialization,
      # dp[n-1][n-1] = 1
      # dp[n-2][n-2] = 1
      # dp[n-2][n-1] = 1 or 2
      # start filling from row n-2. left to right, all the way up to row 1, col n
      # if s[i] = s[j], dp[i][j] = dp[i+1][j-1] + 2
      # else, dp[i][j] = max(dp[i+1][j], dp[i][j-1])
      
      # return dp[0][n-1]
      
      
      # table
      n = len(s)
      dp = [[None for c in range(n)] for r in range(n)]
      
      # initialize
      for i in range(n-1):
        dp[i][i] = 1
        if s[i] == s[i+1]:
          dp[i][i+1] = 2
        else:
          dp[i][i+1] = 1
      dp[n-1][n-1] = 1
      
      # fill
      for i in range(n-3, -1, -1):  # bottom to top
        for j in range(i+2, n):  # left to right
          if s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1] + 2
          else:
            dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            
      # return
      return dp[0][n-1]



longestPalindromeSubseq("bbbab")