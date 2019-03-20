import sys
import traceback
from random import *
from MyBinaryTree import BinaryTree as BT
from LinkedList import LinkedList as LS

# cci = Cracking the Coding Interview
# cci_nn is the problem in page nn of the "Cracking the Coding Interview" book
# cci_p_q is the problem in chapter p question p.q in "Cracking the Coding Interview" book

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def npr(s,r):
    # produce all permutations with length r using all characters in s
    n = len(s)
    if r > n:
        return []

    if r == 1:
        return [ch for ch in s]
    
    result = []
    for i in range(0,n):
        s1 = s[i]
        s2 = s[:i]+s[i+1:]
        curr_rslt = npr (s2,r-1)
        for st in curr_rslt:
            result.append(s1 + st)
    return result

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def ncr(s,r):
    # produce all combinations with length r using all characters in s
    n = len(s)
    if r > n:
        return []
    
    if r == 1:
        return [ch for ch in s]
    
    result = []
    for i in range(0,n):
        s1 = s[i]
        s2 = s[i+1:]
        curr_rslt = ncr(s2,r-1)
        for st in curr_rslt:
            result.append (s1 + st)
    return result

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def permute_question_mark(s):
    # A string contains '0', '1' and '?'
    # the '?' can be either '0' or '1'
    # Find all the possible combinations for a given string
    if s.find('?') == -1:
        return [s]
    else:
        result = []
        s1 = s.replace('?', '0', 1)     # replace the first '?' by '0'
        s2 = s.replace('?', '1', 1)     # replace the first '?' by '1'
        result += permute_question_mark(s1)
        result += permute_question_mark(s2)
        return result

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def cci_70(s,b):
    # Given a smaller string s and a bigger string b,
    # find all permutations of the shorter string within the longer one.
    # Print the location of each permutation.
    # Example:
    # s = "abbc"
    # b = "cbabadcbbabbcbabaabccbabc"
    # result =
    # b = "cbabadcbbabbcbabaabccbabc"
    #      ----     ----       ----
    #            ---- ----      ----
    #                  ----
    lens = len(s)
    lenb = len(b)
    if lenb < lens:
        return []
    
    result = []
    perms = npr (s,lens)
    for i in range (0,lenb-lens+1):
        substr = b[i:i+lens];
        if substr in perms:
            result.append(i)
    return result

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def cci_1_1 (s):
    # Determine if a string has unique characters
    # Assume ASCII. Only 128 characters.

    char_found = [False for i in range (0,128)]
    lens = len(s)
    for i in range (0,lens):
        intval = ord (s[i])
        if char_found [intval]:
            return False
        else:
            char_found [intval] = True

    return True

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def cci_1_2 (s1,s2):
    # Given two strings, determine if one is a permutation of the other
    # Assume the strings have only ASCII chars and the comparison is case sensitive and
    # white spaces are significant

    if len (s1) != len (s2):
        return False

    char_count = [0 for i in range (0,127)]
    for c in s1:
        char_count [ord(c)] += 1

    for c in s2:
        char_count [ord(c)] -= 1
        if char_count [ord(c)] < 0:
            return False

    return True

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def cci_1_3 (s,l):
    # URLify: Write a method to replace all spaces in a string with '%20:
    # Assume that the string has sufficient space at the end to hold the additional characters,
    # and the "true" length of the string is given. For example,
    # Input : "Mr John Smith    ", 13
    # Output: "Mr%20John%20Smith"

    # convert string to char array
    inp = list(s)
    lens = len (s)
    
    j = lens - 1
    for k in range (l-1, -1, -1):
        if inp[k] == ' ':
            inp[j] = '0'
            j -= 1
            inp[j] = '2'
            j -=1
            inp[j] = '%'
            j -=1
        else:
            inp[j] = s[k]
            j -=1
    return "".join(inp)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def cci_68 (n):
    # Print all positive integer solutions to the equation a^3 + b^3 = c^3 + d^3 where a,b,c,d <= n
    result = {}
    for a in range(1, n):
        for b in range (a+1,n):
            pair = (a, b)
            a3b3 = a ** 3 + b ** 3
            # check if sum already exists in result
            entry = result.get(a3b3)
            if entry is None:
                entry = [pair]
            else:
                entry.append(pair)

            result[a3b3] = entry

    # for each result list out the pairs if more than one
    for key, value in result.items():
        if len(value) > 1:
            print(value)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def cci_72 (maxnum, numSamples):
    # Numbers are randomly generated and stored into an expanding array.
    # How would you keep track of the median?
    # Probably, we need to maintain two heaps
    # The bigger half is kept in a min heap, such that the smallest element in the bigger half is at the root.
    # The smaller half is kept in a max heap, such that the biggest element of the smaller half is at the root.

    array = []
    for i in range (0,numSamples):
        n = randint (1,maxnum)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def binary_gap (inp: int):
    """
    A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by
    ones at both ends in the binary representation of N.

    For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
    The number 529 has binary representation 1000010001 and contains two binary gaps:
    one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains
    one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.
    The number 32 has binary representation 100000 and has no binary gaps.
    For example, given N = 1041 the function should return 5, because N has binary representation 10000010001
    and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary
    representation '100000' and thus no binary gaps.

    :param inp: input number
    :return: binary gap length
    """

    cur_len = 0
    max_len = 0
    one_seen_before = False
    n = inp
    while n > 0:
        r = n % 2
        n = n // 2
        if r == 1:
            if one_seen_before and max_len < cur_len:
                max_len = cur_len
            cur_len = 0
            one_seen_before = True
        else:
            cur_len += 1

    return max_len

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    
    lens = len(s)
    remLen = lens
    resultLen = 0
    currInx = 0

    while remLen > 0:
        char_inx = [-1] * 128
        currSubstrLen = 0
        fullStringLookedAt = True
        for i in range (currInx,lens):
            currChar = s [i]
            pos = ord(currChar)
            if char_inx [pos] >= 0:
                # char already found
                # don't update the currInx and remLen
                currInx = char_inx [pos] + 1
                remLen = lens - currInx
                fullStringLookedAt = False
                break # the for loop
            else:
                # non-repeating char
                char_inx [pos] = i
                currSubstrLen += 1

        if currSubstrLen > resultLen:
            resultLen = currSubstrLen

        # we can quit if the remaining lenth of the original str is < resultLen
        if (resultLen >= remLen) or fullStringLookedAt:
            break # the while loop

    # return the found sub string
    return resultLen

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def reconstruct_tree_from_in_and_pre(in_list: list, pre_list: list) -> BT:

    # construct the tree given the inorder and preorder lists

    if len(in_list) != len(pre_list):
        raise ValueError("reconstruct_tree_from_in_and_pre:-> Lengths are not identical. In = %d. Pre = %d" %
                         (len(in_list), len(pre_list)))

    if len(in_list) == 0:
        return None

    first_in_pre_list = pre_list[0]
    print("First item in pre-list = %d" % first_in_pre_list)
    inx_in_in_list = in_list.index(first_in_pre_list)

    # now break the in_list into left and right lists
    left_in_list = in_list[0:inx_in_in_list]
    right_in_list = in_list[inx_in_in_list + 1:]
    len_of_left_list = len(left_in_list)
    len_of_right_list = len(right_in_list)
    left_pre_list = pre_list[1: len_of_left_list + 1]
    right_pre_list = pre_list[len_of_left_list + 1:]
    print("Left Sub-Tree in in-list: %r" % left_in_list)
    print("Right Sub-Tree in in-list: %r" % right_in_list)
    print("Left Sub-Tree in pre-list: %r" % left_pre_list)
    print("Right Sub-Tree in pre-list: %r" % right_pre_list)
    print("-----")

    # create the node and the tree
    t = BT()
    t.add_root_node(first_in_pre_list)
    left_subtree = reconstruct_tree_from_in_and_pre(left_in_list, left_pre_list)
    right_subtree = reconstruct_tree_from_in_and_pre(right_in_list, right_pre_list)
    if left_subtree is not None:
        t.add_left_subtree(left_subtree.root)
    if right_subtree is not None:
        t.add_right_subtree(right_subtree.root)
    return t

# ---------------------------------------------------------------------------------------------------------------


def test_construct_tree():
    t = BT()
    n1 = t.add_root_node(1)
    n2 = t.add_left_node(n1, 2)
    n3 = t.add_right_node(n1, 3)
    n4 = t.add_left_node(n2, 4)
    n5 = t.add_left_node(n3, 5)
    n6 = t.add_right_node(n3, 6)
    n7 = t.add_left_node(n4, 7)
    n8 = t.add_right_node(n4, 8)
    n9 = t.add_right_node(n5, 9)
    n10 = t.add_left_node(n6, 10)
    n11 = t.add_right_node(n6, 11)

    in_list = [7, 4, 8, 2, 1, 5, 9, 3, 10, 6, 11]
    pre_list = [1, 2, 4, 7, 8, 3, 5, 9, 6, 10, 11]
    c_t = reconstruct_tree_from_in_and_pre(in_list, pre_list)
    c_t.inorder(c_t.root)
    print('')
    c_t.preorder(c_t.root)
    print('')
    c_t.postorder(c_t.root)
    print('')

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def cci_1_5(s1, s2):
    """
    One Away: There are three types of edits that can be performed on strings:
    insert a character, remove a character, or replace a character. Given two strings, write a function to check if
    they are one edit (or zero edits) away.
    EXAMPLE
    pale, ple -> true
    pale, ale -> true
    pale, pal -> true
    pales, pale -> true
    pale, bale -> true
    pale, bake -> false
    :param s:
    :param l:
    :return:
    """

    len_s1 = len(s1)
    len_s2 = len(s2)
    if abs(len_s1 - len_s2) != 0 and abs(len_s1 - len_s2) != 1:
        return False

    if len_s1 < len_s2:
        short_str = s1
        long_str = s2
    else:
        short_str = s2
        long_str = s1

    num_diffs = 0
    for i, c in enumerate(short_str):
        if len_s1 == len_s2:
            if c != long_str[i]:
                num_diffs += 1
        else:
            if c == long_str[i]:
                pass
            elif c == long_str[i+1]:
                num_diffs = 1
            else:
                return False

    return num_diffs <= 1


def test_cci_1_5():
    s1 = "pale"
    s2 = "pale"
    print("%s, %s -> %r" % (s1, s2, cci_1_5(s1, s2)))
    s1 = "pale"
    s2 = "ple"
    print("%s, %s -> %r" % (s1, s2, cci_1_5(s1, s2)))
    s1 = "pale"
    s2 = "ale"
    print("%s, %s -> %r" % (s1, s2, cci_1_5(s1, s2)))
    s1 = "pal"
    s2 = "pale"
    print("%s, %s -> %r" % (s1, s2, cci_1_5(s1, s2)))
    s1 = "pale"
    s2 = "bale"
    print("%s, %s -> %r" % (s1, s2, cci_1_5(s1, s2)))
    s1 = "pale"
    s2 = "bake"
    print("%s, %s -> %r" % (s1, s2, cci_1_5(s1, s2)))
    s1 = "pla"
    s2 = "pale"
    print("%s, %s -> %r" % (s1, s2, cci_1_5(s1, s2)))
    s1 = "bull"
    s2 = "blu"
    print("%s, %s -> %r" % (s1, s2, cci_1_5(s1, s2)))


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def cci_1_6(s):
    """
    String Compression: Implement a method to perform basic string compression using the counts of repeated
    characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would
    not become smaller than the original string, your method should return the original string. You can assume the
    string has only uppercase and lowercase letters (a - z).
    Hints: #92, # 110

    :param s:
    :return:
    """

    prev_c = ''
    curr_len = 0
    result = []

    for c in s:
        if c == prev_c:
            curr_len += 1
        else:
            if curr_len > 0:
                result.append(prev_c)
                result.append(str(curr_len))
            prev_c = c
            curr_len = 1
    if curr_len > 0:
        result.append(prev_c)
        result.append(str(curr_len))

    c_str = "".join(result)

    return c_str, s if len(s) < len(c_str) else c_str

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def rotate_one_layer (m: [list], layer_num: int):
    # :::::::::::::::: TO BE DONE ----- INCOMPLETE :::::::::::::
    # layer_num is 1 relative
    # number of layers = len(m) + 1 // 2
    num_layers = (len(m) + 1) // 2
    odd_dim = len(m) % 2 == 1

    # coordinates of layer 1 (x1, y1) is (num_layers - 1, num_layers - 1)
    # coordinates of layer 2 (x2, y2) is (x1 - 1, y1 - 1)
    # coordinates of layer n (xn, yn) is (x(n-1) - 1, y(n-1) - 1)
    # for odd dimension, width of layer x is 2x - 1
    # for even dimension, width of layer x is 2x
    # for odd dimension, number of cells in layer l = 8l - 8
    # for even dimension, number of cells in layer l = 8l - 4

    if odd_dim:
        w = (2 * layer_num) - 1
    else:
        w = 2 * layer_num
    start_row = start_col = num_layers - layer_num
    end_row = end_col = start_row + w -1

    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            if ((i != start_row) and (i != end_row)) and ((j != start_col) and (j != end_col)):
                # ignore j values in the middle
                pass
            else:
                print(m[i][j], end=', ')
    print('')

    for j in range(start_col, end_col + 1):
        print(m[start_row][j], end=', ')
    for i in range (start_row + 1, end_row):
        print(m[i][end_col], end=', ')
    for j in range(end_col, start_col - 1, -1):
        print(m[end_row][j], end=', ')
    for i in range (end_row - 1, start_row, -1):
        print(m[i][start_col], end=', ')
    print('')

    # for odd dimensional matrix, layer 1 has only one cell
    if odd_dim and layer_num == 1:
        return


def cci_1_7(m: [list]):
    """
    Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a
    method to rotate the image by 90 degrees. Can you do this in place?
    Hints: #51, #100
    :param m:
    :return:
    """

    # check if matrix is n x n
    if len(m) == 0 or len(m) != len(m[0]):
        return None

    # rotate layer by layer
    # number of layers = len(m) + 1 // 2
    num_layers = (len(m) + 1) // 2

    for i in range(num_layers):
        pass


def test_cci_1_7():
    for i in range(1,6):
        m = [[0] * i for _ in range(i)]
        for j in range(i):
            for k in range(i):
                    m[j][k] = (j * i) + k + 1
        print(m, cci_1_7(m))


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def cci_2_2(k: int):
    # get kth item from the end of a linked list

    # build a random list
    items = [randint(0,99) for _ in range (20)]
    print(items)
    ls = LS()
    ls.insert_list(items)

    return ls.get_kth_from_end(k)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def reverse_int(k: int):
    # reverse an integer which could be -ve, zero or positive
    if k < 0:
        sign = -1
        k = -k
    else:
        sign = +1

    rev = 0
    while k > 0:
        rev = (rev * 10) + (k % 10)
        k = k // 10

    return sign * rev

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def prob_dm_1():
    # Input
    ##{
    #   "Opt":"10",
    #   "Columns":"2",
    #   "Cells":"5",
    #   "Key" : "Key 2",
    #   "Parameters":[
    #      {
    #         "Key1":"Value 1"
    #      },
    #      {
    #         "Key 2":"Value 1, Value 2, Value 3, Value 4, Value 5, Value 6, Value 7, Value 8, Value 9, Value 10,Value 11, Value 12, Value 13, Value 14, Value 15, Value 16, Value 17, Value 18, Value 19, Value 20,"
    #      }
    #]
    #}


    # Use Opt value as the increment counter. i.e. here take every 10th value.
    # Use columns as number of values that need to be extracted. Since columns = 2, you take Value 1 and Value 11
    # Since Key = Key 2, Use data from "Key 2"


    #Expected output
    #"Key 2a": "Value 1, Value 11",
    #"Key 2b": "Value 2, Value 12"

    # My Actual Output
    # {'Key 2a': 'Value 1,Value 11', 'Key 2b': ' Value 2, Value 12', 'Key 2c': ' Value 3, Value 13',
    # 'Key 2d': ' Value 4, Value 14', 'Key 2e': ' Value 5, Value 15', 'Key 2f': ' Value 6, Value 16',
    # 'Key 2g': ' Value 7, Value 17', 'Key 2h': ' Value 8, Value 18', 'Key 2i': ' Value 9, Value 19',
    # 'Key 2j': ' Value 10, Value 20'}

    d = {
        "Opt": "10",
        "Columns": "2",
        "Cells": "5",
        "Key": "Key 2",
        "Parameters": [
            {
                "Key1": "Value 1"
            },
            {
                "Key 2": "Value 1, Value 2, Value 3, Value 4, Value 5, Value 6, Value 7, Value 8, Value 9, "
                         "Value 10,Value 11, Value 12, Value 13, Value 14, Value 15, Value 16, Value 17, "
                         "Value 18, Value 19, Value 20,"
            }
        ]
    }

    try:
        inc_counter = int(d.get("Opt"))
        cols = int(d.get("Columns"))
        key = d.get("Key")
        params = d.get("Parameters")
    except Exception as e:
        print("Exception %s" % e)
        traceback.print_exc()
        return None

    if inc_counter is None or cols is None or key is None or params is None or type(params) is not list:
        return None

    for t in params:
        if type(t) is not dict:
            raise ValueError("One of the elements in Parameters is not a dictionary ")
        if key in t:
            # key is found
            values = t.get(key)
            # values is a comma separated strings
            val_list = values.split(',')
            num_vals = len(val_list)
            out_d = dict()
            num_output_keys = inc_counter
            for i in range (num_output_keys):
                suffix = ord('a') + i
                out_key = key + chr(suffix)
                num_values_for_out_key = num_vals // inc_counter
                out_val_list = []
                for j in range(num_values_for_out_key):
                    out_val_list.append(val_list[i + (j * inc_counter)])

                # now insrt the key value pair
                out_d[out_key] = ','.join(out_val_list)

            return out_d

    return None

# ---------------------------------------------------------------------------------------------------------------

# ------------###
#     main    ###
# ------------###


def main(arg_list=[]):

    num_args = len(sys.argv)


if __name__ in ['main', '__main__']:
    main()
