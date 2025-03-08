class Solution:
    def maximumSwap(self, num: int) -> int:
        right_most = [-1 for _ in range(10)]
        n = list(str(num))

        for i, dig in enumerate(n):
            right_most[int(dig)] = i

        for i, dig in enumerate(n):
            for j in range(9, int(dig), -1):
                if right_most[j] > i:
                    n[right_most[j]], n[i] = n[i], n[right_most[j]]
                    return int("".join(n))

        return num
