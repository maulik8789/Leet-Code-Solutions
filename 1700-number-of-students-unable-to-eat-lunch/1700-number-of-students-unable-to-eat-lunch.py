class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt=[0,0]
        rem=len(sandwiches)
        for i in students:
            
            cnt[i]+=1
            
            # rem-=1
        print(cnt)
        for i in sandwiches:
            if cnt[i]==0:
                break
            rem-=1
            cnt[i]-=1
        return rem