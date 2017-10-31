GSCbins README

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