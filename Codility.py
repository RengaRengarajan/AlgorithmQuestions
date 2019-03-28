import sys
from typing import List
import time

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             Codility: Cyclic Rotation
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


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             Codility: GenomicRangeQuery
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def GenomicRangeQuery(S: str, P: List[int], Q: List[int]) -> List [int]:
    """
    A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the
    types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer.
    Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer
    several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of
    the given DNA sequence?

    The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters.
    There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers.
    The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA
    sequence between positions P[K] and Q[K] (inclusive).

    For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
    The answers to these M = 3 queries are as follows:

    The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors
    are 3 and 2 respectively, so the answer is 2.
    The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
    The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose
    impact factor is 1, so the answer is 1.Given a non-empty string S consisting of N characters and two non-empty
    arrays P and Q consisting of M integers, return an array consisting of M integers specifying the consecutive
    answers to all queries.
    Result array should be returned as an array of integers.
    For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
    the function should return the values [2, 4, 1], as explained above.

    Write an efficient algorithm for the following assumptions:

    N is an integer within the range [1..100,000];
    M is an integer within the range [1..50,000];
    each element of arrays P, Q is an integer within the range [0..N − 1];
    P[K] ≤ Q[K], where 0 ≤ K < M;
    string S consists only of upper-case English letters A, C, G, T.
    :param S:
    :param P:
    :param Q:
    :return:
    """
    if S is None or len(S) == 0 or P is None or Q is None:
        return []
    N = len(S)
    running_count_A = [0] * (N + 1)
    running_count_C = [0] * (N + 1)
    running_count_T = [0] * (N + 1)
    running_count_G = [0] * (N + 1)

    # first build the running counts from the string
    for inx, c in enumerate(S):
        if c == 'A':
            running_count_A[inx + 1] = running_count_A[inx] + 1
            running_count_C[inx + 1] = running_count_C[inx]
            running_count_G[inx + 1] = running_count_G[inx]
            running_count_T[inx + 1] = running_count_T[inx]
        elif c == 'C':
            running_count_A[inx + 1] = running_count_A[inx]
            running_count_C[inx + 1] = running_count_C[inx] + 1
            running_count_G[inx + 1] = running_count_G[inx]
            running_count_T[inx + 1] = running_count_T[inx]
        elif c == 'G':
            running_count_A[inx + 1] = running_count_A[inx]
            running_count_C[inx + 1] = running_count_C[inx]
            running_count_G[inx + 1] = running_count_G[inx] + 1
            running_count_T[inx + 1] = running_count_T[inx]
        else:
            running_count_A[inx + 1] = running_count_A[inx]
            running_count_C[inx + 1] = running_count_C[inx]
            running_count_G[inx + 1] = running_count_G[inx]
            running_count_T[inx + 1] = running_count_T[inx] + 1

    # now process each query
    if len(P) != len(Q):
        raise ValueError("The list sizes of P amd Q are different. len(P) = %d. len(Q) = %d" % (len(p), len(Q)))
    result = [0] * len(P)

    for inx in range(len(P)):
        # note that the running counts are 0 to N (i.e., one more than the string length)
        s = P[inx]        # don't add 1 here
        e = Q[inx] + 1
        if running_count_A[e] - running_count_A[s] > 0:
            result[inx] = 1
        elif running_count_C[e] - running_count_C[s] > 0:
            result[inx] = 2
        elif running_count_G[e] - running_count_G[s] > 0:
            result[inx] = 3
        elif running_count_T[e] - running_count_T[s] > 0:
            result[inx] = 4

    return result


def test_GenomicRangeQuery():
    test_cases = \
        [("CAGCCTA", [2, 5, 0], [4, 5, 6], [2, 4, 1]),
         ("CAGCGGGGGGGGCTA", [2, 5, 0], [4, 5, 6], [2, 3, 1])
         ]

    err_count = 0
    start_time = time.clock()
    for t in test_cases:
        m = GenomicRangeQuery(t[0], t[1], t[2])
        if m != t[3]:
            err_count += 1
            print("::::ERROR:::: S = %s. P = %r. Q = %r. Returned = %r. Expected = %r." % (t[0], t[1], t[2], m, t[3]))
        else:
            print("S = %s. P = %r. Q = %r. Returned = %r" % (t[0], t[1], t[2], m))
        print("-------------")

    if err_count == 0:
        print("ALL TESTS PASSED")
    else:
        print("%d tests FAILED" % err_count)
    end_time = time.clock()
    print("Elapsed Time = %.6f millisecs" % (1000 * (end_time - start_time)))


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             Codility: NumberOfDiscIntersections
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def NumberOfDiscIntersections(A: List[int]) -> int:
    """
    We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers,
    specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].
    We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common
    point (assuming that the discs contain their borders).

    Given an array A describing N discs as explained above, return the number of (unordered) pairs of intersecting
    discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

    Given array A [1, 5, 2, 1, 4, 0], the function should return 11.
    Write an efficient algorithm for the following assumptions:
    N is an integer within the range [0..100,000];
    each element of array A is an integer within the range [0..2,147,483,647].
    :param A:
    :return:
    """

    # An earlier circle with center c1 and radius r1 intersects later circle with center c2 and radius r2 if
    # c1+r1 >= c2-r2. Here c2 > c1

    c_plus_r = [i + v for i, v in enumerate(A)]
    c_minus_r = [i - v for i, v in enumerate(A)]
    N = len(A)

    # sort both arrays
    c_plus_r.sort()
    c_minus_r.sort()

    # Now for every element in c_plus_or count the number of elements in c_minus_r that are greater than or equal
    # Of course, we will be double counting i,j and j,i. And also i,i

    total_intersection = 0
    total_c_minus_r_seen = 0
    cm_inx = 0
    for x in c_plus_r:
        while cm_inx < N and x >= c_minus_r[cm_inx]:
            cm_inx += 1
        total_intersection += cm_inx
        # if the cm_inx had reached end of array, we might miss out the last element. Take care of this
        if cm_inx < N and x >= c_minus_r[cm_inx]:
            total_intersection += 1

    # now subtract the double counting for i,j and j,i
    # the num of such double count will be n*(N+1)/2
    total_intersection -= int((N * (N + 1)) / 2)
    if total_intersection > 10000000:
        total_intersection = -1

    return total_intersection

def test_NumberOfDiscIntersections():
    test_cases = \
        [([1, 5, 2, 1, 4, 0], 11)
         ]

    err_count = 0
    start_time = time.clock()
    for t in test_cases:
        m = NumberOfDiscIntersections(t[0])
        if m != t[1]:
            err_count += 1
            print("::::ERROR:::: A = %r. Returned = %d. Expected = %d." % (t[0], m, t[1]))
        else:
            print("A = %r. Returned = %d" % (t[0], m))
        print("-------------")

    if err_count == 0:
        print("ALL TESTS PASSED")
    else:
        print("%d tests FAILED" % err_count)
    end_time = time.clock()
    print("Elapsed Time = %.6f millisecs" % (1000 * (end_time - start_time)))


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             Codility: NumberOfDiscIntersections
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

