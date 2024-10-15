# Samuel Bauta Oct 15 404p ComboSum - Backtracking
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            # if we go out of bounds or if the total is too big
            if i >= len(nums) or total > target:
                return
            subset.append(nums[i])
            # adding duplicate of the number
            dfs(i, subset, total + nums[i])
            subset.pop()
            # adding the next number instead
            dfs(i + 1, subset, total)
        # start off at beginning, empty subset, zero total
        dfs(0, [], 0)
        return res
