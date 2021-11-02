'''
Cracking the Coding Interview (CTCI) 1.2

Question: The input is two strings. Check if the first string is a permutation of the second string.

My Solution: 1. The input is two strings. Check if the first string is a permutation of the second string.
              will create two dictionary. And add items in it. Compare it with each other. 



'''


def CheckPermutation(s1, s2):
    if len(s1) != len(s2):
        return False  

    checkPerm = { }
    checkPerm2 = { }
    
    for i in s1:
        checkPerm[i]= checkPerm.get(i,0)+1    # O(n)
    for i in s2:
         checkPerm2[i]= checkPerm2.get(i,0)+1  # O(n)

    if checkPerm == checkPerm2:
        return True
    else: 
        return False


# Test Function: 

print (CheckPermutation('    ', 'adcb'))

'''
Time Complexity: O(n)
Space Complexity: O(n)+ O(n) = O(n)

Another Solution: There is an another way to solve this problem. We would create one dictionary for the first 
                  String and then we would compare it with the other string. If we find the same character we
                  we will minus one from the Dictionary. If, we do not find the charater in the dictionary, 
                  we will just return False. At the end we would just check of the whole dictionary is zero,
                  If not we can say the string is not permutation of each other. 

Time complexity: O(n)
Space Complexity: O(n)

'''




