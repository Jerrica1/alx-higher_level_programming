==============================
How to use 5-text_indentation.py
==============================

Import file
    >>> text_indentation = __import__('5-text_indentation').text_indentation

Correct Usage:

    >>> t=" : . ? "

Output for this function should be las this
>>> t="Hello. : \nI am a string? .\n"


t is equal to: 

>>> t=" : . ? "


On Errors:

empty string: 
>>> text_indentation()
Traceback (most recent call last):
TypeError: text_indentation() missing 1 required positional argument: 'text'

more than one string
>>> text_indentation("ble", "ooh", "wah")
Traceback (most recent call last):
TypeError: text_indentation() takes 1 positional argument but 3 were given

>>> text_indentation(19)
Traceback (most recent call last):
TypeError: text must be a string

>>> text_indentation("")

>>> text_indentation()
Traceback (most recent call last):
TypeError: text_indentation() missing 1 required positional argument: 'text'

>>> text_indentation("Holberton.")
Holberton.
<BLANKLINE>

>>> text_indentation("Hello")
Hello
