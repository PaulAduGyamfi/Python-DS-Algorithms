def isValidParentheses(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', returns true if the input string is valid.

    An input string is valid if:
    * Open brackets must be closed by the same type of brackets.
    * Open brackets must be closed in the correct order.
    * Every close bracket has a corresponding open bracket of the same type.
    """

    mapping = {")":"(", "}":"{", "]":"["}
    stack = []

    for char in s:
        if char in mapping:
            if mapping[char] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)        
    return True if not stack else False

if __name__ == "__main__":
    assert isValidParentheses("()[]{}") == True
    assert isValidParentheses("(]") == False
    assert isValidParentheses("([])") == True
    assert isValidParentheses("([)]") == False
    print(" 🎉 All tests passed successfully!")