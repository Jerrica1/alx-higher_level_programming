==============================
How to use 3-say_my_name.py
==============================

1) Import file 
>>> say_my_name = __import__('3-say_my_name').say_my_name

2) say my name, test
>>> say_my_name("Monica", "Jaimes Caicedo")
My name is Monica Jaimes Caicedo

say my name, test
>>> say_my_name("Monica", "Jaimes Caicedo")
My name is Monica Jaimes Caicedo


3) say my name with space
>>> say_my_name("Monica")
My name is Monica 

4) Error with integers for say my name
>>> say_my_name(1, "me")
Traceback (most recent call last):
TypeError: first_name must be a string

5) Error with integers for my lastname
>>> say_my_name("Guido", [1, 2, 3,])
Traceback (most recent call last):
TypeError: last_name must be a string

6) Error for none name and last name
>>> say_my_name(None, None)
Traceback (most recent call last):
TypeError: first_name must be a string

7) Error for None name
>>> say_my_name(None)
Traceback (most recent call last):
TypeError: first_name must be a string

8) empty values
>>> say_my_name()
Traceback (most recent call last):
TypeError: say_my_name() missing 1 required positional argument: 'first_name'


9)
