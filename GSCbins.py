# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:57:31 2017

@author: Tim
"""

class Language():
    language_constraints = []
    
    def __init__(self, name, token, constraints):
        self.name = name
        self.token = token
        self.language_constraints.append(constraints)
        
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
    bin_languages = []
    
    def __init__(self, quality):
        self.quality = quality
        
    def __lshift__(self, language):
        # adds a language to a bin
        self.bin_languages.append(language)
        
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
   
def info():
    print("""GSCbins README

class Language()
To create a language:
    language1 = Language("totally faithful", "LHO LHC SHO SHC LLC SLC LLO SLO", (-0.5, -0.5, -1, -1))

To add another set of constraints to a language:
    language1 << (-0.5, -0.6, -1, -1)

To see if a set of contraints is in a language:
    (-0.5, -0.6, -1, -1) in language1

To count number of sets of constraints for a language:
    len(language1)
    
To print contents of a language:
    language1.contents()

class Bin()
To create a bin:
    good_bin = Bin('good')

To add a language to a bin:
    good_bin << language1
    
To return a list of language tokens in a bin:
    good_bin.tokens_list()

To see if a language token is in a bin:
    "SHO SHC SHO SHC LLC SLC LLO SLO" in good_bin
    
To see this information again:
    GSCbins.info()""")       
        
info()