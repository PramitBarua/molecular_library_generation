#!/usr/bin/env python3

__author__ = "Pramit Barua"
__copyright__ = "Copyright 2019, IMT, KIT"
__credits__ = ["Pramit Barua"]
__license__ = "IMT, KIT"
__version__ = "3"
__maintainer__ = "Pramit Barua"
__email__ = ["pramit.barua@student.kit.edu", "pramit.barua@gmail.com"]

'''
The program is organized in three frames, namely left, middle and
right frame. The left frame contains the button for individual 
analysis and the display list
'''

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox, IntVar
import numpy as np  
import re


def style_config():
    STYLE = ttk.Style()
#     print(STYLE.layout('Treeview'))
    
#     setting={
#         "TFrame" :          {"configure" :      {"background":'white'}},
#         'default.TButton' : {"configure" :      {'background':"#%02x%02x%02x" % (0, 144, 215),
#                                                  'foreground':'white',
#                                                  'font':('Muli', 12),
#                                                  'relief':'flat'}},
#                             "map" :             {'foreground':[('disabled', 'gray'),
#                                                                ('pressed', 'white'),
#                                                                ('active', 'white')],
#                                                  'background':[('disabled', 'white'),
#                                                                ('pressed', "#%02x%02x%02x" % (0, 73, 108)), 
#                                                                ('active', "#%02x%02x%02x" % (0, 144, 168))]},
#         "default.TLabel" :  {"configure" :     {'background':'white',
#                                               'foreground':"#%02x%02x%02x" % (191, 191, 191),
#                                               'font':('Muli', 12),
#                                               'relief':'flat'},
#                             "map":           {'foreground':[('disabled', 'gray'),
#                                                             ('pressed', 'white'),
#                                                             ('active', 'white')],
#                                               'background':[('disabled', 'white'),
#                                                             ('pressed', "#%02x%02x%02x" % (0, 73, 108)), 
#                                                             ('active', "#%02x%02x%02x" % (0, 144, 168))]}},
#         'analysis.TButton':{'configure':      {'background':'white',
#                                                'foreground':"#%02x%02x%02x" % (191, 191, 191),
#                                                'font':('Muli', 12),
#                                                'relief':'flat'}},
#                             'map':{'foreground':[('disabled', "#%02x%02x%02x" % (191, 191, 191)),
#                                                  ('pressed', "#%02x%02x%02x" % (191, 191, 191)),
#                                                  ('active', "#%02x%02x%02x" % (191, 191, 191))],
#                                    'background':[('disabled', 'white'),
#                                                  ('pressed', 'white'),
#                                                  ('active', 'white')]}
# #         'default.Treeview':{}
#                         }
#     STYLE.theme_create('main_theme', parent="clam", settings=setting)
#     STYLE.theme_use('main_theme')

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


class LoadListPopUp():
    def __init__(self, parent):
        self.parent = parent
        self.parent.button_load_list.bind("<ButtonRelease-1>", self.show_pop_up)
        self.tw = None

    def show_pop_up(self, event):
        ''' basic window setup (toplevel, make the root inactive,
            white background, company logo at the title bar). The 
            window contains all the widgets in this pop up. the 
            definition of the widgets are in this method.
        '''
        self.window = tk.Toplevel()
        self.window.grab_set() # the root is not click-able when top window is present
        self.window.config(bg='white')
        self.window.title('Load List')
        self.window.tk.call('wm', 'iconphoto', self.window._w, self.parent.image_company_logo)

        ''' There are six rows and three columns
            some columns (specially middle and last column) contain frame with different widgets.
            The widgets that a container contains is defined in the following comments 
            example, container12 meaning the container is place at row 1 column 2
        '''
        # row0 contains 
        # label: analysis icon
        # label: name of the analysis 
        # button: info icon

        load_list_message = ['Load a list of already prepared peptide spots',
                             'Displays the length of the peptides of this analysis incl.'
                             + ' local spacers but excl. global spacers',
                             'Define a spacer for all spots of this analysis at the N- and C-terminus'
                             + ' in the One-Letter-Notation without spaces;'
                             + 'special monomers in brackets, i.e GS(BRAC).'
                             + ' It has no effect on the spacers of other analysis or global spacers']
        label_load_list_image = ttk.Label(self.window,
                                          image=self.parent.image_load_list)
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


class OverlapPopUp():
    '''
    pop up window for overlap block
    '''
    def __init__(self, parent):
#         self.wraplength = 180   #pixels
        self.parent = parent
        self.parent.button_overlap.bind("<Button-1>", self.show_pop_up)
        self.tw = None

    def show_pop_up(self, event):
        self.window = tk.Toplevel()
        self.window.grab_set()
        self.window.title('Load List')
        self.window.tk.call('wm', 'iconphoto', self.window._w, self.parent.icon)


class Library_generation_cls(tk.Tk):
    def __init__(self):
        '''
        This init method contains the basic design
        such as (window size) of 
        '''
        super().__init__()
        self.config(bg='white')
        style_config()
        self.root_width = self.winfo_screenwidth() # get the user monitor width
        self.root_height = self.winfo_screenheight() # get the user monitor height
        self.image_dimention_analysis = int(self.root_width/265) # dimention for image in analysis button
        self.image_dimention_button = int(self.root_width/450) # dimentaion of image in button(edit, delete and info)
        self.button_dimention = 12 # analysis button dimention with respect to window size

        # image load
        self.image_company_logo = tk.PhotoImage(file='Logo_axxelera.png')
        self.image_icon_info = tk.PhotoImage(file='icon_info.png') # image of info icon
        self.image_icon_info = self.image_icon_info.subsample(self.image_dimention_button,self.image_dimention_button)
        self.image_folder = tk.PhotoImage(file='Folder.png') # image of Folder
        self.image_folder = self.image_folder.subsample(self.image_dimention_button,self.image_dimention_button)
        self.image_peptide_part1 = tk.PhotoImage(file='3_part_Peptide_part1.png') # image of N-terminal
        self.image_peptide_part1 = self.image_peptide_part1.subsample(self.image_dimention_button,self.image_dimention_button)
        self.image_peptide_part2 = tk.PhotoImage(file='3_part_Peptide_part2.png') # image of peptide
        self.image_peptide_part2 = self.image_peptide_part2.subsample(self.image_dimention_button,self.image_dimention_button)

        self.title("Library Generation")
        self.state('zoomed')        
        self.tk.call('wm', 'iconphoto', self._w, self.image_company_logo) # change logo

        # left container
        self.left_container = ttk.Frame(self, style="TFrame")
        self.left_container.pack(side='top', anchor='w')
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

        # load list button
        self.image_load_list = tk.PhotoImage(file='Icon_Load_List.png')
        self.image_load_list = self.image_load_list.subsample(self.image_dimention_analysis,self.image_dimention_analysis)
        self.button_load_list = ttk.Button(button_frame,
                                           text='Load List',
                                           cursor="hand2",
                                           image=self.image_load_list,
                                           compound='top',
                                           style='analysis.TButton')
 
        # overlap button
        self.image_overlap = tk.PhotoImage(file='Icon_Overlapping.png')
        self.image_overlap = self.image_overlap.subsample(self.image_dimention_analysis,self.image_dimention_analysis)
        self.button_overlap = ttk.Button(button_frame,
                                         text='Overlapping',
                                         cursor="hand2",
                                         image=self.image_overlap,
                                         compound='top',
                                         style='analysis.TButton')
 
        # substitution button
        self.image_subs = tk.PhotoImage(file='Icon_Substitution.png')
        self.image_subs = self.image_subs.subsample(self.image_dimention_analysis,self.image_dimention_analysis)
        self.button_subs = ttk.Button(button_frame,
                                     text='Substitution',
                                     cursor="hand2",
                                     image=self.image_subs, 
                                     compound='top',
                                     style='analysis.TButton')

        # conformational button
        self.image_conf = tk.PhotoImage(file='Icon_Discontinuous.png')
        self.image_conf = self.image_conf.subsample(self.image_dimention_analysis,self.image_dimention_analysis)
        self.button_conf = ttk.Button(button_frame,
                                      text='Discontinuous',
                                      cursor="hand2",
                                      image=self.image_conf,
                                      compound='top',
                                      style='analysis.TButton')

        # random button
        self.image_random = tk.PhotoImage(file='Icon_Random.png')
        self.image_random = self.image_random.subsample(self.image_dimention_analysis,self.image_dimention_analysis)
        self.button_random = ttk.Button(button_frame,
                                        text='Random',
                                        cursor="hand2",
                                        image=self.image_random,
                                        compound='top',
                                        style='analysis.TButton')

        # Combinatorial button
        self.image_comb = tk.PhotoImage(file='Icon_Combinatorial.png')
        self.image_comb = self.image_comb.subsample(self.image_dimention_analysis,self.image_dimention_analysis)
        self.button_comb = ttk.Button(button_frame,
                                      text='Combinatorial',
                                      cursor="hand2",
                                      image=self.image_comb, 
                                      compound='top',
                                      style='analysis.TButton')

        # placement of button in left container
        self.button_load_list.grid(row=0, column=0, padx=5, pady=10)
        self.button_overlap.grid(row=0, column=1, padx=5, pady=10)
        self.button_subs.grid(row=0, column=2, padx=5, pady=10)
        self.button_conf.grid(row=1, column=0, padx=5, pady=10)
        self.button_random.grid(row=1, column=1, padx=5, pady=10)
        self.button_comb.grid(row=1, column=2, padx=5, pady=10)

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

#         self.label_total_spots = tk.Label(list_frame,
#                                           )
        # call pop up
        LoadListPopUp(self)
#         OverlapPopUp(self)

if __name__ == '__main__':
    my_gui = Library_generation_cls()
    my_gui.mainloop()