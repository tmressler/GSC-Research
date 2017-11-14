GSCbins README

--------------------------------------------------------------------------------

class Language()
To create a language:
    In [1]: language1 = Language("LHO LHC SHO SHC LLC SLC LLO SLO", (-0.5, -0.5, -1, -1), "totally faithful")
    In [2]: language2 = Language("LHO LHC SHO SHC LLC SLC LLO SLO", (-0.5, -0.5, -1, -1))

To add another set of constraints to a language:
    In [3]: language1 << (-0.5, -0.6, -1, -1)

To see if a set of contraints is in a language:
    In [4]: (-0.5, -0.6, -1, -1) in language1
    Out[4]: True

To return the range of contraints, or the range of just one constraint in a language:
    In [5]: language1.constraints_range()
    Out[5]: (array([-0.5, -0.6, -1. , -1. ]), array([-0.5, -0.5, -1. , -1. ]))
    In [6]: language1.constraints_range(1)
    Out[6]: (-0.6, -0.5)

To count number of sets of constraints for a language:
    In [7]: language1.count()
    Out[7]: 2
    
To return a numpy array of all of the sets of contraints in a language:
    In [8]: language1.constraints
    Out[8]: 
    array([[-0.5, -0.5, -1. , -1. ],
           [-0.5, -0.6, -1. , -1. ]])

To return the description of a language:
    In [9]: language1.description
    Out[9]: 'totally faithful'

--------------------------------------------------------------------------------

class Bin()
To create a bin:
    In [10]: good_bin = Bin()

To add a language to a bin:
    In [11]: good_bin << language1
    
To see if a language token is in a bin:
    In [12]: "SHO SHC SHO SHC LLC SLC LLO SLO" in good_bin
    Out[12]: False

To return the address of a set of contraints in a bin:
    In [13]: good_bin.constraint_set((-0.5, -0.5, -1, -1))
    Out[13]: <__main__.Language at 0x1a4df9c4dd8>

    You can then do all Language operations on the returned address:
        In [14]: good_bin.constraint_set((-0.5, -0.5, -1, -1)) << (-0.5, -0.7, -1, -1)
        In [15]: good_bin.constraint_set((-0.5, -0.5, -1, -1)).constraints
        Out[15]:
        array([[-0.5, -0.5, -1. , -1. ],
               [-0.5, -0.6, -1. , -1. ],
               [-0.5, -0.7, -1. , -1. ]])
        etc.

To count how many languages are in a bin:
    In [16]: good_bin.count()
    Out[16]: 1

To save a bin to a .txt file:
    In [17]: good_bin.save("good_bin.txt")

To load a bin of languages from a .txt file:
    In [18]: good_bin.load("good_bin.txt")

Note: Loading a bin does not overwrite the current contents. Loading the same file twice will create duplicate
    constraints for each language token.

To return the address of a specific language token in a bin:
    In [19]: good_bin.token("SHO SHC SHO SHC LLC SLC LLO SLO")
    Out[19]: <__main__.Language at 0x1a4df9c4dd8>

    You can then do all Language operations on the returned address:
        In [20]: good_bin.token("LHO LHC SHO SHC LLC SLC LLO SLO") << (-0.5, -0.8, -1, -1)
        In [21]: good_bin.token("LHO LHC SHO SHC LLC SLC LLO SLO").constraints
        Out[21]:
        array([[-0.5, -0.5, -1. , -1. ],
               [-0.5, -0.6, -1. , -1. ],
               [-0.5, -0.7, -1. , -1. ],
               [-0.5, -0.8, -1. , -1. ]])
        etc.

To return a list of language tokens in a bin:
    In [22]: good_bin.tokens_list()
    Out[22]: ['LHO LHC SHO SHC LLC SLC LLO SLO']

To empty a bin (or dereference all languages in a bin):
    In [23]: good_bin.empty()

--------------------------------------------------------------------------------

def bin_language(language, good_bin, okay_bin, trash_bin)
To automatically sort a language into a bin according to language_tokens.txt:
    In [24]: bin_language(language1, good_bin, okay_bin, trash_bin)

    If a language is not listed in the .txt file, user is prompted to enter info. Info is stored as follows:
        token,quality,description