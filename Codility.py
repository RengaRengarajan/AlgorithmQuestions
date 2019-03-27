import sys
from typing import List
import time

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             Leetcode 5: Longest Palindromic Substring
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def cyclic_rotation(A: List[int], K: int) -> List[int]:
    """
    The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times
    EXAMPLE:
        A = [3, 8, 9, 7, 6]
        K = 3
    the function should return [9, 7, 6, 3, 8]. Three rotations were made:

        [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
        [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
        [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
    For another example, given

        A = [0, 0, 0]
        K = 1
    the function should return [0, 0, 0]

    Given

        A = [1, 2, 3, 4]
        K = 4
    the function should return [1, 2, 3, 4]

    Assume that:

    N and K are integers within the range [0..100];
    each element of array A is an integer within the range [−1,000..1,000].
    In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
    :param A:
    :param K:
    :return:
    """
    if A is None or len(A) == 0 or K <= 0:
        return A

    # rotating k times is easy
    # 1. Split array into (n-K) elements  K elements, where n is the length of the array
    # 2. Reverse each part
    # 3. Reverse the entire array

    len_a = len(A)
    K = K % len_a
    if K == 0:
        return A

    # now K is less than length of array
    # first_part = A[0:len_a - K]
    # second_part = A[len_a - K:]
    # first_part_rev = first_part[::-1]
    # second_part_rev = second_part[::-1]
    # return (first_part[::-1] + second_part[::-1])[::-1]

    return (A[0:len_a - K][::-1] + A[len_a - K:][::-1])[::-1]


def test_cyclic_rotation():
    test_cases = \
        [([3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]),
         ([0, 0, 0], 0, [0, 0, 0]),
         ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
         ([1,2,3,4,5], 6, [5, 1, 2, 3, 4]),
         ([1,2,3,4,5], 0, [1, 2, 3, 4, 5]),
         ([], 5, [])
         ]

    err_count = 0
    start_time = time.clock()
    for t in test_cases:
        m = cyclic_rotation(t[0], t[1])
        if m != t[2]:
            err_count += 1
            print("::::ERROR:::: A = %r. K = %d. Returned = %r. Expected = %r." % (t[0], t[1], m, t[2]))
        else:
            print("A = %r. K = %d. Returned = %r" % (t[0], t[1], m))
        print("-------------")

    if err_count == 0:
        print("ALL TESTS PASSED")
    else:
        print("%d tests FAILED" % err_count)
    end_time = time.clock()
    print("Elapsed Time = %.6f millisecs" % (1000 * (end_time - start_time)))


