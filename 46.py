class Solution:
    def permute(self, nums):
        def recur(index, output):

            ## if reached the deepest depth
            if index == M-1:
                output.append(res)
                return output
            
            ## else
            for i in range(0, N):
                if check[i] == False:
                    check[i] = True
                    res.append(nums[i])
                    recur(i, output)

        N = max(nums)
        M = len(nums)
        res = []
        check = [False] * (N+1)
        output = []
        # continuous list

        output = recur(0, output)
        return output
    

nums = [1,2,3]
sol = Solution()
print(sol.permute(nums))