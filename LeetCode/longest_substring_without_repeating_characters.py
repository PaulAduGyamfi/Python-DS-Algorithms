def lengthOfLongestSubstring(s: str) -> int:
    left_pointer = 0
    longest_length = 0
    seen = set()

    for right_pointer in range(len(s)):
        while s[right_pointer] in seen:
            seen.remove(s[right_pointer])
            left_pointer += 1

        seen.add(s[right_pointer])
        longest_length = max(longest_length, (right_pointer - left_pointer)+1)
    return longest_length

if __name__ == "__main__":
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbb") == 1
    assert lengthOfLongestSubstring("abababjkuyt") == 7
    assert lengthOfLongestSubstring("") == 0
    print(" 🎉 All tests passed successfully!")