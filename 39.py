class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        def backtrack(res, obj, sum):
            for i in candidates:
                
                if i+sum > target:
                    return res
                if not obj or obj[-1]<=i:
                    if i+sum < target:
                        backtrack(res,obj+[i], i+sum)
                    else:
                        res.append(obj+[i])
            return res
        return backtrack([],[],0)