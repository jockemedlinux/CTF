def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

print(is_anagram("typhoon", "opython"))  
print(is_anagram("Alice", "Bob"))        
