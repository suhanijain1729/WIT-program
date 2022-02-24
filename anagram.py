def is_anagram(word, candidate):
    w = word.lower()
    c = candidate.lower()
    return sorted(c) == sorted(w) and c != w
def find_anagrams(word, candidates):
    return [candidate for candidate in candidates if is_anagram(word, candidate)]