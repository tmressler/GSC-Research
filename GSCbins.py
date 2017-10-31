# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:57:31 2017

@author: Karen Liou, Tim Ressler
"""

class Language():    
    def __init__(self, name, token, constraints):
        self.name = name
        self.token = token
        self.language_constraints = [constraints]
        
    def __lshift__(self, constraints):
        # adds a set of constraints to Language
        self.language_constraints.append(constraints)
        
    def __contains__(self, constraints):
        # returns True if a set of costraints is in Language
        if constraints in self.language_constraints:
            return True
        else:
            return False
    
    def __len__(self):
        # returns the number of constraints
        return len(self.language_constraints)
        
    def contents(self):
        # prints a list of all sets of contraints
        print(self.language_constraints)
     
class Bin():
    def __init__(self):
        self.bin_languages = []
        
    def __lshift__(self, language):
        # adds a language to a bin
        for bin_language in self.bin_languages:
            if language.token == bin_language.token:
                bin_language << language.language_constraints
                print("Constraints added")
                return
        self.bin_languages.append(language)
        print("Language binned")
        
    def __contains__(self, token):
        # searchs a bin for a language token
        for language in self.bin_languages:
            if token == language.token:
                return True
        return False
        
    def tokens_list(self):
        # prints a list of language tokens in a bin
        for language in self.bin_languages:
            print(language.token)
        
    def contents(self):
        # prints the contents of a bin
        print(self.bin_languages)
        
    def token(self, token):
        # returns the address of the token argument, if it is in Bin
        for language in self.bin_languages:
            if token == language.token:
                return language
        raise IndexError("token not in bin")