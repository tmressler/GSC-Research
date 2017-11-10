# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:57:31 2017

@author: Karen Liou, Tim Ressler
"""
 
# import libaries  
try:
    import numpy
except ImportError:
    import pip
    pip.main(['install', 'numpy'])
    import numpy
    print()
     
class Language():    
    def __init__(self, token, set_of_constraints, description=None):
        self.token = token
        self.constraints = [set_of_constraints] # KAREN: change to intializing a one-row array
        self.description = description
        
    # adds a set of constraints to Language
    def __lshift__(self, set_of_constraints):
        self.constraints.append(set_of_constraints) # KAREN: change to adding a row to the constraints array (I'd use numpy.vstack)
        
    # returns True if a set of costraints is in Language
    def __contains__(self, set_of_constraints):
        if set_of_constraints in self.constraints:  # KAREN: change to looking for set_of_contraints in constraints array (using self.constraints.data.tolist() is probably best but there might be a more efficient way; you'd also have to convert set_of_constraints to a list from a tuple if a tuple is entered which is just list(set_of_constraints))
            return True
        else:
            return False
    
    def constraints_range(self, column=None):
        pass # KAREN: I'd have this return the min and max of either a given column or for every column (depending if column=None or not) in the constraints array (https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.amax.html)
     
    # returns the number of constraints
    def count(self):
        return self.constraints.shape[0] # KAREN: I already did this on accident when I was looking other things up
       
class Bin():
    def __init__(self):
        self.languages = []
        
    # adds a language to a bin
    def __lshift__(self, new_language):
        # checks if language token is already in bin
        for language in self.languages:
            # if token matches, add the constraints to token
            if new_language.token == language.token:
                numpy.concatenate((language.constraints, new_language.constraints), axis=0)
                return

        # addes language to bin
        self.languages.append(new_language)
      
    # searchs a bin for a language token
    def __contains__(self, token):
        for language in self.languages:
            if token == language.token:
                return True
        return False
    
    # returns the first language found with a set of constraints
    def constraint_set(self, set_of_constraints):
        for language in self.languages:
            if list(set_of_constraints) in language.constraints.data.tolist():
                return language
        raise IndexError("set of constraints is not in bin")
    
    # returns the number of languages in a bin
    def count(self):
        return len(self.languages)

    # empties a bin of its languages
    def empty(self):
        self.languages = []
        
    # loads a bin from a text file
    def load(self, filename):
        f = open(filename, 'r')
        for entry in f.readlines():
            entry = entry.split(',')
            self << Language(entry[0], entry[2].rstrip(), entry[1])
        
    # saves a bin to a text file
    def save(self, filename):
        f = open(filename, 'w')
        for language in self.languages:
            f.write(language.token + ',' + language.description + ',' + language.constraints.data.tolist() + '\n')
       
    # returns the address of the token argument
    def token(self, token):
        for language in self.languages:
            if token == language.token:
                return language
        raise IndexError("token not in bin")    
    
    # returns a list of language tokens in a bin
    def tokens_list(self):
        tokens_list = []
        for language in self.languages:
            tokens_list.append(language.token)
        return tokens_list
    
# bins a language according to a file "languages.txt"
def bin_language(language, good_bin, okay_bin, trash_bin):     
    def bin_it(quality):
        if quality == "good":
            good_bin << language
        elif quality == "okay":
            okay_bin << language
        elif quality == "trash":
            trash_bin << language
        else:
            f.close()
            raise LookupError("quality \"" + entry[2] + "\" is not valid")
    
    # opens the list of tokens
    try:
        f = open("language_tokens.txt", 'r+')
        
        for entry in f.readlines():
            entry = entry.split(',')
        
            # if token found, bin it appropriately
            if entry[0] == language.token:
                bin_it(entry[1])
                language.description = entry[2].rstrip()
                return
        
    except FileNotFoundError:
        f = open("language_tokens.txt", 'w')
        
    # token not found
    add_to_bin = None
    while add_to_bin != 'y' and add_to_bin != 'n':
        add_to_bin = input("Token \"" + language.token + "\" not recognized. Add to bin? (y/n): ")
        
        # create new token entry
        if add_to_bin == 'y':
            quality = None
            while quality != "good" and quality != "okay" and quality != "trash":
                quality = input("Language quality (good, okay, trash): ")
            if language.description == None:
                language.description = input("Language description: ")
            f.write(language.token + ',' + quality + ',' + language.description + '\n')
            bin_it(quality)
        
    f.close()