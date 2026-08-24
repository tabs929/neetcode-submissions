class Solution:
    def multiply(self, nums1: str, nums2: str) -> str:
        if "0" in [nums1,nums2]:
            return "0"

        res = [0] * (len(nums1)+len(nums2))
        nums1, nums2  = nums1[::-1],nums2[::-1]

        for i1 in range(len(nums1)):
            for i2 in range(len(nums2)):
                digit = int(nums1[i1]) * int(nums2[i2])
                res[i1+i2] += digit
                res[i1+i2+1] += (res[i1+i2]//10)
                res[i1+i2] = res[i1+i2] % 10
        
        res,beg = res[::-1],0

        while beg < len(res) and res[beg] == 0:
            beg+=1
            
        res = map(str,res[beg:])
        return "".join(res)