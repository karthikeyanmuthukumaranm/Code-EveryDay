def are_anagram(str1,str2):
    str1.replace(" ","").lower()
    str2.replace(" ","").lower()

    return sorted(str1)==sorted(str2)
str1='listen'
str2='silent'

if are_anagram(str1,str2):
    print("The two strings are anagram")
else:
    print("The two strings are not anagram")