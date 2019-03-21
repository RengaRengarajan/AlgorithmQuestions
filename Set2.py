import sys


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