##There are N stacks of coins, numbered from 0 to N−1. The Kth stack has A[K] coins. In one move we can pick two coins from any stack we choose, put the
##first coin away and place the second coin on the adjacent stack (either to the left or to the right of the original stack).
##
##What is the maximum number of coins that can be accumulated in a single stack?
##
##Write a function:
##
##def solution(A)
##
##that, given an array A of N integers, recording the heights of the stacks, returns the maximum number of coins that can be accumulated in one stack after
##performing any number of moves as described above.
##
##Examples:
##
##1. Given A = [2, 3, 1, 3], the function should return 5. A possible sequence of moves is: [2, 3, 1, 3] → [0, 4, 1, 3] → [0, 4, 2, 1] → [0, 5, 0, 1].
##
##2. Given A = [3, 7, 0, 5], the function should return 9. A possible sequence of moves is: [3, 7, 0, 5] → [1, 8, 0, 5] → [1, 8, 1, 3] → [1, 8, 2, 1] → [1, 9, 0, 1].
##
##3. Given A = [1, 1, 1, 1, 1], the function should return 1. No move can be performed.
##
##Write an efficient algorithm for the following assumptions:
##
##N is an integer within the range [1..200,000];
##each element of array A is an integer within the range [0..100,000,000].
##Copyright 2009–2022 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
##
## TEST IT in the CODILITY ENVIRONMENT since it has the test inputs, or write code to read such inputs!!!!

## SOLUTION

def calc(A):
    coins = 0 ##number of coins we can move from current stack
    for a in A:
        coins = (coins + a) // 2
    return coins
        

def solution(A):
    answer = 0
    ##loop over all candidates where we can accumulate coins
    for i in range(len(A)):
        left = A[:i]
        right = A[i+1:]
        ## calc function will assume that we take the coins from left to right, so we need to reverse "right"
        coins = calc(left) + A[i] + calc(right[::-1])
        answer = max(answer, coins)

    return answer

