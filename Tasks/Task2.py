def equilibriumPoint(arr, num):
    total_sum = sum(arr)
    leftsum = 0
    for i, num in enumerate(arr):

        total_sum -= num

        if leftsum == total_sum:
            return arr[i]
        leftsum += num

    return -1


if __name__ == '__main__':
    arrr = [1, 3, 5, 2, 2]
    print("equilibrium number is:", equilibriumPoint(arrr, 5))
