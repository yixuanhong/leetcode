class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        share = 0  # 当前可传播人数

        for day in range(2, n + 1):
            # 新进入可传播窗口
            if day - delay >= 1:
                share = (share + dp[day - delay]) % MOD
            # 今天忘记、退出传播窗口
            if day - forget >= 1:
                share = (share - dp[day - forget]) % MOD
            # 今天新知道的人数 == 今天被传播到的人数
            dp[day] = share

        # 仍记得秘密的人：最近 forget-1 天内新知道的总和
        start = max(1, n - forget + 1)
        return sum(dp[start:n + 1]) % MOD
