## [1,2,3,4,5,6] -> [2,4,6,1,3,5]

class Solution:
    def sort(self, unchanged_list):
        res = [0]*len(unchanged_list)
        odd_list = []
        even_list = []

        for i in range(len(unchanged_list)):
            # even
            if i%2==0:
                even_list.append(unchanged_list[i])
            # odd
            else:
                odd_list.append(unchanged_list[i])
        res[:len(odd_list)] = odd_list[:]
        res[len(odd_list):] = even_list[:]
        return res
    
Sol = Solution()
print(Sol.sort([1,2,3,4,5,6]))