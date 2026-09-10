def isAnagram(s: str, t:str) -> bool:
    """
    A function that returns true if both strings are anagrams of each other
    """
    lookup = {}

    if len(s) != len(t):
        return False
    
    for ch in s:
        if ch in lookup:
            lookup[ch] += 1
        else:
            lookup[ch] = 1
    
    for ch in t:
        if ch in lookup:
            if lookup[ch] == 0:
                return False
            lookup[ch] -= 1
        else:
            return False
    return True

if __name__ == "__main__":
    assert isAnagram("racecar", "cacearr") == True
    assert isAnagram("rt", "ttr") == False
    assert isAnagram("", "") == True
    print(" 🎉 All tests passed successfully!")