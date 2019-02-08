#!/usr/bin/env python3
from library_generation_package import load_list, library_generation_style,\
    overlapping

__author__ = "Pramit Barua"
__copyright__ = "Copyright 2019, IMT, KIT"
__credits__ = ["Pramit Barua"]
__license__ = "IMT, KIT"
__version__ = "3"
__maintainer__ = "Pramit Barua"
__email__ = ["pramit.barua@student.kit.edu", "pramit.barua@gmail.com"]

'''
The software starts from here
All the functionality in the main window (parent) controls from this scripts
The parent window is organized in three frames, namely left, middle and
right frame. 
The left frame contains the button for individual 
analysis and the display list
The middle frame
The right frame
'''

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox, IntVar
import numpy as np  
import os
import sys


import library_generation_package


class Hover_Message():
    """
    create a hover message for a given widget
    """
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.wraplength = 180   #pixels
        self.tw = None

        self.widget.bind('<Enter>', self.show)
        self.widget.bind('<Leave>', self.hide)

    def show(self, event):
        x = event.x_root
        y = event.y_root

        # creates a toplevel window
        self.tw = tk.Toplevel()
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                         background="#ffffff", relief='solid', borderwidth=1,
                         wraplength=self.wraplength)
        label.pack(ipadx=1)

    def hide(self, event):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()


class Library_generation_cls(tk.Tk):
    def __init__(self):
        '''
        This init method contains the basic design
        such as (window size) of 
        '''
        super().__init__()
        self.config(bg='white')
        library_generation_style.style_config() # change style
        self.root_width = self.winfo_screenwidth() # get the user monitor width
        self.root_height = self.winfo_screenheight() # get the user monitor height
        self.image_dimention_analysis = int(self.root_width/265) # dimention for image in analysis button
        self.image_dimention_button = int(self.root_width/450) # dimentaion of image in button(edit, delete and info)
        self.button_dimention = 12 # analysis button dimention with respect to window size

        # image load
        self.image = []
        self.path = '../library_generation/image'
        self.image_company_logo = tk.PhotoImage(file=os.path.join(self.path, 'Logo_axxelera.png'))
        self.image_icon_info = tk.PhotoImage(file=os.path.join(self.path, 'icon_info.png')) # image of info icon
        self.image_icon_info = self.image_icon_info.subsample(self.image_dimention_button,self.image_dimention_button)
        self.image_folder = tk.PhotoImage(file=os.path.join(self.path, 'Folder.png')) # image of Folder
        self.image_folder = self.image_folder.subsample(self.image_dimention_button,self.image_dimention_button)
        self.image_peptide_part1 = tk.PhotoImage(file=os.path.join(self.path, '3_part_Peptide_part1.png')) # image of N-terminal
        self.image_peptide_part1 = self.image_peptide_part1.subsample(self.image_dimention_button,self.image_dimention_button)
        self.image_peptide_part2 = tk.PhotoImage(file=os.path.join(self.path, '3_part_Peptide_part2.png')) # image of peptide
        self.image_peptide_part2 = self.image_peptide_part2.subsample(self.image_dimention_button,self.image_dimention_button)

        self.title("Library Generation")
        self.state('zoomed')
        self.tk.call('wm', 'iconphoto', self._w, self.image_company_logo) # change logo

        # left container
        self.left_container = ttk.Frame(self, style="TFrame")
        self.left_container.pack(side='top', anchor='w')
        self.button = [] # contains the analysis buttons
        # center frame
        self.center_container = ttk.Frame(self, style="TFrame")
        self.center_container.pack(side='left', fill='x')
        # right frame
        self.right_container = ttk.Frame(self, style="TFrame")#, bg=WINDOW_BACKGROUND_COLOR)
        self.right_container.pack(side='left', fill='x')

        # calling frames
        self.left_container_fun()

    def left_container_fun(self):
        '''
        this container contains two frames (button frame and list frame).
        button frame contains the buttons of the analysis
        list frame contains the display list
        '''

        # this frame contains buttons of different analysis
        button_frame = ttk.Frame(self.left_container, style='TFrame')
        button_frame.pack(side='top')

        image_list = ['Icon_Load_List.png',
                      'Icon_Overlapping.png',
                      'Icon_Substitution.png',
                      'Icon_Discontinuous.png',
                      'Icon_Random.png',
                      'Icon_Combinatorial.png']

        text_list = ['Load List',
                     'Overlapping',
                     'Substitution',
                     'Discontinuous',
                     'Random',
                     'Combinatorial']

        opts = {'cursor': "hand2",
                'compound': 'top',
                'style': 'analysis.TButton'}

        for ind, (image, text) in enumerate(zip(image_list, text_list)):
            self.image.append(tk.PhotoImage(file=os.path.join(self.path, image)))
            self.image[ind] = self.image[ind].subsample(self.image_dimention_analysis, self.image_dimention_analysis)
            self.button.append(ttk.Button(button_frame,
                                          text=text,
                                          image=self.image[ind],
                                          **opts))

        # placement of button in left container
        opts = {}
        opts = {'padx': 5, 'pady':'10'}
        self.button[0].grid(row=0, column=0, **opts) # Load List
        self.button[1].grid(row=0, column=1, **opts) # Overlapping
        self.button[2].grid(row=0, column=2, **opts) # Substitution
        self.button[3].grid(row=1, column=0, **opts) # Discontinuous
        self.button[4].grid(row=1, column=1, **opts) # Random
        self.button[5].grid(row=1, column=2, **opts) # Combinatorial

        # this frame contains the list
        list_frame = ttk.Frame(self.left_container, style='TFrame')
        list_frame.pack(padx=5, pady=10, side='top')

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical")
        scrollbar.grid(row=0, column=4, sticky="ns")

        self.treeTable = ttk.Treeview(list_frame, height=int(self.root_height/32), selectmode="browse")
        self.treeTable.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.treeTable['columns'] = ['Type', 'Multiplicator', 'Spots']

        self.treeTable.column('Type', width=int(self.root_width/self.button_dimention), stretch = True)
        self.treeTable.column('Multiplicator', width=int(self.root_width/self.button_dimention))
        self.treeTable.column('Spots', width=int(self.root_width/self.button_dimention))
        self.treeTable.column('#0', minwidth=0, width=0)  # width 0 to not display it

        self.treeTable.heading('Type', text='Type', image=self.image_icon_info)
        self.treeTable.heading('Multiplicator', text='Multiplicator', image=self.image_icon_info)
        self.treeTable.heading('Spots', text='#Spots', image=self.image_icon_info)

        # call pop up
        load_list.LoadListPopUp(self)
        overlapping.OverlappingPopUp(self)

if __name__ == '__main__':
    my_gui = Library_generation_cls()
    my_gui.mainloop()