#!/usr/bin/env python3

__author__ = "Pramit Barua"
__copyright__ = "Copyright 2019, IMT, KIT"
__credits__ = ["Pramit Barua"]
__license__ = "IMT, KIT"
__maintainer__ = "Pramit Barua"
__email__ = ["pramit.barua@student.kit.edu", "pramit.barua@gmail.com"]


import tkinter as tk
import tkinter.ttk as ttk


def style_config():
    STYLE = ttk.Style()

    STYLE.theme_use('clam')
    STYLE.configure("TFrame",
                    background='white')

    '''default.TButton'''
    STYLE.configure('TButton',
                    background="#%02x%02x%02x" % (0, 144, 215),
                    foreground='white',
                    font=('Muli', 12),
                    relief='flat')
    STYLE.map('TButton',
              background=[('disabled', 'white'),
                          ('pressed', "#%02x%02x%02x" % (0, 73, 108)), 
                          ('active', "#%02x%02x%02x" % (0, 144, 168))],
              foreground=[('disabled', 'gray'),
                          ('pressed', 'white'),
                          ('active', 'white')])

    '''info.TButton'''
    STYLE.configure('info.TButton',
                    background='white',
                    bordercolor='white',
                    font=('Muli', 12),
                    relief='flat')
    STYLE.map('info.TButton',
              background=[('disabled', 'white'),
                          ('pressed', 'white'),
                          ('active', 'white')],
              foreground=[('disabled', 'white'),
                          ('pressed', 'white'),
                          ('active', 'white')])

    '''cancel.TButton'''
    STYLE.configure('cancel.TButton',
                    background='white',
                    foreground="#%02x%02x%02x" % (191, 191, 191),
                    bordercolor="#%02x%02x%02x" % (191, 191, 191),
                    font=('Muli', 12),
                    relief='groove')
    STYLE.map('cancel.TButton',
              background=[('disabled', 'white'),
                          ('pressed', "#%02x%02x%02x" % (236, 236, 236)),
                          ('active', "#%02x%02x%02x" % (246, 246, 246))],
              foreground=[('disabled', "#%02x%02x%02x" % (191, 191, 191)),
                          ('pressed', "#%02x%02x%02x" % (191, 191, 191)),
                          ('active', "#%02x%02x%02x" % (191, 191, 191))])

    '''analysis.TButton'''
    STYLE.configure('analysis.TButton',
                    background='white',
                    foreground="#%02x%02x%02x" % (191, 191, 191),
                    font=('Muli', 12),
                    relief='flat')
    STYLE.map('analysis.TButton',
              background=[('disabled', 'white'),
                          ('pressed', "#%02x%02x%02x" % (0, 73, 108)),
                          ('active', "#%02x%02x%02x" % (0, 144, 168))],
              foreground=[('disabled', "#%02x%02x%02x" % (191, 191, 191)),
                          ('pressed', "#%02x%02x%02x" % (191, 191, 191)),
                          ('active', "#%02x%02x%02x" % (89, 89, 89))])

    '''TLabel'''
    STYLE.configure('TLabel',
                    background='white',
                    foreground="#%02x%02x%02x" % (89, 89, 89),
                    font=('Muli', 12),
                    relief='flat')
    '''Title.TLabel'''
    # it defines the title of the analysis (the font size is bigger)
    STYLE.configure('title.TLabel',
                    background='white',
                    foreground="#%02x%02x%02x" % (89, 89, 89),
                    font=('Muli', 16, 'bold'), #font
                    relief='flat')
    '''image.TLabel''' # used in the text of N-spacer image
    # it defines the info image in the analysis pop ups(the font size is smaller)
    STYLE.configure('image.TLabel',
                    background='white',
                    foreground="#%02x%02x%02x" % (89, 89, 89),
                    font=('Muli', 8), #font
                    relief='flat')

    STYLE.configure("Treeview.Heading",
                    font=('Muli', 10))

    STYLE.configure('TSeparator',
                    orient=tk.HORIZONTAL)