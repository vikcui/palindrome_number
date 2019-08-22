# author : YANG CUI
"""
Approach: Revert half of the number
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same
backward as forward.
"""

def palindromeNumber(num):
    # if negative or ending with 0 but not 0, its not gonna be a palindrome
    if num < 0 or (num % 10 == 0 and num != 0):
        return False
    # initialize the second half(reverted number) to be 0
    revertedNumber = 0

    # stop only when two parts are equal or revertedNumber
    # larger than num coz its of odd length
    while num > revertedNumber:
        revertedNumber = revertedNumber * 10 + num % 10
        num = num // 10

    # for even length, condition would be num == revertedNumber
    # for odd length, condition would be revertedNumber//10 == num
    if num == revertedNumber or revertedNumber // 10 == num:
        return True
    else:
        return False
