class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        i=0
        j=len(height)-1
        while i!=j:
            ans=min(height[i],height[j])*(j-i) if min(height[i],height[j])*(j-i)>ans else ans
            if height[j]>height[i]:
                i+=1
            elif height[i]>=height[j]:
                j-=1
        return ans  
                
        # Time Limit Exceeds
        # ans=0
        # for i in range(len(height)-1):
        #     for j in range(i+1,len(height)):
        #         ans=min(height[i],height[j])*(j-i) if min(height[i],height[j])*(j-i)>ans else ans
        #         # ans.append(min(height[i],height[j])*(j-i))
        # print(len(height))
        # return (ans)