'''
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than 
the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).


We can solve this problem by iterating through the string and counting the occurrences of each letter. 
As we count the occurences, we keep a separate array where we append the letter and the number of times it occurs. 
At the end, we can just convert that array to a string and return either the compressed array or the original string 
(whichever one is shorter).

Remember that strings are immutable in Python, so when we're building the compressed string, we must do so with a list. 
After building the compressed string, we can then convert it to a string.

'''




1 def stringCompression(s):
2    compressedString = []
3    cur = s[0]
4    counter = 1
5    for l in s[1:]:
6        if l == cur:
7            counter += 1
8        else:
9            compressedString.append(cur)
10            compressedString.append(str(counter))
11            cur = l
12            counter = 1
13    compressedString.append(cur)
14    compressedString.append(str(counter))
15    compressedString = "".join(compressedString)
16
17    if len(compressedString) < len(s):
18        return compressedString
19    else:
20        return s




Algorithm
Pick the first character from the input string (str).

Append it to the compressed string.

Count the number of subsequent occurrences of the character (in str) and append the count to the compressed string if it is more than 1 only​.

Pick the next character and repeat the steps above until the end of str is reached.




ind = 0

def gen_compressed_str(string):
  global ind
  comp_str = ""
  len_str = len(string)
  while (ind != len_str):
    count = 1

    while ((ind < (len_str-1)) and (string[ind] == string[ind+1])):
      count = count + 1
      ind = ind + 1


    if (count == 1):
      comp_str = comp_str + str(string[ind])
    else:
      comp_str = comp_str + str(string[ind]) + str(count)
    
    ind = ind + 1

  return comp_str
      


string = "wwwwaaadexxxxxxywww"
print gen_compressed_str(string)  