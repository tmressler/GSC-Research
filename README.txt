GSCbins README

--------------------------------------------------------------------------------

class Language()
To create a language:
    language1 = Language("LHO LHC SHO SHC LLC SLC LLO SLO", (-0.5, -0.5, -1, -1), "totally faithful")
    language1 = Language("LHO LHC SHO SHC LLC SLC LLO SLO", (-0.5, -0.5, -1, -1))

To add another set of constraints to a language:
    language1 << (-0.5, -0.6, -1, -1)

To see if a set of contraints is in a language:
    (-0.5, -0.6, -1, -1) in language1

To return the range of contraints, or the range of just one constraint in a language:
    language1.constraints_range()
    language1.constraints_range(1)

To count number of sets of constraints for a language:
    language1.count()
    
To return a numpy array of all of the sets of contraints in a language:
    language1.constraints

To return the description of a language:
    language1.description

--------------------------------------------------------------------------------

class Bin()
To create a bin:
    good_bin = Bin()

To add a language to a bin:
    good_bin << language1
    
To see if a language token is in a bin:
    "SHO SHC SHO SHC LLC SLC LLO SLO" in good_bin

To return the address of a set of contraints in a bin:
    good_bin.constraint_set((-0.5, -0.5, -1, -1))

    You can then do all Language operations on the returned address:
        good_bin.constraint_set((-0.5, -0.5, -1, -1)) << (-0.5, -0.6, -1, -1)
        good_bin.constraint_set((-0.5, -0.5, -1, -1)).constraints
        etc.

To count how many languages are in a bin:
    good_bin.count()

To empty a bin (or dereference all languages in a bin):
    good_bin.empty()

To load a bin of languages from a .txt file:
    good_bin.load("C:/.../good_bin.txt")

To save a bin to a .txt file:
    good_bin.save("C:/.../good_bin.txt")

To return the address of a specific language token in a bin:
    good_bin.token("SHO SHC SHO SHC LLC SLC LLO SLO")

    You can then do all Language operations on the returned address:
        good_bin.token("SHO SHC SHO SHC LLC SLC LLO SLO") << (-0.5, -0.6, -1, -1)
        good_bin.token("SHO SHC SHO SHC LLC SLC LLO SLO").constraints
        etc.

To return a list of language tokens in a bin:
    good_bin.tokens_list()

--------------------------------------------------------------------------------

def bin_language(language, good_bin, okay_bin, trash_bin)
To automatically sort a language into a bin according to language_tokens.txt:
    def bin_language(language, good_bin, okay_bin, trash_bin)

    If a language is not listed in the .txt file, user is prompted to enter info. Info is stored as follows:
        token,quality,description