from typing import List
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(list,combinations(range(1,n+1),k)))

s = Solution()
print(s.combine(4,2))
        
        