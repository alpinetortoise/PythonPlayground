# Anagram checker
# ===============

# By Joshua Chubb

# Check that the letters are the same
def check_letters(str1: str, str2: str):
    letter_bool = True
    for char in str1:
        if char in str2:
            letter_bool &= True
            str2 = eat(str2, str2.find(char))
        else:
            letter_bool &= False
    return letter_bool

def eat(str1: str, index):
    return str1[:index]+str1[index+1:]

def are_anagrams(str1: str, str2: str) -> bool:
    anagram_bool = True
    if len(str1) == len(str2):
        anagram_bool = check_letters(str1.lower(), str2.lower()) and check_letters(str2.lower(), str1.lower())
    else:
        anagram_bool = False
    return anagram_bool

print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("triangle", "integral"))  # Output: True
print(are_anagrams("apple", "palea"))  # Output: False
