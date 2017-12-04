# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:57:31 2017

@author: Karen Liou, Tim Ressler
@version: 3.0
    
"""
 
# import libaries  
try:
    import numpy
except ImportError:
    import pip
    pip.main(['install', 'numpy'])
    import numpy
    print()
try:
    from scipy.spatial import ConvexHull, Delaunay
    from scipy.spatial.qhull import QhullError
except ImportError:
    import pip
    pip.main(['install', 'scipy'])
    from scipy.spatial import ConvexHull, Delaunay
    from scipy.spatial.qhull import QhullError
    print()
try:
    import matplotlib.pyplot as plt
    import matplotlib.path as mpath
    import matplotlib.patches as mpatches
    from mpl_toolkits.mplot3d import axes3d
except ImportError:
    import pip
    pip.main(['install', 'matplotlib'])
    import matplotlib.pyplot as plt
    import matplotlib.path as mpath
    import matplotlib.patches as mpatches
    from mpl_toolkits.mplot3d import axes3d
    print()
     
class Language():        
    def __init__(self, token, set_of_weights, description=None):
        self.token = token
        self.weights = numpy.array([set_of_weights])
        self.description = description
        
    # adds a set of weights to the language
    def __lshift__(self, set_of_weights):
        self.weights = numpy.vstack((self.weights, set_of_weights))

    # returns True if a set of weights is in the convex hull of the language using Delauney triangulation
    def __contains__(self, set_of_weights):
        return Delaunay(self.weights).find_simplex(set_of_weights) >= 0
        
    # returns True if a set of weights is a member of language.weights
    def set_of_weights(self, set_of_weights):
        if list(set_of_weights) in self.weights.data.tolist():
            return True
        else:
            return False
        
    # returns a tuple of the minimum and maximum weight(s)
    def constraint_range(self, constraint=None):
        min_constraints = numpy.amin(self.weights, axis=0)
        max_constraints = numpy.amax(self.weights, axis=0)
        if constraint == None:
            return (min_constraints.tolist(), max_constraints.tolist())
        else:
            return (min_constraints[constraint], max_constraints[constraint])
     
    # returns the number of sets of weights in the language
    def count_weights(self):
        return self.weights.shape[0]   

    # checks if another language has sets of weights in the language's convex hull
    def weights_in(self, language):
        intersecting_weights = []
        for set_of_weights in self.weights.tolist():
            if set_of_weights in language:
                intersecting_weights.append(set_of_weights)
        return intersecting_weights
            
    # plots the language on two axes corresponding to two constraints
    def plot(self, first_constraint, second_constraint, third_constraint=None, alpha=0.1):
        master_plot(self, first_constraint, second_constraint, third_constraint, alpha, offset=0)

    # returns the verticies of the language's convex hull
    def vertices(self):
        return self.weights[ConvexHull(self.weights).vertices]
    
    # returns the volume of the language's convex hull
    def volume(self):
        return ConvexHull(self.weights).volume
       
class Bin():
    def __init__(self):
        self.languages = []
        
    # adds a language to a bin
    def __lshift__(self, new_language):
        # checks if language token is already in bin
        for language in self.languages:
            # if token matches, add the weights to token
            if new_language.token == language.token:
                language.weights = numpy.concatenate((language.weights, new_language.weights), axis=0)
                return

        # addes language to bin
        self.languages.append(new_language)
      
    # searchs a bin for a language token
    def __contains__(self, token):
        for language in self.languages:
            if token == language.token:
                return True
        return False
    
    # returns the first language found with a set of weights
    def set_of_weights(self, set_of_weights):
        for language in self.languages:
            if list(set_of_weights) in language.weights.data.tolist():
                return language
        raise IndexError("set of weights is not in bin")
        
    # returns a list of tokens that are in a range, along with their weights
    def constraint_space(self, lower_limits, upper_limits):
        space_contents = []
        
        # check each language
        for language in self.languages:
            intersecting_weights = []
            
            # check every set of weights for a language
            for set_of_weights in language.weights.data.tolist():
                constraint_number = 0
                weights_in_range = 0
                
                # check each constraint to be in range
                for constraint in set_of_weights:
                    if constraint >= lower_limits[constraint_number] and constraint <= upper_limits[constraint_number]:
                        weights_in_range += 1
                    constraint_number += 1
                if weights_in_range == len(set_of_weights):
                    intersecting_weights.append(set_of_weights)
                    
            space_contents.append([language.token, intersecting_weights])
            
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
            language.weights = numpy.array(ast.literal_eval(entry[2].rstrip()))
            self << language
         
    # plots the languages in the bin using two weights
    def plot_bin(self, first_constraint, second_constraint, third_constraint=None, alpha=0.1, offset=0.05):
        master_plot(self.languages, first_constraint, second_constraint, third_constraint, alpha, offset)
  
    # plots one or more languages in the bin on a two dimensional graph
    def plot_languages(self, languages, first_constraint, second_constraint, third_constraint=None, alpha=0.1, offset=0.05):
        master_plot(languages, first_constraint, second_constraint, third_constraint, alpha, offset)
        
    # saves a bin to a text file
    def save(self, filename):
        f = open(filename, 'w')
        for language in self.languages:
            f.write(language.token + '|' + str(language.description) + '|' + str(language.weights.data.tolist()) + '\n')
       
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
    
def master_plot(languages, first_constraint, second_constraint, third_constraint, alpha, offset):
    if isinstance(languages, Language):
        languages = [languages]
            
    counter = 0
        
    if third_constraint == None:
        error_tokens = []
        figure, axes = plt.subplots()
            
        for language in languages:
            
            # plots constrain points
            axes.plot(language.weights[:,first_constraint] + (counter * offset), language.weights[:,second_constraint], 'o', label=language.token)
            
            # plots convex hull using witchcraft
            try:
                codes = [1]
                vertices = []
                for index in ConvexHull(language.weights[:,[first_constraint, second_constraint]]).vertices:
                    codes.append(2)
                    vertices.append(language.weights[index, [first_constraint, second_constraint]].tolist())
                    vertices[-1][0] += (counter * offset)
                codes[len(codes) - 1] = 79
                vertices.append(vertices[0])
                path = mpath.Path(vertices, codes)
                axes.add_patch(mpatches.PathPatch(path, facecolor='C'+str(counter % 10), alpha=alpha))
                x, y = zip(*path.vertices)
                line, = axes.plot(x, y, 'k-')
                counter += 1
            except QhullError:
                error_tokens.append(language.token)

        if len(error_tokens) > 0:
            print("Languages with no convex hull in these dimensions: " + ', '.join(error_tokens))
        
    else:
        figure = plt.figure()
        axes = figure.add_subplot(111, projection='3d')
        for language in languages:
            axes.scatter(language.weights[:,first_constraint] + (counter * offset), language.weights[:,second_constraint], language.weights[:,third_constraint], label=language.token)

        axes.set_zlabel("constraint " + str(third_constraint))
     
    axes.set_ylabel("constraint " + str(second_constraint))
    axes.set_xlabel("constraint " + str(first_constraint))
    chartBox = axes.get_position()
    axes.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
    axes.legend(loc='upper center', bbox_to_anchor=(1.2, 1), ncol=1)