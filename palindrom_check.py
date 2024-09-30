from collections import deque


def is_palindrome(input_string: str) -> bool:
    """
    Checks if the given string is a palindrome.

    This function converts the input string to lowercase, removes non-alphanumeric characters, 
    and uses a deque to compare characters from both ends.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned_string = ''.join(char.lower()
                             for char in input_string if char.isalnum())

    # Create a deque from the cleaned string
    char_deque = deque(cleaned_string)

    # Check if the string is a palindrome by comparing characters from both ends
    while len(char_deque) > 1:
        # Compare characters from the front and back
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


# Test cases for validating the palindrome function
test_strings = {
    "A man, a plan, a canal, Panama!": True,  # Palindrome
    "Was it a car or a cat I saw?": True,     # Palindrome
    "No 'x' in Nixon": True,                  # Palindrome
    "Hello, world!": False,                   # Not a palindrome
    "Race car": True,                         # Palindrome
}


def test_is_palindrome():
    """
    Unit test for the is_palindrome function.

    Iterates through the predefined test strings and checks if the 
    function returns the expected results. 
    """
    for string, expected in test_strings.items():
        actual = is_palindrome(string)
        assert actual == expected, (
            f"Expected result for string '{string}' is '{expected}', "
            f"but actual is '{actual}'"
        )
        print(f"String: '{string}' test passed")


# Uncomment to run the test
# test_is_palindrome()
