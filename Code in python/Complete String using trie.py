# from os import *
# from sys import *
from collections import *
from math import *

from typing import *

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    
    def checkIfPrefixExists(self,word):
        node = self.root
        node.is_word = True
        for char in word:
            if char in node.children and node.is_word == True:
                node = node.children[char]
            else:
                return False
        return True

def completeString(n: int, a: List[str])-> str:
    trie = Trie()
    
    for word in a:
        trie.insert(word)

    longest = ""

    for word in a:
        # print(trie.checkIfPrefixExists(word))
        if trie.checkIfPrefixExists(word):
            
            if len(word) > len(longest):
                longest = word
            elif len(word) == len(longest) and word < longest:
                longest = word
    if longest == "":
        return None
    return longest
    
    pass