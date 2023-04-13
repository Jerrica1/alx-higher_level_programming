#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.first.name = first_name
        self.last.name = last_name
        self.age = age

    def to_json(self):
        return {"first.name": self.first.name,
                "last.name": self.last.name,
                "age": self.age}
