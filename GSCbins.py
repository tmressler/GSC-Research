# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:57:31 2017

@author: Karen Liou, Tim Ressler
@version: 1.03

changelog:
    1.03: first implementatoin of constraint_space()
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
        self.constraints = numpy.array([set_of_constraints])
        self.description = description
        
    # adds a set of constraints to Language
    def __lshift__(self, set_of_constraints):
        self.constraints = numpy.vstack((self.constraints, set_of_constraints))
        
    # returns True if a set of costraints is in Language
    def __contains__(self, set_of_constraints):
        if list(set_of_constraints) in self.constraints.data.tolist():
            return True
        else:
            return False
    
    # returns a tuple of the minimum and maximum constraint(s)
    def constraints_range(self, constraint=None):
        min_constraints = numpy.amin(self.constraints, axis=0)
        max_constraints = numpy.amax(self.constraints, axis=0)
        if constraint == None:
            return (min_constraints, max_constraints)
        else:
            return (min_constraints[constraint], max_constraints[constraint])
     
    # returns the number of constraints
    def count(self):
        return self.constraints.shape[0]
       
class Bin():
    def __init__(self):
        self.languages = []
        
    # adds a language to a bin
    def __lshift__(self, new_language):
        # checks if language token is already in bin
        for language in self.languages:
            # if token matches, add the constraints to token
            if new_language.token == language.token:
                language.constraints = numpy.concatenate((language.constraints, new_language.constraints), axis=0)
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
        
    # returns a list of tokens that are in a range, along with their constraints
    def constraint_space(self, lower_limits, upper_limits):
        space_contents = []
        
        # check each language
        for language in self.languages:
            intersecting_constraints = []
            
            # check every set of constraints for a language
            for set_of_constraints in language.constraints.data.tolist():
                constraint_number = 0
                constraints_in_range = 0
                
                # check each constraint to be in range
                for constraint in set_of_constraints:
                    if constraint >= lower_limits[constraint_number] and constraint <= upper_limits[constraint_number]:
                        constraints_in_range += 1
                    constraint_number += 1
                if constraints_in_range == len(set_of_constraints):
                    intersecting_constraints.append(set_of_constraints)
                    
            space_contents.append([language.token, intersecting_constraints])
            
        return space_contents
                
    # returns the number of languages in a bin
    def count(self):
        return len(self.languages)

    # empties a bin of its languages
    def empty(self):
        self.languages = []
        
    # loads a bin from a text file
    def load(self, filename):
        import ast
        f = open(filename, 'r')
        for entry in f.readlines():
            entry = entry.split('|', 2)
            language = Language(entry[0], None, entry[1])
            language.constraints = numpy.array(ast.literal_eval(entry[2].rstrip()))
            self << language
        
    # saves a bin to a text file
    def save(self, filename):
        f = open(filename, 'w')
        for language in self.languages:
            f.write(language.token + '|' + str(language.description) + '|' + str(language.constraints.data.tolist()) + '\n')
       
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
            entry = entry.split('|')
        
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
            f.write(language.token + '|' + quality + '|' + language.description + '\n')
            bin_it(quality)
        
    f.close()