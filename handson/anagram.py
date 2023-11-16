

def are_anagrams(str1,str2) :
    '''
    Write a Python function called are_anagrams(str1: str, str2: str) -> bool that takes two strings as input and returns True if they are anagrams of each other, and False otherwise.
    :param str1:
    :param str2:
    :return:
    '''
    chlist = [c for c in str1.lower() if c.isalnum()]
    for e in chlist :
        if (str2.lower()).find(e) == -1 :
            return False
    return True



result1 = are_anagrams("Listen", "silent")
result2 = are_anagrams("Debit card", "Bad credit")
result3 = are_anagrams("Dormitory", "dirty room##")
result4 = are_anagrams("Hello", "World")

print(result1)  # True
print(result2)  # True
print(result3)  # True
print(result4)  # False