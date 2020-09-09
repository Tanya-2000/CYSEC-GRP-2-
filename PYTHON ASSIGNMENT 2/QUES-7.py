


def summer_69(arr):
    Sum = 0
    for n in range(0, len(arr)):
        if arr[n] < 6:
            Sum += arr[n]
        elif arr[n] > 9:
            Sum += arr[n]
        else:
            pass

    return Sum
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))