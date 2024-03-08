'''
idea
hashmap = {}
    for each_num in nums:
        if each_num in hashmap:
            hashmap[each_num] += 1
        else:
            hashmap[each_num] = 1
        
    # sort hashmap by each value
    sorted_hashmap = sorted(hashmap.items(), key=lambda(x:x[1]))
    # return first k values in hashmap
    return list(sorted_hashmap.keys())[:k]
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for each_num in nums:
            if each_num in hashmap:
                hashmap[each_num] += 1
            else:
                hashmap[each_num] = 1
            
        # sort hashmap by each value
        sorted_hashmap = sorted(hashmap.items(), key=lambda x:x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_hashmap[i][0])
        # return first k values in hashmap
        return res