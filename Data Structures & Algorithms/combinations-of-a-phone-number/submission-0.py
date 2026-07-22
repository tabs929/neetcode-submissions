class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digits_to_no = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def bactrk(i,currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return

            for c in digits_to_no[digits[i]]:
                bactrk(i+1, currStr+c)
            
        if digits:
            bactrk(0,"")
        
        return res