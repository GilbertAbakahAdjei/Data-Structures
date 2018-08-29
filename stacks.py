# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Stack:
    def __init__(self):
        self.elements = []
    def push(self, element):
        self.elements.append(element)
    def size(self):
        return len(self.elements)
    def pop(self):
        return self.elements.pop()
    def isEmpty(self):
        self.elements == []
   
