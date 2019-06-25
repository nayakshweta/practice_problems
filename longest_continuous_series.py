# Get the longest  continuous series in the array
# For example, if the array is:
# [1, 2, 3, 6, 7, 11, 12, 13, 14, 15, 16, 1, 7, 4, 5, 21, 22, 23]
# The longest continuous series in it is [11, 12, 13, 14, 15, 16]

def main():
    array = [1, 2, 3, 6, 7, 11, 12, 13, 14, 15, 16, 1, 7, 4, 5, 21, 22, 23]
    series = longest_continuous_series(array)
    print series

def longest_continuous_series(array):
    i = 0
    series_1 = [array[0]]
    series_2 = []

    while i < (len(array) - 1):
        if array[i + 1] == (array[i] + 1):
            if array[i] in series_1:
                series_1.append(array[i + 1])
                l1 = len(series_1)
            elif array[i] in series_2:
                series_2.append(array[i + 1])
                l2 = len(series_2)
        elif array[i + 1] != (array[i] + 1):
            if series_2 == []:
                series_2.append(array[i + 1])
                l2 = len(series_2)
            elif l2 > l1:
                series_1 = series_2
                l1 = len(series_1)
                series_2 = []
                series_2.append(array[i + 1])
                l2 = len(series_2)
            elif l1 > l2:
                series_2 = []
                series_2.append(array[i + 1])
                l2 = len(series_2)
        i += 1
    
    if l1 > l2:
        longest_continuous_series = series_1
    elif l2 > l1:
        longest_continuous_series = series_2
    
    return longest_continuous_series


if __name__ == "__main__":
    main()