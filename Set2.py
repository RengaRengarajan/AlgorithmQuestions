import sys
from typing import List

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def binary_search(sorted_arr: list, start_inx: int, end_inx: int, item):
    """
    Search for the item in the slice of the input sorted array. Return the index of the first element that >= item
    :param sorted_arr:
    :param start_inx: start index (inclusive)
    :param end_inx: end index (non-inclusive)
    :param item:
    :return:
    """

    if sorted_arr is None or len(sorted_arr) < 1 or start_inx < 0 or end_inx <= start_inx or item is None:
        return None

    left_inx = start_inx
    right_inx = end_inx - 1

    while right_inx >= left_inx:
        curr_inx = (left_inx + right_inx) // 2
        if sorted_arr[curr_inx] == item:
            return curr_inx
        elif right_inx == left_inx:
            break
        elif sorted_arr[curr_inx] < item:
            left_inx = curr_inx + 1
        else:
            right_inx = curr_inx
    # if the element is less, return one more than right_inx. This could go out of array
    return right_inx if sorted_arr[right_inx] > item else (right_inx + 1)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def test_binary_search():
    arr = [10, 23, 56, 78, 89, 90, 92, 100]
    tests = [(10,0), (23,1), (56,2), (78,3), (89,4), (90, 5), (92,6), (100, 7), (11,1), (25,2), (77,3),
             (85,4), (95,7), (105, 8), (5,0)]
    l = len(arr)
    print("Input = %r" % arr)
    for x in tests:
        inx = binary_search(arr, 0, l, x[0])
        err = inx != x[1]
        if err:
            print("Item = %d. Inx = %d. Expected = %d. ERROR!" % (x[0], inx, x[1]))
        else:
            print("Item = %d. Inx = %d" % (x[0], inx))


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def median(sorted_arr: list, start_inx: int, end_inx: int):
    """
    Compute the median for a slice of the passed array which is already sorted
    :param sorted_arr: input list
    :param start_inx: start index (inclusive)
    :param end_inx: end index (non-inclusive)
    :return: median value
    """

    if sorted_arr is None or len(sorted_arr) < 1 or start_inx < 0 or end_inx <= start_inx:
        return None

    num_elements = end_inx - start_inx
    mid_point = num_elements // 2

    if num_elements % 2 == 0:
        return (sorted_arr[start_inx + mid_point - 1] + sorted_arr[start_inx + mid_point]) / 2
    else:
        return sorted_arr[start_inx + mid_point]

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             M E D I A N   O F   T W O   S O R T E D   A R R A Y S
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def median_two_arrays_linear(nums1: list, nums2: list):
    """
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
    :param nums1:
    :param nums2:
    :return:
    """
    if nums1 is None or nums2 is None:
        return None
    len1 = len(nums1)
    len2 = len(nums2)
    if len1 == 0 and len2 == 0:
        return None

    """
    
    At any point, the two lists can be in one of the following 6 scenarios.
    (1) Start-2, End-2 -> Both Left of Start-1
    (2) Start-2 -> Left of Start-1. End-2 -> in between Start-1 and End-1 
    (3) Start-2, End-2 -> Both in between Start-1 and End-1
    (4) Start-2 -> in between Start-1 and End-1. End-2 -> Right of End-1
    (5) Start-2, End-2 -> Both Right of End-1
    (6) Start-2 -> Left of Start-1. End-2 -> Right of End-1
      
    """
    s1 = 0
    e1 = len1 - 1
    s2 = 0
    e2 = len2 - 1

    while True:
        len1 = e1 - s1 + 1
        len2 = e2 - s2 + 1
        if len1 <= 0:
            return median(nums2, s2, e2 + 1)
        elif len2 <= 0:
            return median(nums1, s1, e1 + 1)

        a1_first = nums1[s1]
        a1_last = nums1[e1]
        a2_first = nums2[s2]
        a2_last = nums2[e2]

        if a2_first <= a1_first:
            if a2_last <= a1_first:
                # (1) Start-2, End-2 -> Both Left of Start-1
                # we can just append list-1 to list-2 and take the median
                new_list = nums2[s2:e2 + 1] + nums1[s1:e1 + 1]
                return median(new_list, 0, len(new_list))
            elif a2_last <= a1_last:
                # (2) Start-2 -> Left of Start-1. End-2 -> in between Start-1 and End-1
                # eliminate left of nums2 and right of nums1
                s2 += 1
                e1 -= 1
            else:
                # (6) Start-2 -> Left of Start-1. End-2 -> Right of End-1
                # eliminate start and end of nums2
                s2 += 1
                e2 -= 1
        elif a2_first <= a1_last:
            if a2_last <= a1_last:
                # (3) Start-2, End-2 -> Both in between Start-1 and End-1
                # eliminate start and end of nums1
                s1 += 1
                e1 -= 1
            else:
                # (4) Start-2 -> in between Start-1 and End-1. End-2 -> Right of End-1
                # eliminate start of nums1 and end of nums2
                s1 += 1
                e2 -= 1
        else:
            # (5) Start-2, End-2 -> Both Right of End-1
            # we can just append list-2 to list-1 and take the median
            new_list = nums1[s1:e1 + 1] + nums2[s2:e2 + 1]
            return median(new_list, 0, len(new_list))


def median_two_arrays_binary(nums1: list, nums2: list):
    """
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
    :param nums1:
    :param nums2:
    :return:
    """
    if nums1 is None or nums2 is None or (len(nums1) == 0 and len(nums2) == 0):
        return None
    if len(nums1) == 0:
        return median(nums2, 0, len(nums2))
    if len(nums2) == 0:
        return median(nums1, 0, len(nums1))

    if len(nums1) < len(nums2):
        small_ary = nums1
        big_ary = nums2
    else:
        small_ary = nums2
        big_ary = nums1
    total_num = len(nums1) + len(nums2)

    s1 = 0
    e1 = len(small_ary)

    while True:
        # now partition arrays - n1 on small_ary and n2 on big_ary such that n1 + n2 is half the total
        left_n1 = (s1 + e1) // 2
        left_n2 = ((total_num + 1) // 2) - left_n1
        right_n1 = len(small_ary) - left_n1
        right_n2 = len(big_ary) - left_n2
        left_small = -sys.maxsize if left_n1 == 0 else small_ary[left_n1 - 1]
        left_big = -sys.maxsize if left_n2 == 0 else big_ary[left_n2 - 1]
        right_small = +sys.maxsize if right_n1 == 0 else small_ary[left_n1]
        right_big = +sys.maxsize if right_n2 == 0 else big_ary[left_n2]

        if left_small <= right_big and left_big <= right_small:
            # we found the right split
            if (total_num % 2) == 0:
                return (max(left_small, left_big) + min(right_small, right_big)) / 2
            else:
                return max(left_small, left_big)
        elif left_small > right_big:
            # we need to move left on the small array
            e1 = left_n1 - 1
        else:
            # we need to move right on the small array
            s1 = left_n1 + 1



def test_median_two_arrays():
    test_cases = [([1, 3],           [2],              2.0),
                  ([1, 2],           [3, 4],           2.5),
                  ([10, 20, 30],     [1, 2, 3],        6.5),
                  ([10, 20, 30],     [2, 5, 12],       11.0),
                  ([10, 20, 30],     [2, 5, 32],       15.0),
                  ([10],             [6],              8.0),
                  ([20],             [],               20.0),
                  ([],               [12],             12.0),
                  ([12, 24, 36],     [13, 14, 25, 31], 24.0),
                  ([12, 24, 36],     [13, 14, 25, 39], 24.0),
                  ([10, 20, 30, 35], [40, 50, 60],     35.0)
                  ]

    err_count = 0
    for t in test_cases:
        m = median_two_arrays_binary(t[0], t[1])
        if m is None:
            err_count += 1
            print("::::ERROR:::: a1 = %r. a2 = %r. Median = None. Expected Median = %f" % (t[0], t[1], t[2]))
        elif m != t[2]:
            err_count += 1
            print("::::ERROR:::: a1 = %r. a2 = %r. Median = %f. Expected Median = %f" % (t[0], t[1], m, t[2]))
        else:
            print("a1 = %r. a2 = %r. Median = %f." % (t[0], t[1], m))

    if err_count == 0:
        print("ALL TESTS PASSED")
    else:
        print("%d tests FAILED" % err_count)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             COUNT NUMBER OF NEIGHBORS
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def get_neighbors(row_num: int, col_num: int, num_rows: int, num_cols: int):
    result = []
    for row_delta in [-1, 0, 1]:
        new_row_num = row_num + row_delta
        if 0 <= new_row_num < num_rows:
            for col_delta in [-1, 0, 1]:
                new_col_num = col_num + col_delta
                if 0 <= new_col_num < num_cols:
                    if not (row_delta == 0 and col_delta == 0):
                        result.append((new_row_num, new_col_num))
    return result


def count_neighbors(nums: [list]):
    """
    Count neighbors for every element (all possible 8 neighbors)
    If element =1 and neighbors>3 then that element should become 1 else 0
    If elenent=0 and neighbors>2 then tht should become 1 else 0
    :param nums:
    :return:
    """
    num_rows = len(nums)
    num_cols = len(nums[0])

    result = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

    for row_num in range(num_rows):
        for col_num in range(num_cols):
            num_neighbors = 8
            if row_num == 0 or row_num == num_rows - 1:
                num_neighbors -= 3
            if col_num == 0 or col_num == num_cols - 1:
                if row_num == 0 or row_num == num_rows - 1:
                    num_neighbors -= 2
                else:
                    num_neighbors -= 3
            # Now check if the cell has 0 or 1 and update
            if nums[row_num][col_num] == 1:
                result[row_num][col_num] = 1 if num_neighbors > 3 else 0
            else:
                result[row_num][col_num] = 1 if num_neighbors > 2 else 0

    return result


def count_neighbors_2(nums: [list]):
    """
    Count neighbors for every element (all possible 8 neighbors)
    If element =1 and non-zero neighbors>3 then that element should become 1 else 0
    If elenent=0 and non-zero neighbors>2 then tht should become 1 else 0
    :param nums:
    :return:
    """
    num_rows = len(nums)
    num_cols = len(nums[0])

    result = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

    for row_num in range(num_rows):
        for col_num in range(num_cols):
            neighbors = get_neighbors(row_num, col_num, num_rows, num_cols)
            non_zero_count = 0
            for n in neighbors:
                if nums[n[0]][n[1]] == 1:
                    non_zero_count += 1

            # Now check if the cell has 0 or 1 and update
            if nums[row_num][col_num] == 1:
                result[row_num][col_num] = 1 if non_zero_count > 3 else 0
            else:
                result[row_num][col_num] = 1 if non_zero_count > 2 else 0

    return result

def test_count_neighbors_2():
    nums = [[1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0]]
    result = count_neighbors_2(nums)
    print(result)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             1.5   O N E   A W A Y
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def one_away (s1: str, s2: str):
    """
    Modified version of problem 1.5 in Cracking Coding Interviews
    Two strings s1 and s2 are given. This function must check if we can apply exactly one edit to s1 and
    transform it into s2. The edits allowed are insert a character, remove a character, replace a character
    or swap two adjacent characters. The function must return the following values:
    "equal" - s1 and s2 are already equal
    "not possible" - can't change s1 to s2 with only one edit
    "replace c1 c2" - replace char c1 with c2
    "insert c" - insert char c
    "delete c" - delete char c
    "swap c1 c2" - swap two adjacent characters c1 and c2
    EXAMPLES:
    ple, pale -> insert a
    farm, far -> delete m
    abcd, acbd -> swap b c
    pale, kale -> replace p k
    abcd, abcd -> equal
    abcd, acbe -> not possible
    :param s1:
    :param s2:
    :return:
    """

    len_s1 = len(s1)
    len_s2 = len(s2)
    if abs(len_s1 - len_s2) > 1:
        return "not possible"

    if s1 == s2:
        return "equal"

    num_diffs = 0
    result = ''
    if len_s1 == len_s2:
        # onlly REPLACE and SWAP are applicable
        i = 0
        while i < len_s1:
            if s1[i] == s2[i]:
                i += 1
            elif (i != len_s1 - 1) and s1[i + 1] == s2[i] and s1[i] == s2[i + 1]:
                # swap
                num_diffs += 1
                result = "swap %c %c" % (s1[i], s1[i + 1])
                i += 2
            else:
                num_diffs += 1
                result = "replace %c %c" % (s1[i], s2[i])
                i += 1
    elif len_s1 > len_s2:
        # only delete is possible
        i = 0
        while i < len_s2:
            if s2[i] != s1[i]:
                num_diffs += 1
                if num_diffs > 1:
                    break
                result = "delete %c" % s1[i]
                s1 = s1[0:i] + s1[i+1:]     # delete the char
            i += 1
        if num_diffs == 0:
            num_diffs = 1
            result = "delete %c" % s1[-1]

    else:
        # only INSERT applicable
        i = 0
        while i < len_s1:
            if s1[i] != s2[i]:
                num_diffs += 1
                s1 = s1[0:i] + s2[i] + s1[i:]
                result = "insert %c" % s2[i]
            i += 1
        if num_diffs == 0:
            num_diffs = 1
            result = "insert %c" % s2[-1]

    if num_diffs > 1:
        return "not possible"
    else:
        return result


def test_one_away():
    test_cases = [("pale", "pale", "equal"),
                  ("ale", "pale", "insert p"),
                  ("ple", "pale", "insert a"),
                  ("pal", "pale", "insert e"),
                  ("fit", "first", "not possible"),
                  ("find", "kind", "replace f k"),
                  ("cord", "card", "replace o a"),
                  ("data", "date", "replace a e"),
                  ("ofol", "fool", "swap o f"),
                  ("form", "from", "swap o r"),
                  ("firts", "first", "swap t s"),
                  ("forn", "from", "not possible"),
                  ("away", "way", "delete a"),
                  ("runs", "run", "delete s"),
                  ("first", "fist", "delete r"),
                  ("uneven", "even", "not possible"),
                  ("abcde", "cbde", "not possible")]

    err_count = 0
    for t in test_cases:
        m = one_away(t[0], t[1])
        if m != t[2]:
            err_count += 1
            print("::::ERROR:::: s1 = %s. s2 = %r. Returned = %s. Expected = %s" % (t[0], t[1], m, t[2]))
        else:
            print("s1 = %s. s2 = %r. Returned = %r" % (t[0], t[1], m))

    if err_count == 0:
        print("ALL TESTS PASSED")
    else:
        print("%d tests FAILED" % err_count)


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             R I G H T   T R I A N G L E
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def right_triangle(xa:int, ya: int, xb: int, yb: int):
    """
    ABC is a right angled triangle with angle ABC = 90 degrees
    The coordinates of A, B and C are (xa, ya), (xb, yb) and (xc, yc)
    All coordinates are integers
    The points A, B and C are clockwise
    Given the coordinates of A and B, find the coordinates of C for the shortest length of BC possible
    EXAMPLE:
        A = (-2, 3) B = (2, 1) Then C = (1, -1)
        A = (-6, 1) B = (4, 1) Then C = (4, 0)
    :param xa:
    :param ya:
    :param xb:
    :param yb:
    :return: (xc, yc)
    """

    if xb == xa:
        # line 1 is vertical and so line 2 is horizontal
        slope_2 = 0
    elif yb == ya:
        # line 1 is horizontal, so line 2 is vertical
        slope_2 = sys.maxsize
    else:
        slope_1 = (yb - ya) / (xb - xa)
        slope_2 = -1 / slope_1

    # second line passes through B
    # y = mx + c
    c = yb - (slope_2 * xb)
    # equation of second line = y = slope_2 * x + c
    # find integer x, y

    # from point B, when we make a 90 deg right turn, determine if x will increase or decrease
    # if B is above A, right turn will increase x. If B is below A, it will decrease
    # if B and A are horizontal, we need to increment/decrement y depending on xb < xa or xb > xa
    if ya == yb:
        # line 1 is horizontal and line 2 is vertical. Line 2 has equation x = xb
        # if xb > xa then decrease y else increase y
        inc = -1 if xb > xa else 1
        x = xb
        y = yb + inc
        return (x, y,)
    else:
        # line 1 is slanting or vertical. If B is above A, right turn will increase x. If B is below A, it will decrease
        inc = 1 if yb > ya else -1
        begx = xb + inc
        endx = 51 * inc
        for x in range(begx, endx, inc):
            y = slope_2 * x + c
            if int(y) == y:
                return (x, y,)


def test_right_triangle():
    test_cases = [(-2, 3, 2, 1, (1, -1)),
                  (-6, 1, 4, 1, (4, 0))]

    err_count = 0
    for t in test_cases:
        m = right_triangle(t[0], t[1], t[2], t[3])
        if m != t[4]:
            err_count += 1
            print("::::ERROR:::: xa = %d. ya = %d. xb = %d. yb = %d. Returned = %r. Expected = %r" %
                  (t[0], t[1], t[2], t[3], m, t[4]))
        else:
            print("xa = %d. ya = %d. xb = %d. yb = %d. Returned = %r" %
                  (t[0], t[1], t[2], t[3], m))

    if err_count == 0:
        print("ALL TESTS PASSED")
    else:
        print("%d tests FAILED" % err_count)


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             D R O P   M I N I M U M   F O R   A S C E N D I N G
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def drop_to_get_ascending (nums: list):
    """
    You are given an array containing integers
    Each array element can be between -100 to 100, both inclusive
    The array could be as big as 250,000 elements
    Find the minimum number of array elements to be dropped so that the remaining elements are in ascending order
    EXAMPLE:
        [45, 30, 32, 46, 47] -> return 1 as we can drop just 45
        [45, 30, 32, 46, 47, 33, 48, 49] -> return 2 as we can drop just 45 and 33
    :param nums:
    :return: n
    """

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             Leetcode 128. Longest Consecutive Sequence
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def longestConsecutive(nums: List[int]) -> int:
    """
    Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
    Your algorithm should run in O(n) complexity.
    Example:
        Input: [100, 4, 200, 1, 3, 2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    :param nums:
    :return:
    """

    seq_start = dict()
    seq_end = dict()
    already_seen = dict()

    for n in nums:
        # skip if already seen
        if n in already_seen:
            continue
        else:
            already_seen[n] = 1

        # check if n+1 is in seq start
        if (n + 1) in seq_start:
            # add n to the beginning of this sequence
            curr_end = seq_start.pop(n + 1)
            seq_end.pop(curr_end)

            seq_start[n] = curr_end
            seq_end[curr_end] = n

            # now n has been added to the beginning of a sequence. Check if this sequence has to be merged
            # to the end of another sequence
            if (n - 1) in seq_end:
                # append current sequence to the seq found
                merge_start = seq_end.pop(n - 1)
                seq_start[merge_start] = curr_end
                seq_end[curr_end] = merge_start
        elif (n - 1) in seq_end:
            # add n to the end of this sequence
            curr_start = seq_end.pop(n - 1)
            seq_start.pop(curr_start)

            seq_end[n] = curr_start
            seq_start[curr_start] = n

            # now n has been added to the end of a sequence. Check if this sequence has to be merged
            # to the beginning of another sequence
            if (n + 1) in seq_start:
                # prepend current sequence to the seq found
                merge_end = seq_start.pop(n + 1)
                seq_end[merge_end] = curr_start
                seq_start[curr_start] = merge_end

        else:
            # insert this into both start and end seq
            seq_start[n] = n
            seq_end[n] = n

    # now locate the longest sequence
    longest_seq_len = 0
    for k, v in seq_start.items():
        seq_len = v - k + 1
        if seq_len > longest_seq_len:
            longest_seq_len = seq_len

    return longest_seq_len


def test_longestConsecutive():
    test_cases = \
        [([100, 4, 200, 1, 3, 2], 4),
         ([2, 1, 100, 200, 4, 5, 300, 3], 5),
         ([5, 4, 3, 2, 100, 1, 200, 0], 6),
         ([10, 14, 12, 13, 11, 100, 16, 17, 300, 19, 20, 18, 15], 11),
         ([1, 2, 3, 2, 3, 4], 4),
         ([-3, 2, 8, 5, 1, 7, -8, 2, -8, -4, -1, 6, -6, 9, 6, 0, -7, 4, 5, -4, 8, 2, 0, -2, -6, 9, -4, -1], 7)]

    err_count = 0
    for t in test_cases:
        m = longestConsecutive(t[0])
        if m != t[1]:
            err_count += 1
            print("::::ERROR:::: nums = %r. Returned Length = %d. Expected Length = %d" % (t[0], m, t[1]))
        else:
            print("nums = %r. Seq length = %d." % (t[0], m))

    if err_count == 0:
        print("ALL TESTS PASSED")
    else:
        print("%d tests FAILED" % err_count)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             Leetcode 30. Substring with Concatenation of All Words
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def findSubstring(s: str, words: List[str]) -> List[int]:
    """
    You are given a string, s, and a list of words, words, that are all of the same length.
    Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once
    and without any intervening characters.

    Example 1:
        Input:
          s = "barfoothefoobarman",
          words = ["foo","bar"]
        Output: [0,9]
        Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
        The output order does not matter, returning [9,0] is fine too.

    Example 2:
        Input:
          s = "wordgoodgoodgoodbestword",
          words = ["word","good","best","word"]
        Output: []
    :param self:
    :param s:
    :param words:
    :return:
    """

    if s is None or words is None:
        return []

    s_len = len(s)
    num_words = len(words)

    if s_len == 0 or num_words == 0:
        return []

    # all words are assumed to be of same length. No specific validation
    word_length = len(words[0])
    total_word_length = num_words * word_length

    # if length of the string is less than total word length, then there won't be any match
    if s_len < total_word_length:
        return []

    # Now count the number of occurrences of each character in s. Assume s has ASCII chars
    # this will help in finding no match quickly, if the count for any char in s is less that its count in words
    s_char_count = [0] * 128
    for c in s:
        s_char_count[ord(c)] += 1

    # Now process each word
    word_char_count = [0] * 128
    words_dict = dict()
    words_first_char = dict()
    for w in words:
        # note that words might contain duplicates
        words_dict[w] = words_dict.get(w,0) + 1
        first_char = w[0]
        words_first_char[first_char] = words_first_char.get(first_char, 0) + 1
        for c in w:
            word_char_count[ord(c)] += 1

    # now check if for any char its count in s is less than words
    for i in range(128):
        if s_char_count[i] < word_char_count[i]:
            return []

    # the best way to check if concatenated words is a sub-string is to scan the given string
    # we need to start from the beginning of the string and stop at total_word_length from the end

    result = []

    for i in range(s_len - total_word_length + 1):
        if s[i] in words_first_char:
            # there is a chance. now check if all the words are found
            # clear the counts in words_dict
            words_seen_count = dict()
            for w in words_dict:
                words_seen_count[w] = 0
            num_words_to_find = num_words
            for n in range(num_words):
                start_pos = i + (n * word_length)
                end_pos = start_pos + word_length
                sub_str = s[start_pos: end_pos]
                if sub_str not in words_dict:
                    # we can abandon this starting position i
                    continue

                # now increment the count of this word in words_seen_count

                curr_count = words_seen_count[sub_str]
                if curr_count >= words_dict[sub_str]:
                    # we have already seen this word enough number of times
                    continue
                words_seen_count[sub_str] = curr_count + 1

                num_words_to_find -= 1

            # Now check if all the words have been found at this position of i. Add it to result
            if num_words_to_find == 0:
                result.append(i)

    return result


def test_findSubstring():
    test_cases = \
        [("barfoothefoobarman", ["foo","bar"], [0, 9]),
         ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
         ("abcd", ['ab', 'cd', 'ab'], []),
         ("bcdcdeabcxyabxabccdebcdy", ['abc', 'bcd', 'cde'], [0, 14]),
         ("wordgoodgoodgoodbestword", ["word","good","best","good"], [8])]

    err_count = 0
    for t in test_cases:
        m = findSubstring(t[0], t[1])
        if m != t[2]:
            err_count += 1
            print("::::ERROR:::: s = %s. words = %r. Returned = %r. Expected = %r" % (t[0], t[1], m, t[2]))
        else:
            print("s = %s. words = %r. Returned = %r" % (t[0], t[1], m))

    if err_count == 0:
        print("ALL TESTS PASSED")
    else:
        print("%d tests FAILED" % err_count)
