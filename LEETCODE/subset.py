# Samuel Bauta Oct14 1127a Subset - Backtracking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # how this works is every time we have 2 decisions
        # decision to add another number or not to
       # this will result in all possible subsets
        res = []
        subset = []
        def dfs(i):
            # if it goes out of bounds
            if i >= len(nums):
                # add new subset to list
                res.append(subset.copy())
                return
            # decision to include next number
            subset.append(nums[i])
            dfs(i + 1)

            # decision to NOT include next number
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res

