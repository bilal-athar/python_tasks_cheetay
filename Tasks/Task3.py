def findLongestSubstring(string):
    n = len(string)

    st = 0
    maxlen = 0

    start = 0

    pos = {}

    pos[string[0]] = 0

    for i in range(1, n):
        if string[i] not in pos:
            pos[string[i]] = i

        else:
            if pos[string[i]] >= st:

                currlen = i - st
                if maxlen < currlen:
                    maxlen = currlen
                    start = st

                st = pos[string[i]] + 1

            pos[string[i]] = i

    if maxlen < i - st:
        maxlen = i - st
        start = st

    substring = string[start: start + maxlen]
    length = maxlen
    return length, substring


if __name__ == "__main__":
    string = "GEEKSFORGEEKS"
    result = findLongestSubstring(string)
    print("The length of non repeating substring is ", result[0], "and the substring is", result[1])
