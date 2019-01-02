#!/usr/bin/env python3

__author__ = "Pramit Barua"
__copyright__ = "Copyright 2018, IMT, KIT"
__credits__ = ["Pramit Barua"]
__license__ = "IMT, KIT"
__version__ = "1"
__maintainer__ = "Pramit Barua"
__email__ = ["pramit.barua@student.kit.edu", "pramit.barua@gmail.com"]

'''

'''

import numpy as np 
import tkinter as tk
import tkinter.filedialog as filedialog


def file_browser(path):
    '''
    This method reads the txt file
    and returns line/s of the file in a list
    '''
    # define lines based on '\n' 
    with open(path, "r") as raw_data:
        data_buf = raw_data.read().split('\n')

    data_str = []
    for item in data_buf:
        # remove empty lines in the txt file
        if item:
            # remove white space (space, \t etc)
            data_str.append(''.join(item.split()))
    return data_str


def overlapping_sequence_fun(path, overlapSteps, length_peptide):
    '''
    This method generates the overlap sequence
    based on the overlap_step and peptide length
    this method also used during the substitutional analysis
    '''

    data = file_browser(path)
    overlap_block = []
    #for number of lines in data file
    for line in data:
        visited = False
        buf = []
        for item in line:
            if item is '(':
                buf.append('')
                visited = True
            if visited:
                buf[-1] += item
                if item is ')':
                    visited = False
            else:
                buf.append(item)

        if len(buf) > length_peptide:
            overlap_block += [''.join(buf[i:i+length_peptide]) for i in range(0, len(buf), overlapSteps)
                              if len(buf[i:i+length_peptide]) == length_peptide]
        else:
            overlap_block += ''.join(buf)
    return overlap_block


def main():

    tk.Tk().withdraw()
    path = filedialog.askopenfilename()
    
    overlap_steps = 1
    length_peptide = 10
    overlapping_sequence_fun(path, overlap_steps, length_peptide)


if __name__ == '__main__':
    main()

