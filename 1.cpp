#include <iostream>
#include <vector>

class Solution
{
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target)
    {
        bool bFound = false;
        int tobeZero = target;
        std::vector<int> vOutput;
        int i,j;
        for(i=0; i<nums.size(); ++i)
        {
            tobeZero -= nums[i];
            for(j=i+1; j<nums.size(); ++j)
            {
                if(tobeZero == nums[j])
                {
                    bFound = true;
                    break;
                }
            }
            if(bFound == true)
            {
                break;
            }
            else
            {
                tobeZero = target;
            }
        }
        vOutput.push_back(i);
        vOutput.push_back(j);
        return vOutput;
    }
};