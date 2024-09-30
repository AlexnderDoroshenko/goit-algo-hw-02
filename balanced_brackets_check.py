def are_brackets_balanced(input_string: str) -> bool:
    """
    Function to check if the brackets in the given string are balanced.

    Args:
        input_string (str): The input string containing various types of brackets.

    Returns:
        bool: True if the brackets are balanced, False otherwise.
    """
    # Mapping of closing to opening brackets
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    stack = []  # Stack to store opening brackets

    for char in input_string:
        # If the character is an opening bracket, add it to the stack
        if char in bracket_pairs.values():
            stack.append(char)
        # If the character is a closing bracket
        elif char in bracket_pairs:
            # If the stack is empty or the last element does not match the current bracket
            if not stack or stack.pop() != bracket_pairs[char]:
                return False

    # Check if the stack is empty (all brackets are closed)
    return len(stack) == 0


# Test cases for validation
test_brackets = {
    "( ){[ 1 ]( 1 + 3 )( ){ }}": True,  # Symmetrical
    "( 23 ( 2 - 3);": False,  # Asymmetrical
    "( 11 }": False,  # Asymmetrical
}


def test_are_brackets_balanced():
    """
    Unit test for the are_brackets_balanced function.

    Runs through predefined test cases and checks for expected results.
    """
    for brackets, expected in test_brackets.items():
        result = are_brackets_balanced(brackets)
        assert expected == result, f"Expected result is {
            expected}, but actual is {result}"
        print(f"Test for string '{brackets}' passed")


# Uncomment to run the test
test_are_brackets_balanced()
