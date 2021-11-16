'''
Brute Force Solution: The first solution that comes to my mind is two have two for loops and just check if a character repeats or not.
                    Which will take O(n^2) time. 

for i in range(len(string):
    for j in range (i+1, len(string)):
        if string[i]== string [j]:
            return False
       
return true

Optimized Solution: In this way I will just insert every element of the string into a set. Since set doesn't allow duplicates, 
                    If I find one characteralready exists in the set I will just return False.




'''

def UniqueCharacters(string):
    stringSet = set(string)
    
    if len(string) == len(stringSet):
        return True
    return False

#Main Function
output = UniqueCharacters("Cracking the Coding Interview")
print(output)

