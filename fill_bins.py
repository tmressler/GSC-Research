# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 13:49:13 2017

@author: Tim
"""

# import libraries
from GSCbins import *
try:
    import xlrd
except ImportError:
    import pip
    pip.main(['install', 'xlrd'])
    import xlrd
    print()
    
# open Excel file and read contents
data_file = xlrd.open_workbook('typologyFFC.xlsx', on_demand=True)
data = data_file.sheet_by_index(0)

# creates a big for all languages (not sure how to sort the file we have yet)
general_bin = Bin()

# creates langauges and adds them to bin
rows = data.get_rows()
next(rows)
for row in rows:
    general_bin << Language(row[20].value, None, (row[0].value, row[1].value, row[2].value, row[3].value))
    
'''
Language Notes
Good:
    LHOLHCSHOSHCLLCSLCLLOSLO, total faithfulness
    SHOSHCSHOSHCLLCSLCLLOSLO, shortening of long high vowels
    LLOLLCSHOSHCLLCSLCLLOSLO, lowering of long high vowels
    LHOSHCSHOSHCSLCSLCLLOSLO, shortening of long vowels in closed syllables
    LLOSHCSHOSHCSLCSLCLLOSLO, A) shortening of long vowels in closed syllables + B) long high vowel lowering (A bleeds B)
    LLOSLCSHOSHCSLCSLCLLOSLO, A) lowering of long high vowels + B) shortening of long vowels in closed syllables (B counterbleeds A)
    
Acceptable:
    SHOSHCSHOSHCSLCSLCLLOSLO, A) shortening of long vowels in closed syllables + B) shortening of long high vowels, A) shortening of long high vowels + B) shortening of long vowels in closed syllables
    LHOLHOSHOSHCLLOSLCLLOSLO, opening of closed syllables with long vowels
    SHOSHCSHOSHCLLOSLCLLOSLO, A) shortening of long high vowels + B) opening of closed syllables with long vowels (A bleeds B)
    LLOLLOSHOSHCLLOSLCLLOSLO, A) lowering of long high vowels + B) opening of closed syllables with long vowels
    LHOSHCSHOSHCLLCSLCLLOSLO, shortening of long high vowels in closed syllables
    LLOSHCSHOSHCLLCSLCLLOSLO, A) shortening of long high vowels in closed syllables + B) lowering of long high vowels (A bleeds B)
    LHOSHCSHOSHCLLOSLCLLOSLO, A) shortening of long high vowels in closed syllables + B) opening of closed syllables with long vowels (A bleeds B)
    LLOSHCSHOSHCLLOSLCLLOSLO, A) shortening of long high vowels in closed syllables + B) lowering of long high vowels (A bleeds B) + C) opening of closed syllables with long vowels (A bleeds C)
'''