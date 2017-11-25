GSCbins README

Update 2.0
Lots of changes since the first edition. The main change is the integration of convex hulls. This allows us to treat
arrays of constraints as shapes, instead of point clouds. Note that for convex hulls to be calculated, there must be
more sets of constraints than there are constraints, and those sets cannot form a "plane" or the equivalent in
higher dimensions.

    - old Language.__contains__() changed to Language.constraint()
    - new Language.__contains__() now determines if point is in the convex hull of the language
    - Language.language() returns the set of constraints of a language found in the conxev hull
        of the base language
    - Language.volume() calculates volume of convex hull
    - Bin.plot() plots the languages in a bin using two dimensions
    
Update 2.1: added more plotting functions to Bin()
    - plots are now generated using paths instead of lines
    - changed name of Bin.plot() to Bin.plot_bin() and added legend to plot
    - added Bin.plot_language() which plots a specific language or list of languages in a bin
    - added Language.plot() to plot a language
    - added legends to all plotting functions
    - added background color to all plots

All loads and saves will work from 1.0.

--------------------------------------------------------------------------------

class Language()
To create a language:
    In [1]: language1 = Language("LHO LHC SHO SHC LLC SLC LLO SLO", (-0.5, -0.5, -1, -1), "totally faithful")
    In [2]: language2 = Language("LHO LHC SHO SHC LLC SLC LLO SLO", (-0.5, -0.5, -1, -1))

To add another set of constraints to a language:
    In [3]: language1 << (-0.5, -0.6, -1, -1)

NEW: To see if a set of constraints is in the convex hull of a language:
    There must be more sets of constraints than constraints (5 sets in this case):
        In [4]: language1 << (-0.6, -0.5, -1, -1)
        In [5]: language1 << (-0.5, -0.5, -0.9, -1)
        In [6]: language1 << (-0.5, -0.6, -1, -0.9)

    In [7]: (-0.5, -0.6, -1, -0.95) in language1
    Out[7]: True

NEW: To see if a set of constraints one of the language's constraint sets:
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

NEW: To return the sets of constraints of another language's sets of constraints that lie in the convex hull
of the language:
    In [12]: language1.language(language2)
    Out[12]: [[-0.5, -0.5, -1.0, -1.0]]

NEW: To create a 2D plot of the language using two constraints as axes
(first constraint, second constraint, optional alpha):
    In [13]: language1.plot(0, 1)
    Out[13]:
    In [14]: language1.plot(0, 1, 0)
    Out[14]:

NEW: To return the volume of the convex hull of a language:
    In [15]: language1.volume()
    Out[15]: 4.166666666666659e-06
    
To return a numpy array of all of the sets of contraints in a language:
    In [16]: language1.constraints
    Out[16]: 
    array([[-0.5, -0.5, -1. , -1. ],
           [-0.5, -0.6, -1. , -1. ]])

To return the description of a language:
    In [17]: language1.description
    Out[17]: 'totally faithful'

--------------------------------------------------------------------------------

class Bin()
To create a bin:
    In [18]: good_bin = Bin()

To add a language to a bin:
    In [19]: good_bin << language1
    
To see if a language token is in a bin:
    In [20]: "SHO SHC SHO SHC LLC SLC LLO SLO" in good_bin
    Out[20]: False

To return the address of a set of contraints in a bin:
    In [21]: good_bin.constraint_set((-0.5, -0.5, -1, -1))
    Out[21]: <__main__.Language at 0x1a4df9c4dd8>

    You can then do all Language operations on the returned address:
        In [22]: good_bin.constraint_set((-0.5, -0.5, -1, -1)) << (-0.5, -0.7, -1, -1)
        In [23]: good_bin.constraint_set((-0.5, -0.5, -1, -1)).constraints
        Out[23]:
        array([[-0.5, -0.5, -1. , -1. ],
               [-0.5, -0.6, -1. , -1. ],
               [-0.6, -0.5, -1. , -1. ],
               [-0.5, -0.5, -0.9, -1. ],
               [-0.5, -0.6, -1. , -0.9],
               [-0.5, -0.7, -1. , -1. ]])
        etc.

To count how many languages are in a bin:
    In [24]: good_bin.count()
    Out[24]: 1

To save a bin to a .txt file:
    In [25]: good_bin.save("good_bin.txt")

To load a bin of languages from a .txt file:
    In [26]: good_bin.load("good_bin.txt")

    Note: Loading a bin does not overwrite the current contents. Loading the same file twice will
        create duplicate constraints for each language token. You might want to empty a bin first.

NEW: To create a 2D plot of all the languages in the bin using two constraints as axes:
    In [27]: good_bin.plot_bin(0, 1)
    Out[27]: 
    In [28]: good_bin.plot_bin(2, 3, 0)
    Out[28]: 

NEW: To create a 2D plot of specific languages in the bin using two constraints as axes:
    In [29]: good_bin.plot_bin(0, 1)
    Out[29]: 
    In [30]: good_bin.plot_bin(0, 1, 1)
    Out[30]: 

To return the address of a specific language token in a bin:
    In [31]: good_bin.token("LHO LHC SHO SHC LLC SLC LLO SLO") 
    Out[31]: <__main__.Language at 0x1a4df9c4dd8>

    You can then do all Language operations on the returned address:
        In [32]: good_bin.token("LHO LHC SHO SHC LLC SLC LLO SLO") << (-0.5, -0.8, -1, -1)
        In [33]: good_bin.token("LHO LHC SHO SHC LLC SLC LLO SLO").constraints
        Out[33]:
        array([[-0.5, -0.5, -1. , -1. ],
               [-0.5, -0.6, -1. , -1. ],
               [-0.6, -0.5, -1. , -1. ],
               ..., 
               [-0.5, -0.6, -1. , -0.9],
               [-0.5, -0.7, -1. , -1. ],
               [-0.5, -0.8, -1. , -1. ]])
        etc.

To return a list of language tokens in a bin:
    In [34]: good_bin.tokens_list()
    Out[34]: ['LHO LHC SHO SHC LLC SLC LLO SLO']

To empty a bin (or dereference all languages in a bin):
    In [35]: good_bin.empty()

--------------------------------------------------------------------------------

def bin_language(language, good_bin, okay_bin, trash_bin)
To automatically sort a language into a bin according to language_tokens.txt:
    In [26]: bin_language(language1, good_bin, okay_bin, trash_bin)

    If a language is not listed in the .txt file, user is prompted to enter info. Info is stored as follows:
        token,quality,description