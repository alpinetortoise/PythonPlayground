# Anagram checker
# ===============

# By Joshua Chubb

def are_anagrams(str1, str2) -> bool:
    anagram_bool = True
    if len(str1) == len(str2):
        anagram_bool = True
        for char in str1.lower():
            if char in str2.lower():
                anagram_bool &= True
            else:
                anagram_bool &= False
    else:
        anagram_bool = False
    return anagram_bool

print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("triangle", "integral"))  # Output: True
print(are_anagrams("apple", "pale"))  # Output: False
