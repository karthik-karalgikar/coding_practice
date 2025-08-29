'''
Question = 
Maximum Number of Non-Overlapping Intervals
Given an array of intervals where each interval has a start and end time, 
return the maximum number of non-overlapping intervals.

Example 1

Input:

meetings = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output:

3
Explanation:

Step 1: Sort meetings by end time → [[1,2],[2,3],[1,3],[3,4]].
Step 2: Select [1,2] (count=1, last_end=2).
Step 3: [2,3] has start 2 ≥ 2, select (count=2, last_end=3).
Step 4: [1,3] start 1 < 3, skip.
Step 5: [3,4] start 3 ≥ 3, select (count=3). Result = 3.
'''

def maximizeNonOverlappingMeetings(meetings):
    meetings.sort(key=lambda x:x[1])

    start = meetings[0][0]
    last_end = meetings[0][1]
    count = 1
    
    for i in range(1, len(meetings)):
        if meetings[i][0] >= last_end:
            start = meetings[i][0]
            last_end = meetings[i][1]
            count = count + 1
                
    return count

print(maximizeNonOverlappingMeetings(meetings= [[1, 2], [2, 3], [3, 4], [1, 3]]))

'''
TRACING - 

meetings= [[1, 2], [2, 3], [3, 4], [1, 3]]

meetings.sort(key=lambda x : x[1])
This means that we are sorting the array according to the second element of each sub-element of the array. 

Like, suppose I did only meetings.sort(), then it becomes ->
[[1, 2], [1, 3], [2, 3], [3, 4]]

But here, we will not get the result if we do this because, suppose there is an array [1, 10], 
so the last_end will be initialzed to 10 and it will never pass the if condition and hence we will not get the right 
answer.

So, we use lamdba to sort the array according to the end times ->
x[1] says that it will look at the second element of the sub-element and sort according to that.

meetings = [[1, 2], [2, 3], [1, 3], [3, 4]]

start = meetings[0][0]
start = 1
last_end = meetings[0][1]
last_end = 2
count = 1

for i in range(1, len(meetings)):
    -> i = 1, until 3 (len(meetings) = 4)
    if meetings[i][0] >= last_end:
    -> meetings[1][0] >= 2 -> 2 >= 2 -> True
        start = meetings[i][0]
        start = 2

        last_end = meetings[i][1]
        last_end = 3

        count = count + 1
        count = 2

    -> i = 2
    if meetings[i][0] >= last_end:
    -> meetings[2][0] >= 3 -> 1 >= 3 -> False

    -> i = 3
    if meetings[i][0] >= last_end:
    -> meetings[3][0] >= 3 -> 3 >= 3 -> True
        start = meetings[i][0]
        start = 3

        last_end = meetings[i][1]
        last_end = 4

        count = count + 1
        count = 3

Output = 3


'''