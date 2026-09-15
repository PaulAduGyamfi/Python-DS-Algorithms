from collections import defaultdict
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Given an array of strings strs, groups the anagrams together. 
    """
    grouped_dict = defaultdict(list)

    for string in strs:
        count = [0] * 26
        for character in string:
            count[ord(character) - ord('a')] += 1
        
        key = tuple(count)
        grouped_dict[key].append(string)

    return list(grouped_dict.values())


def same_groups(a, b):
    """Compare grouped output ignoring order, inside groups and between them."""
    return sorted(sorted(g) for g in a) == sorted(sorted(g) for g in b)

if __name__ == "__main__":
    assert same_groups(
    groupAnagrams(["eat","tea","tan","ate","nat","bat"]),
    [["bat"],["nat","tan"],["ate","eat","tea"]])
    assert same_groups(groupAnagrams([""]), [[""]])
    assert same_groups(groupAnagrams(["a"]), [["a"]])
    print(" 🎉 All tests passed successfully!")