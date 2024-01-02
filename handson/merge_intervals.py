intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

def merge_intervals(intervals):
    '''
    Given a list of intervals, where each interval is represented by a pair of integers [start, end], write a Python function to merge overlapping intervals.
    :param intervals:
    :return:
    '''
    fint = intervals[0]
    x, y = fint[0], fint[1]
    merli=[]
    for i in range(1 ,len(intervals)):
        fint = intervals[i]
        x1,y1 = fint[0],fint[1]
        if x1 in range(y):
            y=y1
            merli.append([x,y1])
        else :
            merli.append([x1,y1])
