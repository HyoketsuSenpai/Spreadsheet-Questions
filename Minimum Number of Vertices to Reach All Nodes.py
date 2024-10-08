class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        s = set(range(n))
        for u,v in edges:
            if v in s:
                s.remove(v)
        return s
