#!/usr/bin/env python3

__author__ = "Pramit Barua"
__copyright__ = "Copyright 2019, IMT, KIT"
__credits__ = ["Pramit Barua"]
__license__ = "IMT, KIT"
__maintainer__ = "Pramit Barua"
__email__ = ["pramit.barua@student.kit.edu", "pramit.barua@gmail.com"]

'''
This file contains the widgets and corresponding methods related
to the pop up window of load list
'''

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


class LoadListPopUp():
    def __init__(self, parent):
        self.parent = parent
        # bind the load list button in parent
        self.parent.button[0].bind("<ButtonRelease-1>", self.show_pop_up) 

    def show_pop_up(self, event):
        ''' basic window setup (toplevel, make the root inactive,
            white background, company logo at the title bar). The 
            window contains all the widgets in this pop up. the 
            definition of the widgets are in this method.
        '''
        self.window = tk.Toplevel()
        self.window.resizable(False, False)
        self.window.grab_set() # the root is not click-able when top window is present
        self.window.config(bg='white')
        self.window.title('Load List')
        self.window.tk.call('wm', 'iconphoto', self.window._w, self.parent.image_company_logo)

        ''' There are eight rows and three columns
            some columns (specially middle and last column) contain frame with different widgets.
            example, container12 meaning the container is place at row 1 column 2
            The widgets that a container contains is defined in the following comments
        '''
        # row0 contains 
        # label: analysis icon
        # label: name of the analysis 
        # button: info icon

        # 'load_list_message' contains the info messages in a list 
        load_list_message = ['Load a list of already prepared peptide spots',
                             'Displays the length of the peptides of this analysis incl.'
                             + ' local spacers but excl. global spacers',
                             'Define a spacer for all spots of this analysis at the N- and C-terminus'
                             + ' in the One-Letter-Notation without spaces;'
                             + 'special monomers in brackets, i.e GS(BRAC).'
                             + ' It has no effect on the spacers of other analysis or global spacers']
        label_load_list_image = ttk.Label(self.window,
                                          image=self.parent.image[0])
        label_load_list_title = ttk.Label(self.window,
                                          text='Load list of peptides', 
                                          style='title.TLabel')
        button_load_list_info = ttk.Button(self.window,
                                           image=self.parent.image_icon_info, 
                                           cursor="hand2",
                                           command=lambda:messagebox.showinfo(parent=self.window,
                                                                              title="Message", 
                                                                              message=load_list_message[0]),
                                           style='info.TButton')
        label_load_list_image.grid(row=0, column=0, padx=3, pady=3, sticky="N")
        label_load_list_title.grid(row=0, column=1, padx=3, pady=3, sticky="NW")
        button_load_list_info.grid(row=0, column=2, padx=3, pady=3, sticky="NW")

        # row1 contains 
        # label: list of peptides, 
        # container11: label: name of the file
        #              button: load file
        # container12: label: number of peptide sequence + '-mer'
        #              button: info button

        label_load_list_LoP = ttk.Label(self.window,
                                        text='List of peptide')
        container11 = ttk.Frame(self.window)
        label_load_list_file_name = ttk.Label(container11,
                                              text='file name', # modify later
                                              )
        button_load_list_load_file = ttk.Button(container11,
                                                image=self.parent.image_folder, #change later
                                                style='analysis.TButton')
        label_load_list_file_name.grid(row=0, column=0, padx=(50,3), pady=3, sticky="NEWS")
        button_load_list_load_file.grid(row=0, column=1, padx=3, pady=1, sticky="NSW")

        container12 = ttk.Frame(self.window)        
        label_load_list_mer = ttk.Label(container12,
                                        text='num') # modify later ''+'-mer'
        button_load_list_info_row1 = ttk.Button(container12,
                                                image=self.parent.image_icon_info, #change later
                                                cursor="hand2",
                                                command=lambda:messagebox.showinfo(parent=self.window,
                                                                                   title="Message", 
                                                                                   message=load_list_message[1]),
                                                style='info.TButton')
        label_load_list_mer.grid(row=0, column=0, padx=3, pady=3, sticky="NSW")
        button_load_list_info_row1.grid(row=0, column=1, padx=3, pady=1, sticky="NSW")

        label_load_list_LoP.grid(row=1, column=0, padx=(15,0), pady=3, sticky="NSE")
        container11.grid(row=1, column=1, sticky="NSW")        
        container12.grid(row=1, column=2, sticky="NSW")

        # (row2) contains
        # label: N-spacer
        # container21: label: N-
        #              entry: entry_n spacer
        #              label:-c
        #              button: info button
        # label: image & N terminal

        container21 = ttk.Frame(self.window)
        label_N_21 = ttk.Label(container21,
                             text='N-',
                             foreground="#%02x%02x%02x" % (191, 191, 191))
        entry_load_list_N_spacer = ttk.Entry(container21)
        label_C_21 = ttk.Label(container21,
                             text='-C',
                             foreground="#%02x%02x%02x" % (191, 191, 191))
        button_load_list_info_row2 = ttk.Button(container21,
                                                image=self.parent.image_icon_info, #change later
                                                cursor="hand2",
                                                command=lambda:messagebox.showinfo(parent=self.window,
                                                                                   title="Message", 
                                                                                   message=load_list_message[2]),
                                                style='info.TButton')
        label_N_21.grid(row=0, column=0)
        entry_load_list_N_spacer.grid(row=0, column=1)
        label_C_21.grid(row=0, column=2)
        button_load_list_info_row2.grid(row=0, column=3)

        label_load_list_Nspacer_text = ttk.Label(self.window,
                                                text='N-spacer')
        label_load_list_N_terminal_image = ttk.Label(self.window,
                                                    text='N-Terminal Spacer',
                                                    image=self.parent.image_peptide_part1,
                                                    compound='left',
                                                    style='image.TLabel')
        label_load_list_Nspacer_text.grid(row=2, column=0, sticky="NSE")
        container21.grid(row=2, column=1)
        label_load_list_N_terminal_image.grid(row=2, column=2, sticky="W")

        # row3
        ttk.Separator(self.window).grid(row=3, column=0, columnspan=3, padx=15, sticky="EW")

        # (row4) contains
        # label: peptide image
        ttk.Label(self.window,
                  text='pertide',
                  image=self.parent.image_peptide_part2,
                  compound='left',
                  style='image.TLabel').grid(row=4, column=2, sticky="W")
        # row5
        ttk.Separator(self.window).grid(row=5, column=0, columnspan=3, padx=15, sticky="EW")

        # (row6) contains
        # label: C-spacer
        # container61: label: N-
        #              entry: entry_c spacer
        #              label:-C
        #              button: info button
        # label: image & C terminal

        container61 = ttk.Frame(self.window)
        label_N_61 = ttk.Label(container61,
                             text='N-',
                             foreground="#%02x%02x%02x" % (191, 191, 191))
        entry_load_list_C_spacer = ttk.Entry(container61)
        label_C_61 = ttk.Label(container61,
                             text='-C',
                             foreground="#%02x%02x%02x" % (191, 191, 191))
        button_load_list_info_row6 = ttk.Button(container61,
                                                image=self.parent.image_icon_info, #change later
                                                cursor="hand2",
                                                command=lambda:messagebox.showinfo(parent=self.window,
                                                                                   title="Message", 
                                                                                   message=load_list_message[2]),
                                                style='info.TButton')
        label_N_61.grid(row=0, column=0)
        entry_load_list_C_spacer.grid(row=0, column=1)
        label_C_61.grid(row=0, column=2)
        button_load_list_info_row6.grid(row=0, column=3)

        label_load_list_Cspacer_text = ttk.Label(self.window,
                                                text='C-spacer')
        label_load_list_C_terminal_image = ttk.Label(self.window,
                                                    text='C-Terminal Spacer',
                                                    image=self.parent.image_peptide_part1,
                                                    compound='left',
                                                    style='image.TLabel')
        label_load_list_Cspacer_text.grid(row=6, column=0, sticky="NSE")
        container61.grid(row=6, column=1)
        label_load_list_C_terminal_image.grid(row=6, column=2, padx=(0,15), sticky="W")

        # (row7) contains
        # label: surface image
        ttk.Label(self.window,
                  text='surface',
                  image=self.parent.image_peptide_part2,
                  compound='left',
                  style='image.TLabel').grid(row=7, column=2, sticky="NW")

        # (row7) contains
        # container: cancel button
        #            add button
        container71 = ttk.Frame(self.window)
        container71.grid(row=8, column=1)
        button_load_list_cancel = ttk.Button(container71,
                                             text='Cancel',
                                             command=self.window.destroy,
                                             style='cancel.TButton')
        button_load_list_add = ttk.Button(container71,
                                             text='Add')
        button_load_list_cancel.grid(row=0, column=0, padx=(15,3), pady=3)
        button_load_list_add.grid(row=0, column=1, padx=3, pady=3)
        
        