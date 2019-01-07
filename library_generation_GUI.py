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

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox
import numpy as np

# import library_generation_method.overlapping_sequence_fun as overlap_fun
from library_generation_method import overlapping_sequence_fun as overlap_fun


def Library_generation_fun():
    class Library_generation_cls:
        def __init__(self, master):
            self.master = master
            master.title("Library Generation")

            # 'self.count' works as index of analysis
            self.count = 0
            self.curIndex = None

            # input variable default value
            self.GUI_data = {}
            self.overlap_peptide_len = tk.IntVar()
            self.overlap_shift_step = tk.IntVar()

            # define frame
            # overlap frame
            self.overlap_frame = tk.Frame(self.master, 
                                          highlightbackground="black", 
                                          highlightcolor="black", 
                                          highlightthickness=1,
                                          bd=1)
            self.overlap_frame.grid(row=0, column=0, padx=5, pady=5, sticky='NW')
            self.overlap_frame.bind("<Button-1>", self.overlap_add_open)

            # substitutional frame
            self.substitutional_frame = tk.Frame(self.master,
                                            highlightbackground="black",
                                            highlightcolor="black",
                                            highlightthickness=1,
                                            bd=1)
            self.substitutional_frame.grid(row=1, column=0, padx=5, pady=5, sticky='NW')
 
            # display frame
            self.display_frame = tk.Frame(self.master, 
                                         highlightbackground="black", 
                                         highlightcolor="black", 
                                         highlightthickness=1,
                                         bd=1)
            self.display_frame.grid(row=0, column=1, padx=5, pady=5, rowspan=2, sticky='NW')
 
            # run frame (this frame should contain all other general frames
            # such as (run, close))
            self.run_frame = tk.Frame(self.master)
            self.run_frame.grid(row=2, column=1, padx=5, pady=5, sticky='NW')

            # calling methods
            self.overlap_sequence_frame()
            self.substitutional_analysis_frame()
            self.display()
            self.Run()

        def overlap_sequence_frame(self):
            '''
            this method contains the widget of
            overlap block
            '''

            label_overlap_title = tk.Label(self.overlap_frame,
                                      text="Overlap Sequence", 
                                      width=40)
            label_overlap_title.grid(row=0, column=0, columnspan=2, padx=3, pady=3, sticky="NWSE")
 
            # Button overlap txt file
            self.button_overlap_seq = tk.Button(self.overlap_frame,
                                                text="Select File",
                                                command = lambda: self.file_browser('Overlap'), 
                                                width = 10,
                                                cursor="hand2")
            self.button_overlap_seq.grid(row=1, column=0, padx=3, pady=3, sticky="N")

            # button overlap add
            self.button_overlap_add = tk.Button(self.overlap_frame,
                                                text="Add",
                                                state='disable',
                                                command = self.overlap_add, 
                                                width = 10,
                                                cursor="hand2")
            self.button_overlap_add.grid(row=1, column=1, padx=3, pady=3, sticky="N")

            # Entry overlap peptide length
            label_overlap_peptide_len = tk.Label(self.overlap_frame,
                                      text="Peptide Length", 
                                      width=12)
            label_overlap_peptide_len.grid(row=2, column=0, padx=3, pady=3, sticky="N")
            self.entry_overlap_peptide_len = tk.Entry(self.overlap_frame,
                                                width = 15,
                                                cursor="hand2")
            self.entry_overlap_peptide_len.grid(row=2, column=1, padx=3, pady=3, sticky="N")
            self.entry_overlap_peptide_len.bind("<Return>", self.overlap_add_open)
            self.entry_overlap_peptide_len.bind("<Button-1>", self.overlap_add_open)
 
            # Entry overlap shift step
            label_overlap_shift_step = tk.Label(self.overlap_frame,
                                      text="Shift Steps", 
                                      width=12)
            label_overlap_shift_step.grid(row=3, column=0, padx=3, pady=3, sticky="N")
            self.entry_overlap_shift_step = tk.Entry(self.overlap_frame,
                                                width = 15,
                                                cursor="hand2")
            self.entry_overlap_shift_step.grid(row=3, column=1, padx=3, pady=3, sticky="N")
            self.entry_overlap_shift_step.bind("<Return>", self.overlap_add_open)
            self.entry_overlap_shift_step.bind("<Button-1>", self.overlap_add_open)

        def readPortfolioFile(self):
            print('readPortfolioFile')

        def overlap_add_open(self, event):
            check = True
            try:
                if self.GUI_data[self.count]['Analysis_Name'] != 'Overlap':
                    check = False
            except:
                check = False
            try:
                self.GUI_data[self.count]['Peptide_Len'] = int(self.entry_overlap_peptide_len.get())
            except:
                check = False
            try:
                self.GUI_data[self.count]['Shift_Step'] = int(self.entry_overlap_shift_step.get())
            except:
                check = False
            if check:
                self.button_overlap_add.config(state="normal")
 
        def overlap_add(self):
            self.GUI_data[self.count]['Multiple'] = 1
            path_ = self.GUI_data[self.count]['Path']
            if path_:
                length_peptide = self.GUI_data[self.count]['Peptide_Len']
                overlapSteps = self.GUI_data[self.count]['Shift_Step']
                buf = overlap_fun(path_, overlapSteps, length_peptide)
                self.GUI_data[self.count]['Num_Peptide'] = len(buf)
                self.GUI_data[self.count]['Data'] = buf
        #         self.overlap_seq_count()
                self.display()
                self.entry_overlap_peptide_len.delete(0, 'end')
                self.entry_overlap_shift_step.delete(0, 'end')
                self.button_overlap_seq.config(bg='SystemButtonFace')
                self.button_overlap_add.config(state='disable')
                self.count += 1

        def substitutional_analysis_frame(self):
            '''
            this method contains the widget of
            overlap block
            '''
            label_subs_title = tk.Label(self.substitutional_frame,
                                           text="Substitutional Analysis",
                                            width=40)
            label_subs_title.grid(row=0, column=0, columnspan=10, padx=3, pady=3, sticky="NWSE")

            # Button overlap txt file
            self.button_subs_txt = tk.Button(self.substitutional_frame,
                                                text="Select File",
                                                command=lambda: self.file_browser('Substitutional'), 
                                                width=10,
                                                cursor="hand2")
            self.button_subs_txt.grid(row=1, column=1, padx=3, pady=3, sticky="EW")

            # button overlap add
            self.button_subs_add = tk.Button(self.substitutional_frame,
                                                text="Add",
                                                state='disable',
                                                command=self.overlap_add, 
                                                width=10,
                                                cursor="hand2")
            self.button_subs_add.grid(row=1, column=3, padx=3, pady=3, sticky="EW")
            
            # substitutional AA frame
            subs_AA_frame = tk.Frame(self.substitutional_frame)
            subs_AA_frame.grid(row=2, column=0, columnspan=5, sticky='NWSE')
 
            #sub A
            self.subs_check_button_A = tk.Checkbutton(subs_AA_frame,
                                                      text="A")
            self.subs_check_button_A.grid(row=0, column=0, sticky="NWSE")
            self.subs_check_button_A.select()
            #sub C
            self.subs_check_button_C = tk.Checkbutton(subs_AA_frame,
                                                      text="C")
            self.subs_check_button_C.grid(row=0, column=1, sticky="NWSE")
            self.subs_check_button_C.select()
            #sub D
            self.subs_check_button_D = tk.Checkbutton(subs_AA_frame,
                                                      text="D")
            self.subs_check_button_D.grid(row=0, column=2, sticky="NWSE")
            self.subs_check_button_D.select()
            #sub E
            self.subs_check_button_E = tk.Checkbutton(subs_AA_frame,
                                                      text="E")
            self.subs_check_button_E.grid(row=0, column=3, sticky="NWSE")
            self.subs_check_button_E.select()
            #sub F
            self.subs_check_button_F = tk.Checkbutton(subs_AA_frame,
                                                      text="F")
            self.subs_check_button_F.grid(row=0, column=4, sticky="NWSE")
            self.subs_check_button_F.select()
            #sub G
            self.subs_check_button_G = tk.Checkbutton(subs_AA_frame,
                                                      text="G")
            self.subs_check_button_G.grid(row=0, column=5, sticky="NWSE")
            self.subs_check_button_G.select()
            #sub H
            self.subs_check_button_H = tk.Checkbutton(subs_AA_frame,
                                                      text="H")
            self.subs_check_button_H.grid(row=0, column=6, sticky="NWSE")
            self.subs_check_button_H.select()
            #sub I
            self.subs_check_button_I = tk.Checkbutton(subs_AA_frame,
                                                      text="I")
            self.subs_check_button_I.grid(row=0, column=7, sticky="NWSE")
            self.subs_check_button_I.select()
            #sub K
            self.subs_check_button_K = tk.Checkbutton(subs_AA_frame,
                                                      text="K")                                            
            self.subs_check_button_K.grid(row=0, column=8, sticky="NWSE")
            self.subs_check_button_K.select()
            #sub L
            self.subs_check_button_L = tk.Checkbutton(subs_AA_frame,
                                                      text="L")
            self.subs_check_button_L.grid(row=0, column=9, sticky="NWSE")
            self.subs_check_button_L.select()
            #sub M
            self.subs_check_button_M = tk.Checkbutton(subs_AA_frame,
                                                      text="M")
            self.subs_check_button_M.grid(row=1, column=0, sticky="NWSE")
            self.subs_check_button_M.select()
            #sub N
            self.subs_check_button_N = tk.Checkbutton(subs_AA_frame,
                                                      text="N")
            self.subs_check_button_N.grid(row=1, column=1, sticky="NWSE")
            self.subs_check_button_N.select()
            #sub I
            self.subs_check_button_P = tk.Checkbutton(subs_AA_frame,
                                                      text="P")
            self.subs_check_button_P.grid(row=1, column=2, sticky="NWSE")
            self.subs_check_button_P.select()
            #sub K
            self.subs_check_button_Q = tk.Checkbutton(subs_AA_frame,
                                                      text="Q")                                            
            self.subs_check_button_Q.grid(row=1, column=3, sticky="NWSE")
            self.subs_check_button_Q.select()
            #sub L
            self.subs_check_button_R = tk.Checkbutton(subs_AA_frame,
                                                      text="R")
            self.subs_check_button_R.grid(row=1, column=4, sticky="NWSE")
            self.subs_check_button_R.select()
            #sub M
            self.subs_check_button_S = tk.Checkbutton(subs_AA_frame,
                                                      text="S")
            self.subs_check_button_S.grid(row=1, column=5, sticky="NWSE")
            self.subs_check_button_S.select()
            #sub N
            self.subs_check_button_T = tk.Checkbutton(subs_AA_frame,
                                                      text="T")
            self.subs_check_button_T.grid(row=1, column=6, sticky="NWSE")
            self.subs_check_button_T.select()
            #sub I
            self.subs_check_button_V = tk.Checkbutton(subs_AA_frame,
                                                      text="V")
            self.subs_check_button_V.grid(row=1, column=7, sticky="NWSE")
            self.subs_check_button_V.select()
            #sub K
            self.subs_check_button_W = tk.Checkbutton(subs_AA_frame,
                                                      text="W")                                            
            self.subs_check_button_W.grid(row=1, column=8, sticky="NWSE")
            self.subs_check_button_W.select()
            #sub L
            self.subs_check_button_Y = tk.Checkbutton(subs_AA_frame,
                                                      text="Y")
            self.subs_check_button_Y.grid(row=1, column=9, sticky="NWSE")
            self.subs_check_button_Y.select()

             # Entry overlap peptide length
            label_substitutional_peptide_len = tk.Label(self.substitutional_frame,
                                                        text="Peptide Length", 
                                                        width=12)
            label_substitutional_peptide_len.grid(row=7, column=1, padx=3, pady=3, sticky="EW")
            self.entry_substitutional_peptide_len = tk.Entry(self.substitutional_frame,
                                                             width=15,
                                                             cursor="hand2")
            self.entry_substitutional_peptide_len.grid(row=7, column=3, padx=3, pady=3, sticky="EW")
#             self.entry_overlap_peptide_len.bind("<Return>", self.overlap_add_open)
#             self.entry_overlap_peptide_len.bind("<Button-1>", self.overlap_add_open)
#     
#             # Entry overlap shift step
            label_substitutional_shift_step = tk.Label(self.substitutional_frame,
                                                       text="Shift Steps", 
                                                       width=12)
            label_substitutional_shift_step.grid(row=8, column=1, padx=3, pady=3, sticky="EW")
            self.entry_substitutional_shift_step = tk.Entry(self.substitutional_frame,
                                                            width=15,
                                                            cursor="hand2")
            self.entry_substitutional_shift_step.grid(row=8, column=3, padx=3, pady=3, sticky="EW")
#             self.entry_overlap_shift_step.bind("<Return>", self.overlap_add_open)
#             self.entry_overlap_shift_step.bind("<Button-1>", self.overlap_add_open)

        def file_browser(self, analysis_name):
            '''
            This method reads the txt file
            and returns line/s of the file in a list form
            '''
            path_ = filedialog.askopenfilename()
 
            buf = {}
            buf['Analysis_Name'] = analysis_name
            buf['Path'] = path_
 
            self.GUI_data[self.count] = buf
            if analysis_name == 'Overlap':
                self.button_overlap_seq.config(bg='Green')
                self.overlap_add_open(0)
 
        def display(self):
            '''Contains the widget of the displayed list '''
            scrollbar = tk.Scrollbar(self.display_frame, orient="vertical", width=20)
            scrollbar.grid(row=0, column=4, sticky="ns")
 
            self.treeTable = ttk.Treeview(self.display_frame, height=7, selectmode="browse")
            self.treeTable.grid(row=0, column=0, columnspan=3, sticky="n")
            self.treeTable['columns']=['Name','Contribution','Times']
 
            self.treeTable.column('Name', width=100, stretch=False)
            self.treeTable.column('Contribution', width=100)
            self.treeTable.column('Times', width=100)
            self.treeTable.column('#0', minwidth=0, width=0)  # width 0 to not display it
 
            self.treeTable.heading('Name', text='Name')
            self.treeTable.heading('Contribution', text='Contribution')
            self.treeTable.heading('Times', text='Times')
 
            total_num_peptide = 0
            for key in self.GUI_data.keys():
                buf = [self.GUI_data[key]['Analysis_Name'],
                       self.GUI_data[key]['Num_Peptide'],
                       self.GUI_data[key]['Multiple']]
                total_num_peptide += (self.GUI_data[key]['Num_Peptide']
                                      * self.GUI_data[key]['Multiple'])
                self.treeTable.insert('', 'end', text='%s' % key, values=buf)
 
            # showing total contribution
            label_total_contribution_name = tk.Label(self.display_frame,
                                                     text="Total", 
                                                     width=10)
            label_total_contribution_name.grid(row=1, column=0, sticky="n")
            label_total_contribution_value = tk.Label(self.display_frame,
                                                      text=str(total_num_peptide), 
                                                      width=10)
            label_total_contribution_value.grid(row=1, column=1, sticky="n")
 
            # double left click for delete item
            self.treeTable.bind("<Double-1>", self.OnDoubleClick)
            # shift+left_click edit window
            self.treeTable.bind("<Shift-Button-1>", self.mul_window)
            # shift+left_click info window
            self.treeTable.bind("<Button-3>", self.display_window)
 
            self.treeTable.bind('<Control-Button-1>', self.setCurrent)
            self.treeTable.bind('<Control-ButtonRelease-1>', self.shiftSelection)
 
        def OnDoubleClick(self, event):
            '''Method to delete item in the displayed list '''
            item = self.treeTable.identify('item', event.x, event.y)
            if item:
                key = int(self.treeTable.item(item, "text"))
                del self.GUI_data[key]
                self.display()
 
        def setCurrent(self, event):
            ''' Select the 1st item to change
            the sequence in the displayed list '''
            self.curIndex = (event.x, event.y)
 
        def shiftSelection(self, event):
            ''' change the sequence in the displayed list'''
            total_key = list(self.GUI_data.keys())
 
            # define the edited position
            current_item = self.treeTable.identify('item', event.x, event.y)
            if current_item:
                current_key = int(self.treeTable.item(current_item, "text"))
            else:
                current_key = total_key[-1]
 
            # check the old key
            old_item = self.treeTable.identify('item', self.curIndex[0], self.curIndex[1]) 
            try:
                old_key = int(self.treeTable.item(old_item, "text"))
            except ValueError:
                old_key = total_key[-1]
 
            start = total_key.index(old_key)
            end = total_key.index(current_key)
            if old_key > current_key:
                while(start != end):
                    buf = self.GUI_data[total_key[start]]
                    self.GUI_data[total_key[start]] = self.GUI_data[total_key[start-1]]
                    self.GUI_data[total_key[start-1]] = buf
                    start -= 1
            else:
                while(start != end):
                    buf = self.GUI_data[total_key[start]]
                    self.GUI_data[total_key[start]] = self.GUI_data[total_key[start+1]]
                    self.GUI_data[total_key[start+1]] = buf
                    start += 1
            self.display()
 
        def mul_window(self, event):
            '''
            pop-up window to edit time field
            '''
            item = self.treeTable.identify('item', event.x, event.y)
            if item:
                key = int(self.treeTable.item(item, "text"))
                self.window = tk.Toplevel(root)
                self.window.title('Muliple')
                self.window.geometry("200x25+50+55")
                level_mul = tk.Label(self.window,
                                     text="Multiple", 
                                     width=10)
                level_mul.grid(row=0, column=0, padx=3, pady=3, sticky="NW")
                self.entry_mul = tk.Entry(self.window,
                                     width = 10,
                                     cursor="hand2")
                self.entry_mul.grid(row=0, column=1, padx=3, pady=3, sticky="NE")
                self.entry_mul.bind("<Return>", lambda event: self.mul_value(event, key))
 
        def mul_value(self, event, key):
            '''
            edit the time field value
            '''
            try:
                self.GUI_data[key]['Multiple'] = int(self.entry_mul.get())
                self.window.destroy()
                self.display()
            except ValueError:
                pass
 
        def display_window(self, event):
            '''
            This method displays the peptide sequence of
            individual analysis
            '''
            event_item = self.treeTable.identify('item', event.x, event.y)
            if event_item:
                key = int(self.treeTable.item(event_item, "text"))
                self.window = tk.Toplevel(root)
                self.window.title('Display')
                self.window.geometry("305x315+50+55")
                buf = self.GUI_data[key]['Data']
                treeTable = ttk.Treeview(self.window, height='14', selectmode="browse")
                treeTable.grid(row=0, column=0, columnspan=2, sticky="n")
                treeTable['columns'] = ['1']
 
                treeTable.column('1', width=200, stretch=False)
                treeTable.column('#0', minwidth=0, width=0)
                for item in buf:
                    treeTable.insert('', 'end', values=item)
                treeTable.bind("<Button-1>", lambda event: self.window.destroy())
 
        def Run(self):
            # run button
            button_run = tk.Button(self.run_frame,
                                    text="Run",
                                    command=self.readPortfolioFile, 
                                    width=10,
                                    cursor="hand2")
            button_run.grid(row=0, column=0, padx=3, pady=3, sticky="NWSE")
     
            # close button
            button_close = tk.Button(self.run_frame,
                                    text="Close",
                                    command=self.master.destroy,
                                    width=10,
                                    cursor="hand2")
            button_close.grid(row=0, column=1, padx=3, pady=3, sticky="NWSE")
    
    root = tk.Tk()
    # Make window 600x570 and place at position (150,75)
    root.geometry("700x570+50+55")
    my_gui = Library_generation_cls(root)
    root.mainloop()

if __name__ == '__main__':
    Library_generation_fun()