# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:43:44 2018

@author: gilbert
"""

'''Linear search or sequential search is a type of 
    searhing algorithm in which the entire sequence 
    in a list is searched until the targeted key
    is found. It has a time complexity of O(n)
    where n is the total of elements/items in the
    list. A quick definition of what time complexity is:
    The time which an algorithm runs with relation
    to its input is termed as time complexity. An example of linear search
    would be finding my friend Samuel in a queue buying food. Because
    I know Samuel by face, I would check from begining of the queue till
    I find my target - in this case Samuel. If I don't match Samuel early,
    It means I would have to check the entire queue till I find him. That
    would be the worst case. Hence if the queue is of length n, at worse
    to find Samuel, I have to go through it n-times. That's why the time
    complexity is O(n). '''
    
    #Let's write some python code to implement this
length = input('Input the length of your list')
def linear_search(length):
    list_items = [input('Enter your list items') for i in range(length)]
    target = input('Input your element you want to match')
    for k in range(len(list_items)):
        if k == target:
            return '{} found at position {}'.format(target,k)
        else:
            return '{} not found in the list'.format(target)
    