#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    string reverseWords(string s)
    {
        char cSubString;
        string outputStr;
        int prev = 0;
        int detect = 0;
        for(int i=0; i < s.length(); i++)
        {
            cSubString = (s.substr(i,1))[0];
            // if ' ' detected, then reverse the word.
            if(cSubString == ' ')
            {
                detect = i;
                for(int j = detect-1; j >= prev; j--)
                {
                    cSubString = (s.substr(j, 1))[0];
                    outputStr += cSubString;
                }
                prev = detect+1;
                outputStr += ' ';
            }
            if(i == s.length()-1)
            {
                detect = i+1;
                for(int j = detect-1; j >= prev; j--)
                {
                    cSubString = (s.substr(j, 1))[0];
                    outputStr += cSubString;
                }
            }
        }
        return outputStr;
    }
};

int main()
{
    Solution solution;
    std::cout << solution.reverseWords("Hello world") << std::endl;
    return 0;
}