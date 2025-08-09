class Solution(object):
    def threeSum(self, nums):
        Nums = sorted(nums)
        res=[]
        for i,a in enumerate(Nums):
            if a > 0:
                break
            if i>0 and a==Nums[i-1]:
                continue
            
            l=i+1
            r=len(Nums)-1
            while l<r:
                threesum = a+Nums[l]+Nums[r]
                if threesum<0:
                    l+=1
                elif threesum>0:
                    r-=1
                else:
                    res.append([a,Nums[l],Nums[r]])
                    l+=1
                    r-=1
                    while Nums[l]==Nums[l-1] and l<r:
                        l+=1
        return res

        
        