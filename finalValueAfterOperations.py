class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        count=Counter(operations)
        return count["++X"]-count["--X"]+count["X++"]-count["X--"]
