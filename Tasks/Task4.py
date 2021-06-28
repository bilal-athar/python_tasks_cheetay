def maximumMeetings(n, start, end):
    arr = []
    for i in range(len(start)):
        arr.append([start[i], end[i]])

    arr.sort(key=lambda x: x[1])

    lf = -1

    total = 0

    for s, f in arr:
        if s > lf:
            total += 1
            lf = f

    return total


if __name__ == '__main__':
    print("maximum meetings:", maximumMeetings(n=8, start=[75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924],
                                               end=[112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]))
