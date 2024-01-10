class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        j=0
        intervals.sort()
        while j<len(intervals)-1:

            if intervals[j][-1]>=intervals[j+1][0] and intervals[j][0]<=intervals[j+1][0] and intervals[j][-1]<=intervals[j+1][-1] :
                intervals[j+1].pop(0)
                intervals[j+1].insert(0,intervals[j][0])
                intervals.pop(j)
                j=0
            elif intervals[j][0]<=intervals[j+1][0] and intervals[j][-1]>=intervals[j+1][-1]:
                intervals.pop(j+1)
                j=0
            elif intervals[j][0]>=intervals[j+1][0] and intervals[j][-1]>=intervals[j+1][-1]:
                intervals[j].pop(0)
                intervals[j].insert(0,intervals[j+1][0])
                intervals.pop(j+1)
                j=0
            elif intervals[j][0]>=intervals[j+1][0] and intervals[j][-1]<=intervals[j+1][-1]:
                intervals.pop(j)
                j=0
            elif (intervals[j][0]==intervals[j][1] or intervals[j+1][0]==intervals[j+1][1]) and (intervals[j][0]!=intervals[j+1][0] and intervals[j][-1]!=intervals[j+1][-1]):
                j+=1
            else:
                j+=1
        return intervals
                