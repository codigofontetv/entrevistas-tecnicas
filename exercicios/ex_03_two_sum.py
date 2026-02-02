"""
Solução de: https://leetcode.com/problems/two-sum/

Fazer análise de complexidade em tempo e espaço
"""


class Solution:
    """
    >>> s = Solution()
    >>> s.twoSum([2, 7, 11, 15] , 9)
    [0, 1]

    Solução quadrática para tempo de execução
    Solução constante em tempo de memória
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
