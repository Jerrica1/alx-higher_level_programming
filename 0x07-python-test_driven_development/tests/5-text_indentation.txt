#!/usr/bin/python3

"""Defines a text-indentation function."""

def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """

    # Check that the input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Skip over any leading whitespace
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    # Loop over the characters in the input string
    while c < len(text):
        # Print the current character without a newline
        print(text[c], end="")

        # Check if we need to add newlines
        if text[c] == "\n" or text[c] in ".?:":
            # If the character is one of '.', '?', or ':', add two newlines
            if text[c] in ".?:":
                print("\n")
            print("\n")

            # Skip over any leading whitespace in the next line
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1

            # Continue to the next character
            continue

        # Increment the character index
        c += 1
