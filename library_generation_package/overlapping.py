#!/usr/bin/env python3

__author__ = "Pramit Barua"
__copyright__ = "Copyright 2019, IMT, KIT"
__credits__ = ["Pramit Barua"]
__license__ = "IMT, KIT"
__maintainer__ = "Pramit Barua"
__email__ = ["pramit.barua@student.kit.edu", "pramit.barua@gmail.com"]

'''
This file contains the widgets and corresponding methods related
to the pop up window of overlapping 
'''

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


class OverlappingPopUp():
    def __init__(self, parent):
        self.parent = parent
        # bind the overlapping button in parent
        self.parent.button[1].bind("<ButtonRelease-1>", self.show_pop_up) 

    def show_pop_up(self, event):
        print('overlapping pop up')