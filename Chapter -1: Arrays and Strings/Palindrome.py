'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome. 
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement 
of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)

Solution: In order to solve this, we need to think about the properties of a palindrome. You should write a couple of palindromes down and see if you can notice any patterns.


If a string can be rewritten as a palindrome, then it either

has an even number of characters. Ex. caac a - 2, c - 2
has an odd number of characters, where there's only one character that appears an odd number of times. Ex. cabbbac a - 2, b - 3, c - 2

In other words, a palindrome is a string that can be reversed to produce the same string. That means that either every character has a matching pair, 
or there is only one character that appears an odd number of times (and that character will be placed in the middle of the string for the palindrome).


We can count the number of occurrences of each character with a dictionary. If the counts of each character satisfy our condition, then we return True.


The time complexity is O(n)O(n) and the space complexity is O(n)O(n) 

'''

def checkPermutation(s):
    counts = {}
    for i in s:
        if i == " ":
            continue
        counts[i] = counts.get(i, 0) + 1
    
    hasOdd = False
    
    for value in counts.values():
        if value % 2 == 1:
            if hasOdd:
               # we have more than one char
               # that appears an odd number
              # of times
                return False
            hasOdd = True

    return True



print(checkPermutation("car race"))