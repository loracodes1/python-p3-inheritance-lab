#!/usr/bin/env python

from user import User


class Student(User):
    def __init__(self, first_name, last_name):
        """
        Initializes a Student instance with first and last name,
        and an empty knowledge list.
        """
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, info):
        """
        Adds a string to the student's knowledge list.
        """
        self.knowledge.append(info)
