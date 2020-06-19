#python script to insert an interval into a list of non-overlappig intervals
def insertIntervals(intervals, newIntervals): 
    #create a central stack to hold the value of both intervals and newInterval
    stack = []
    #extracting the first and last element in the new intervals
    start, end = newIntervals
    #loop through the intervals and append the element into the list
    for i, j in intervals:
        #the first element of each intervals in the intervals list would be appended and followed by a 1
        #the final element of each intevrvals in the intervals list would be followed by a -1
        stack.append((i, 1))
        stack.append((j, -1))
    
    #appending newIntervals value into the stack:
    stack.append((start, 1))
    stack.append((end, -1))
    #sort the stack to make it easy to work on: 
    stack.sort(key=lambda k:(k[0], -k[1]))

    # =====> stack = [1,1,2,1,3,-1]
    #another stack to hold the final answer
    answer = []
    currentCounter = 0
    upperbound = 0
    #within or outside of each intervals
    for lowerbound, outside in stack:
        #we are working inside an interval
        if currentCounter == 0 and outside == 1:
            upperbound = lowerbound
        #we are outside of an interval, aka, we are done checking an intervals
        if currentCounter == 1 and outside == -1:
            answer.append((upperbound, lowerbound))
        currentCounter += outside
    assert currentCounter == 0
    return answer

    
intervals = [[1,3],[6,9]]
newInterval = [2, 5]

print(insertIntervals(intervals, newInterval))









