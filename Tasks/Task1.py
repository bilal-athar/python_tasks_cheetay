def activityselection(start, end, n):
    max_activities = []
    y = 0
    for x in range(n):
        if x == 0:
            max_activities.append(x)
        elif x > 0:
            if start[x] >= end[y]:
                y = x
                max_activities.append(x)
    return "maximum number of activities are: ", len(max_activities)


if __name__ == '__main__':
    s = [1, 3, 2, 5]
    e = [2, 4, 3, 6]
    n = 4
    print(activityselection(s, e, n))

    strt = [2, 1]
    ed = [2, 2]
    num = 2

    print(activityselection(strt, ed, num))
