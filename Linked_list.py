#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:47:25 2021

@author: karanoberoi
"""

class Node:    
    def __init__(self,val):
        self.val = val
        self.next = None
        
def insert_beg(head,val):
    n_head = Node(val)
    n_head.next = head
    return n_head


def insert_end(head,val):
    e_head = Node(val)
    end = head
    while end.next is not None:    
        end = end.next
    end.next = e_head
    return end

def reverseList(head):
    r_head = None
    while head:
        temp = head.next
        head.next = r_head
        r_head = head
        head = temp
    return r_head

def listprint(head):    
    while head:        
        print(head.val)
        head = head.next
        
f_node = Node(10)
s_node = Node(15)
t_node = Node(20)

f_node.next = s_node
s_node.next = t_node
print("Printing the Linked List:")
listprint(f_node)

print("Printing the reversed Linked List:")
revert = reverseList(f_node)
listprint(revert)


print("Inserting a node in the beginning Linked List:")
a_node = insert_beg(f_node,120)
listprint(a_node)

print("Inserting a node in the end Linked List:")
e_node = insert_end(f_node,120)
listprint(e_node)

