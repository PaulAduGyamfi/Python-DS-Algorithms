def isPalindrome(s: str) -> bool:
    """
    Given a string s, return true if it is a palindrome, or false otherwise.
    """

    left_pointer = 0
    right_pointer = len(s) - 1

    while left_pointer < right_pointer:
        if not isalnum(s[left_pointer]):
            left_pointer += 1
            continue

        if not isalnum(s[right_pointer]):
            right_pointer -= 1
            continue

        if s[left_pointer].lower() != s[right_pointer].lower():
            return False

        left_pointer += 1
        right_pointer -= 1

    return True

def isalnum(ch: str):
    """
    Given a character ch, return true if it is an alphanumeric character and false otherwise
    """
    return (ord('a') <= ord(ch) <= ord('z')) or (ord('A') <= ord(ch) <= ord('Z')) or (ord('0') <= ord(ch) <= ord('9'))


if __name__ == "__main__":
    assert isPalindrome("A man, a plan, a canal: Panama") == True
    assert isPalindrome("race a car") == False
    assert isPalindrome("" "") == True
    print(" 🎉 All tests passed successfully!")