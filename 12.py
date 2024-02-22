class Solution:
    def intToRoman(self, num: int) -> str:
        hashtable = {1:'I', 4:'IV', 5:'V', 
                     9:'IX', 10:'X', 40:'IL', 50:'L', 
                     90:'IC', 100:'C', 400:'CD', 500:'D', 
                     900:'CM', 1000:'M'}
        res = ""
        # 1000
        res += "M"* (num//1000)
        num -= num//1000 * 1000
        # 100
        if(num//100 == 9):
            res += "CM"
        elif(num//100==4):
            res += "CD"
        elif(num//100 < 5):
            res += "C"* (num//100)
        elif(num//100 >= 5):
            res += "D"
            res += "C"* ((num-500) // 100)
        num -= num//100 * 100
        # 10
        if(num//10 == 9):
            res += "XC"
        elif(num//10==4):
            res += "XL"
        elif(num//10 < 5):
            res += "X"* (num//10)
        elif(num//10 >= 5):
            res += "L"
            res += "X"* ((num-50) // 10)
        num -= num//10 * 10
        # 1
        if(num == 9):
            res += "IX"
        elif(num==4):
            res += "IV"
        elif(num < 5):
            res += "I"* (num)
        elif(num >= 5):
            res += "V"
            res += "I"* (num-5)
        return res