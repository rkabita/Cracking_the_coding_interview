'''
String Rotation:Assumeyou have a method isSubstringwhich checks if one word is a substring of another. 
Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to 
isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").



'''

def isSubString(s1, s2):

    if len(s1) != len(s2):
        return False
    concatString = s1 + s1

    if concatString.count(s2)> 0:
        return True
    else: 
        return False


output = isSubString("ABCD", "CDA")


print(output)