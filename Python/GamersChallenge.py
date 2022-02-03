##You are given a string S of length N consisting of characters 'a' and 'b' with additional empty gaps represented by '?'. Your task is to replace every such gap
##with either an 'a' character or a 'b' character so that the longest fragment of S, consisting only of 'a' characters or 'b' characters, is as short as possible.
##
##For example, for S = "aa??bbb", if you replace "??" with "aa", the longest fragment consisting of equal characters will have length 4: "aaaabbb". You can obtain
##a better result by replacing "??" with "ba", resulting in "aababbb". Then the longest fragment consisting of equal characters will have length 3.
##
##Write a function:
##
##def solution(S)
##
##that, given a string S of length N, returns the minimum possible length of the longest fragment of S consisting of equal characters after replacing all "?" characters with letters.
##
##Examples:
##
##1. Given S = "aa??bbb", your function should return 3, as explained above.
##
##2. Given S = "a?b?aa?b?a", your function should return 2. Question marks can be replaced in the following way: "aabbaabbaa".
##
##3. Given S = "??b??", your function should return 1.
##
##4. Given S = "aa?b?aa", your function should return 3.
##
##Write an efficient algorithm for the following assumptions:
##
##string S consists only of the following characters: "a", "b" and/or "?";
##N is an integer within the range [1..100,000].
##Copyright 2009–2022 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
##
## TEST IT in the CODILITY ENVIRONMENT since it has the test inputs, or write code to read such inputs!!!!

## SOLUTION

def fragments(S):
    i = 0
    while i < len(S):
        d = 1
        ## while in the string and reading the same letters as the first letter of the fragment, then increase the length
        while i+d < len(S) and S[i+d] == S[i]:
            d += 1
        ## if the 1st letter was not ? then i will return the fragment using the Python construct 'yield' -> yes i have another element to generate
        ## and the generator will be stopped here when the next element is requested by the function that called the generator
        if S[i] != '?':
            yield (i, d)
        i += d
             
def solution(S):
    S = list(S) ## change string to list of of letter, because strings are immutable in Python, and we need to change it, so make it a list
    answer = 1; ## longest fragment assumes 1, initially

    for i, d in fragments(S):
        answer = max(answer, d)

    for i, d in fragments(S):
        if d == answer:
            other = 'a' if S[i] == 'b' else 'b' ## this variable "other" is an a if my current position is b else put b
            ## if we are not at the end of the word and at the next position we have ? then we fill the letter with "other"
            if i+d < len(S) and S[i+d] == "?":
                S[i+d] = other

    ##recalculate the length of the longest fragment, because the added letters may have created a longer fragment (of size k+1)
    for i, d in fragments(S):
        answer = max(answer, d)

    return answer


        
