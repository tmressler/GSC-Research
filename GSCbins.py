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
        
    # adds a set of constraints to Language
    def __lshift__(self, constraints):
        self.language_constraints.append(constraints)
        
    # returns True if a set of costraints is in Language
    def __contains__(self, constraints):
        if constraints in self.language_constraints:
            return True
        else:
            return False
    
    # returns the number of constraints
    def __len__(self):
        return len(self.language_constraints)
        
    # prints a list of all sets of contraints
    def contents(self):
        print(self.language_constraints)
     
class Bin():
    def __init__(self):
        self.bin_languages = []
        
    # adds a language to a bin
    def __lshift__(self, language):
        # checks if language token is already in bin
        for bin_language in self.bin_languages:
            # if token matches, add the constraints to token
            if language.token == bin_language.token:
                bin_language << language.language_constraints
                print("Constraints added")
                return
        
        # addes language to bin
        self.bin_languages.append(language)
        print("Language binned")
      
    # searchs a bin for a language token
    def __contains__(self, token):
        for language in self.bin_languages:
            if token == language.token:
                return True
        return False
       
    # prints a list of language tokens in a bin
    def tokens_list(self):
        for language in self.bin_languages:
            print(language.token)
       
    # prints the contents of a bin
    def contents(self):
        print(self.bin_languages)
     
    # returns the address of the token argument
    def token(self, token):
        for language in self.bin_languages:
            if token == language.token:
                return language
        raise IndexError("token not in bin")