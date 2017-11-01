# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:57:31 2017

@author: Karen Liou, Tim Ressler
"""
        
class Language():    
    def __init__(self, token, description, set_of_constraints):
        self.token = token
        self.description = description
        self.constraints = [set_of_constraints]
        
    # adds a set of constraints to Language
    def __lshift__(self, set_of_constraints):
        self.constraints.append(set_of_constraints)
        
    # returns True if a set of costraints is in Language
    def __contains__(self, set_of_constraints):
        if set_of_constraints in self.constraints:
            return True
        else:
            return False
    
    # returns the number of constraints
    def count(self):
        return len(self.constraints)
        
class Bin():
    def __init__(self):
        self.languages = []
        
    # adds a language to a bin
    def __lshift__(self, new_language):
        # checks if language token is already in bin
        for language in self.languages:
            # if token matches, add the constraints to token
            if new_language.token == language.token:
                for set_of_constraints in new_language.constraints:
                    language << set_of_constraints
                print("Constraints added")
                return

        # addes language to bin
        self.languages.append(new_language)
        print("Language binned")
      
    # searchs a bin for a language token
    def __contains__(self, token):
        for language in self.languages:
            if token == language.token:
                return True
        return False
    
    # returns the number of languages in a bin
    def count(self):
        return len(self.languages)
       
    # returns a list of language tokens in a bin
    def tokens_list(self):
        tokens_list = []
        for language in self.languages:
            tokens_list.append(language.token)
        return tokens_list
       
    # returns the address of the token argument
    def token(self, token):
        for language in self.languages:
            if token == language.token:
                return language
        raise IndexError("token not in bin")