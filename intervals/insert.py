"""
Insert Interval
Medium

You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. intervals is initially sorted in ascending order by start_i.

You are given another interval newInterval = [start, end].

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

Return intervals after adding newInterval.

Note: Intervals are non-overlapping if they have no common point. For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

Example 1:
Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
Output: [[1,6]]
Explanation: [2,5] overlaps with [1,3] and [4,6], so all three are merged into [1,6].

Example 2:
Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
Output: [[1,2],[3,5],[6,7],[9,10]]
Explanation: [6,7] does not overlap with any existing interval, so it is simply inserted between [3,5] and [9,10].

Constraints:
0 <= intervals.length <= 10000
newInterval.length == intervals[i].length == 2
0 <= start <= end <= 100000
"""
class Solution:
    def insert(self, intervals, newInterval):

        res = []

        for i in range(len(intervals)):

            if (newInterval[1] < intervals[i][0]):
                res.append(newInterval)
                return res + intervals[i:]
            elif (newInterval[0] > intervals[i][1]):
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)

        return res 

intervals1 = [[1,3],[4,6]]
newInterval1 = [2,5]
print(Solution().insert(intervals1, newInterval1))

intervals2 = [[1,2],[3,5],[9,10]]
newInterval2 = [6,7]
print(Solution().insert(intervals2, newInterval2))

intervals3 = [[1,2],[3,5],[9,10]]
newInterval3 = [6,8]
print(Solution().insert(intervals3, newInterval3))

