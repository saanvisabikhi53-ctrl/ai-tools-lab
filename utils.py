"""A small collection of simple utility functions."""


def is_palindrome(s):
    """Return True if the string reads the same forwards and backwards.

    Ignores upper/lower case, spaces, and punctuation.
    Example: "A man, a plan, a canal: Panama" -> True
    """
    # Keep only letters and numbers, and make them lowercase
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()

    # Compare the cleaned text with its reverse
    return cleaned == cleaned[::-1]


def count_words(text):
    """Return the number of words in the text.

    Words are separated by whitespace (spaces, tabs, or new lines).
    Example: "Hello   world" -> 2
    """
    # split() with no arguments splits on any whitespace
    # and ignores extra spaces
    words = text.split()
    return len(words)


def celsius_to_fahrenheit(c):
    """Convert a temperature from Celsius to Fahrenheit.

    Formula: F = C * 9/5 + 32
    Example: 100 -> 212.0
    """
    return c * 9 / 5 + 32


# Quick tests that run only when you execute this file directly:
#     python utils.py
if __name__ == "__main__":
    print(is_palindrome("racecar"))                         # True
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("hello"))                           # False

    print(count_words("Hello world"))                       # 2
    print(count_words("  Python   is   fun  "))             # 3
    print(count_words(""))                                  # 0

    print(celsius_to_fahrenheit(0))                         # 32.0
    print(celsius_to_fahrenheit(100))                       # 212.0
    print(celsius_to_fahrenheit(-40))                       # -40.0