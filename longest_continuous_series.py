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
    series_1_start_index = 0
    series_1_len = 1
    series_2_len = 0

    while i < (len(array) - 1):
        if array[i + 1] == (array[i] + 1):
            if (i + 1 == series_1_start_index + series_1_len):
                series_1_len += 1
            else:
                series_2_len += 1
        elif array[i + 1] != (array[i] + 1):
            if series_2_len == 0:
                series_2_start_index = i + 1
                series_2_len += 1
            elif series_2_len > series_1_len:
                series_1_start_index = series_2_start_index
                series_1_len = series_2_len
                series_2_start_index = i + 1
                series_2_len = 1
            elif series_1_len > series_2_len:
                series_2_start_index = i + 1
                series_2_len = 1
        i += 1
    
    if series_1_len > series_2_len:
        longest_continuous_series_start_index = series_1_start_index
        longest_continuous_series_len = series_1_len
    elif series_2_len > series_1_len:
        longest_continuous_series_start_index = series_2_start_index
        longest_continuous_series_len = series_2_len
    elif series_1_len == series_2_len:
        print "There are 2 longest series of the same length. Printing one of them:"
        longest_continuous_series_start_index = series_1_start_index
        longest_continuous_series_len = series_1_len

    longest_continuous_series = []
    s = 0
    while s < longest_continuous_series_len:
        longest_continuous_series.append(array[longest_continuous_series_start_index + s])
        s += 1

    return longest_continuous_series


if __name__ == "__main__":
    main()