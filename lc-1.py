import sys
from typing import List
import time

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             Leetcode 5: Longest Palindromic Substring
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def is_palindrome(s: str) -> bool:
    # checks if the passed string is a is_palindrome
    return s == s[::-1]


def longestPalindrome(s: str) -> str:
    """
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
    Example 1:
        Input: "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.
    Example 2:
        Input: "cbbd"
        Output: "bb"
    :param self:
    :param s:
    :return:
    """

    if s is None or len(s) == 0:
        return ""
    if len(s) == 1:
        return s

    # for each character, note down the positions
    char_positions = dict()
    for i, c in enumerate(s):
        if c in char_positions:
            char_positions[c].append(i)
        else:
            char_positions[c] = [i]

    # Now let's check for each char if it can start a is_palindrome.
    longest_palindrome = s[0]
    longest_palindrome_len = 1
    for c, positions in char_positions.items():
        # For a is_palindrome to start, it should have more than one occurrence of that character
        if len(positions) <= 1:
            continue

        # Now there are more than one occurrence of this character
        # check if any two pair would give a is_palindrome
        for p1, start_pos in enumerate(positions):
            # try from longest to shortest
            for end_pos in positions[-1:p1:-1]:
                substr_len = end_pos - start_pos + 1
                if substr_len < longest_palindrome_len:
                    # now we can break the inner lop as we are searching from the fartheset
                    break

                # check if string is a is_palindrome
                substr = s[start_pos: end_pos + 1]
                if substr == substr[::-1]:
                    # it's a palindrome
                    longest_palindrome = substr
                    longest_palindrome_len = substr_len
                    # now we can break the inner lop as we are searching from the fartheset
                    break

    return longest_palindrome


def test_longestPalindrome():
    test_cases = \
        [("babad", ("bab", "aba")),
         ("cbbd", ("bb,")),
         ("babcdcbabx", ("babcdcbab",)),
         ("aa", ("aa",)),
         ("a", ("a",)),
         ("ac", ("a",)),
         ("abcdefgha", ("a",)),
         ("baaaac", ("aaaa",)),
         ("xabcdadcbabcdefgfedcbabcdatyuyghrewaol", "adcbabcdefgfedcbabcda"),
         ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")]

    err_count = 0
    start_time = time.time()
    for t in test_cases:
        m = longestPalindrome(t[0])
        if m not in t[1]:
            err_count += 1
            print("::::ERROR:::: s = %s. Returned = %s. Expected = %r" % (t[0], m, t[1]))
        else:
            print("s = %s. Returned = %s" % (t[0], m))

    if err_count == 0:
        print("ALL TESTS PASSED")
    else:
        print("%d tests FAILED" % err_count)
    print("Elapsed Time = %.6f millisecs" % (1000 * (time.time() - start_time)))

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             Leetcode
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


