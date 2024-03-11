class Solution:
    def checkRecord(self, n: int) -> int:
        mod = lambda x : x % (10**9+7)

        absentZero = [1, 1, 0]
        absentOnce = [1, 0, 0]

        for i in range(2, n+1):
            absentZero, absentOnce = \
            [mod(sum(absentZero)), absentZero[0], absentZero[1]], \
            [mod(sum(absentZero+absentOnce)), absentOnce[0], absentOnce[1]]
            # print(absentZero, absentOnce)
        return mod(sum(absentZero+absentOnce))