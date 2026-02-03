"""
Solução de: https://leetcode.com/problems/two-sum/

Fazer análise de complexidade em tempo e espaço
"""


class Solution:
    """

    >>> s = Solution()
    >>> s.twoSum([2, 7, 11, 15], 9)
    [0, 1]
    >>> s.twoSum([2, 1, 3, 15], 4)
    [1, 2]
    >>> s.twoSum([2, 1, 2, 15], 4)
    [0, 2]

    linear em memória e também em tempo de execução

    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        idx_dct = {}
        for i, v in enumerate(nums):
            complement = target - v
            if complement in idx_dct:
                return [idx_dct[complement], i]

            idx_dct[v] = i

