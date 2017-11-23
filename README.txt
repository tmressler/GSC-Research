GSCbins README

Update 2.0
The main change is the integration of convex hulls. This allows us to treat arrays of constraints as shapes,
instead of point clouds. Note that for convex hulls to be calculated, there must be more sets of
constraints than there are constraints, and those sets cannot form a "plane" or the equivalent in higher
dimensions.

    - old Language.__contains__() changed to Language.constraint()
    - new Language.__contains__() now determines if point is in the convex hull of the language
    - Language.language() returns the set of contraints of a language found in the conxev hull
        of the base language
    - Language.volume() calculates volume of convex hull
    - Bin.plot() plots the languages in a bin using two dimensions

--------------------------------------------------------------------------------

class Language()
To create a language:
    In [1]: language1 = Language("LHO LHC SHO SHC LLC SLC LLO SLO", (-0.5, -0.5, -1, -1), "totally faithful")
    In [2]: language2 = Language("LHO LHC SHO SHC LLC SLC LLO SLO", (-0.5, -0.5, -1, -1))

To add another set of constraints to a language:
    In [3]: language1 << (-0.5, -0.6, -1, -1)

To see if a set of constraints is in the convex hull of a language:
    There must be more sets of constraints than constraints (5 sets in this case):
        In [4]: language1 << (-0.6, -0.5, -1, -1)
        In [5]: language1 << (-0.5, -0.5, -0.9, -1)
        In [6]: language1 << (-0.5, -0.6, -1, -0.9)

    In [7]: (-0.5, -0.6, -1, -0.95) in language1
    Out[7]: True

To see if a set of constraints one of the language's constraint sets:
    In [8]: language1.constraint((-0.5, -0.6, -1, -1))
    Out[8]: True

To return the range of constraints, or the range of just one constraint in a language:
    In [9]: language1.constraints_range()
    Out[9]: (array([-0.6, -0.6, -1. , -1. ]), array([-0.5, -0.5, -0.9, -0.9]))
    In [10]: language1.constraints_range(1)
    Out[10]: (-0.6, -0.5)

To count number of sets of constraints for a language:
    In [11]: language1.count()
    Out[11]: 5

To return the sets of constraints of another language's sets of constraints that lie in the convex hull
of the language:
    In [12]: language1.language(language2)
    Out[12]: [[-0.5, -0.5, -1.0, -1.0]]

To return the volume of the convex hull of a language:
    In [13]: language1.volume()
    Out[13]: 4.166666666666659e-06
    
To return a numpy array of all of the sets of contraints in a language:
    In [14]: language1.constraints
    Out[14]: 
    array([[-0.5, -0.5, -1. , -1. ],
           [-0.5, -0.6, -1. , -1. ]])

To return the description of a language:
    In [15]: language1.description
    Out[15]: 'totally faithful'

--------------------------------------------------------------------------------

class Bin()
To create a bin:
    In [16]: good_bin = Bin()

To add a language to a bin:
    In [17]: good_bin << language1
    
To see if a language token is in a bin:
    In [18]: "SHO SHC SHO SHC LLC SLC LLO SLO" in good_bin
    Out[18]: False

To return the address of a set of contraints in a bin:
    In [19]: good_bin.constraint_set((-0.5, -0.5, -1, -1))
    Out[19]: <__main__.Language at 0x1a4df9c4dd8>

    You can then do all Language operations on the returned address:
        In [20]: good_bin.constraint_set((-0.5, -0.5, -1, -1)) << (-0.5, -0.7, -1, -1)
        In [21]: good_bin.constraint_set((-0.5, -0.5, -1, -1)).constraints
        Out[21]:
        array([[-0.5, -0.5, -1. , -1. ],
               [-0.5, -0.6, -1. , -1. ],
               [-0.6, -0.5, -1. , -1. ],
               [-0.5, -0.5, -0.9, -1. ],
               [-0.5, -0.6, -1. , -0.9],
               [-0.5, -0.7, -1. , -1. ]])
        etc.

To count how many languages are in a bin:
    In [22]: good_bin.count()
    Out[22]: 1

To save a bin to a .txt file:
    In [23]: good_bin.save("good_bin.txt")

To load a bin of languages from a .txt file:
    In [24]: good_bin.load("good_bin.txt")

    Note: Loading a bin does not overwrite the current contents. Loading the same file twice will
        create duplicate constraints for each language token. You might want to empty a bin first.

To create a 2D plot of all the languages in a bin using two constraints:
    In [25]: good_bin.plot(0, 1)
    Out[25]: 

To return the address of a specific language token in a bin:
    In [26]: good_bin.token("LHO LHC SHO SHC LLC SLC LLO SLO") 
    Out[26]: <__main__.Language at 0x1a4df9c4dd8>

    You can then do all Language operations on the returned address:
        In [27]: good_bin.token("LHO LHC SHO SHC LLC SLC LLO SLO") << (-0.5, -0.8, -1, -1)
        In [28]: good_bin.token("LHO LHC SHO SHC LLC SLC LLO SLO").constraints
        Out[28]:
        array([[-0.5, -0.5, -1. , -1. ],
               [-0.5, -0.6, -1. , -1. ],
               [-0.6, -0.5, -1. , -1. ],
               ..., 
               [-0.5, -0.6, -1. , -0.9],
               [-0.5, -0.7, -1. , -1. ],
               [-0.5, -0.8, -1. , -1. ]])
        etc.

To return a list of language tokens in a bin:
    In [29]: good_bin.tokens_list()
    Out[29]: ['LHO LHC SHO SHC LLC SLC LLO SLO']

To empty a bin (or dereference all languages in a bin):
    In [30]: good_bin.empty()

--------------------------------------------------------------------------------

def bin_language(language, good_bin, okay_bin, trash_bin)
To automatically sort a language into a bin according to language_tokens.txt:
    In [24]: bin_language(language1, good_bin, okay_bin, trash_bin)

    If a language is not listed in the .txt file, user is prompted to enter info. Info is stored as follows:
        token,quality,description