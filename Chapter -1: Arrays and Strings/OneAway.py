'''
Let the input strings be s1 and s2 and lengths of input 
strings be m and n respectively.

1) If difference between m an n is more than 1, 
     return false.
2) Initialize count of edits as 0.
3) Start traversing both strings from first character.
    a) If current characters don't match, then
       (i)   Increment count of edits
       (ii)  If count becomes more than 1, return false
       (iii) If length of one string is more, then only
             possible  edit is to remove a character.
             Therefore, move ahead in larger string.
       (iv)  If length is same, then only possible edit
             is to  change a character. Therefore, move
             ahead in both strings. 
    b) Else, move ahead in both strings. 



'''

def isEditDistanceOne(s1, s2):
 
    # Find lengths of given strings
    m = len(s1)
    n = len(s2)
 
    # If difference between lengths is more than 1,
    # then strings can't be at one distance
    if abs(m - n) > 1:
        return false
 
    count = 0    # Count of isEditDistanceOne
 
    i = 0
    j = 0
    while i < m and j < n:
        # If current characters dont match
        if s1[i] != s2[j]:
            if count == 1:
                return false
 
            # If length of one string is
            # more, then only possible edit
            # is to remove a character
            if m > n:
                i+=1
            elif m < n:
                j+=1
            else:    # If lengths of both strings is same
                i+=1
                j+=1
 
            # Increment count of edits
            count+=1
 
        else:    # if current characters match
            i+=1
            j+=1
 
    # if last character is extra in any string
    if i < m or j < n:
        count+=1
 
    return count == 1
 
# Driver program
s1 = "gfg"
s2 = "gf"
if isEditDistanceOne(s1, s2):
    print "Yes"
else:
    print "No"
 
 



