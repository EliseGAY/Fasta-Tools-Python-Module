# Python-Module

List of python functions
Used with Python 3.6

# Python modules to play with fasta file
Functions are
- Split fasta file in 'n' fasta file with 'x' sequences
- Create dictionnary of Key=sequence_ID and value=Sequences
- Subset fasta file from an ID list of sequence
- Add attribute to fasta ID and return fasta file with complete ID
- Remove dupicated nucleiq seqeuence in fasta file
- Count number of "N" or "n" character in fasta sequence

# Run modules on a ptyhon script :
'''
# -*- coding: utf-8 -*-
import sys
import os

sys.path.append('PATH_TO/software/python_tools/')
import fasta_tools

# example of one function used :
fasta_tools.get_N_percent("PATH_TO_YOUR_FILE")
'''
