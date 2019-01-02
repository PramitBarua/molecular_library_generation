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
            self.display_frame.grid(row=0, column=1, padx=5, pady=5, sticky='NW')
    
            # run frame (this frame should contain all other general frames
            # such as (run, close))
            self.run_frame = tk.Frame(self.master)
            self.run_frame.grid(row=1, column=1, padx=5, pady=5, sticky='SE')
    
            # calling methods
            self.overlap_sequence_frame()
            self.overlap_sequence_frame()
            self.display()
            self.Run()

        def overlap_sequence_frame(self):
            '''
            this method contains the widget of
            overlap block
            '''
            # check box overlap
            label_overlap_title = tk.Label(self.overlap_frame,
                                      text="Overlap Sequence", 
                                      width=40)
            label_overlap_title.grid(row=0, column=0, columnspan=2, padx=3, pady=3, sticky="NW")
    
            # button overlap add
            self.button_overlap_add = tk.Button(self.overlap_frame,
                                                text="Add",
                                                state='disable',
                                                command = self.overlap_add, 
                                                width = 15,
                                                cursor="hand2")
            self.button_overlap_add.grid(row=1, column=1, padx=3, pady=3, sticky="NW")
    
            # Button overlap txt file
            self.button_overlap_seq = tk.Button(self.overlap_frame,
                                                text="Select File",
                                                command = lambda: self.file_browser('Overlap'), 
                                                width = 15,
                                                cursor="hand2")
            self.button_overlap_seq.grid(row=1, column=0, padx=3, pady=3, sticky="NW")
    
            # Entry overlap peptide length
            label_overlap_peptide_len = tk.Label(self.overlap_frame,
                                      text="Peptide Length", 
                                      width=16)
            label_overlap_peptide_len.grid(row=2, column=0, padx=3, pady=3, sticky="NW")
            self.entry_overlap_peptide_len = tk.Entry(self.overlap_frame,
                                                width = 15,
                                                cursor="hand2")
            self.entry_overlap_peptide_len.grid(row=2, column=1, padx=3, pady=3, sticky="NW")
            self.entry_overlap_peptide_len.bind("<Return>", self.overlap_add_open)
            self.entry_overlap_peptide_len.bind("<Button-1>", self.overlap_add_open)
    
            # Entry overlap shift step
            label_overlap_shift_step = tk.Label(self.overlap_frame,
                                      text="Shift Steps", 
                                      width=16)
            label_overlap_shift_step.grid(row=3, column=0, padx=3, pady=3, sticky="NW")
            self.entry_overlap_shift_step = tk.Entry(self.overlap_frame,
                                                width = 15,
                                                cursor="hand2")
            self.entry_overlap_shift_step.grid(row=3, column=1, padx=3, pady=3, sticky="NW")
            self.entry_overlap_shift_step.bind("<Return>", self.overlap_add_open)
            self.entry_overlap_shift_step.bind("<Button-1>", self.overlap_add_open)
    
        def readPortfolioFile(self):
            print('readPortfolioFile')
    
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
            self.button_overlap_seq.config(bg='Green')
            self.overlap_add_open(0)
    
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
    
        def display(self):
            scrollbar = tk.Scrollbar(self.display_frame, orient="vertical", width=20)
            scrollbar.grid(row=0,column=4, sticky="ns")
    
            self.treeTable = ttk.Treeview(self.display_frame, height='7', selectmode="extended")
            self.treeTable.grid(row=0, column=0, columnspan=2, sticky="n")
            self.treeTable['columns']=['Name', 'Contribution', 'Times']
    
            self.treeTable.column('Name', width=100, stretch=False)
            self.treeTable.column('Contribution', width=100)
            self.treeTable.column('Times', width=100)
            self.treeTable.column('#0', minwidth=0, width=0) #width 0 to not display it
    
            self.treeTable.heading('Name', text='Name')
            self.treeTable.heading('Contribution', text='Contribution')
            self.treeTable.heading('Times', text='Times')
    
            total_num_peptide = 0
            for key in self.GUI_data.keys():
                buf = [self.GUI_data[key]['Analysis_Name'], self.GUI_data[key]['Num_Peptide'], self.GUI_data[key]['Multiple']] 
                total_num_peptide += (self.GUI_data[key]['Num_Peptide']
                                      * self.GUI_data[key]['Multiple'])                 
                self.treeTable.insert('', 'end', text='%s' % key, values=buf)
    
            self.treeTable.bind("<Double-1>", self.OnDoubleClick)
            self.treeTable.bind("<Shift-Button-1>", self.mul_window)
            self.treeTable.bind("<Button-3>", self.display_window)
#             multiple_editor_fun
            
            # showing total contribution
            label_total_contribution_name=tk.Label(self.display_frame,
                                                   text="Total", 
                                                   width=10)
            label_total_contribution_name.grid(row=1,column=0, sticky="n")
            label_total_contribution_value=tk.Label(self.display_frame,
                                                   text=str(total_num_peptide), 
                                                   width=10)
            label_total_contribution_value.grid(row=1,column=1, sticky="n")

        def OnDoubleClick(self, event):
            item = self.treeTable.identify('item', event.x, event.y)
            if item:
                key = int(self.treeTable.item(item, "text"))
                del self.GUI_data[key]
                self.display()

        def mul_window(self, event):
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
            try:
                self.GUI_data[key]['Multiple'] = int(self.entry_mul.get())
                self.window.destroy()
                self.display()
            except ValueError:
                pass

        def display_window(self, event):
            event_item = self.treeTable.identify('item', event.x, event.y)
            if event_item:
                key = int(self.treeTable.item(event_item, "text"))
                self.window = tk.Toplevel(root)
                self.window.title('Display')
                self.window.geometry("405x200+50+55")
                buf = self.GUI_data[key]['Data']
                value = [buf[i:i+4] for i in range(0, len(buf), 4)]
                treeTable = ttk.Treeview(self.window, height='7', selectmode="extended")
                treeTable.grid(row=0, column=0, columnspan=2, sticky="n")
                treeTable['columns'] = ['1', '2', '3', '4']

                treeTable.column('1', width=100, stretch=False)
                treeTable.column('2', width=100)
                treeTable.column('3', width=100)
                treeTable.column('4', width=100)
                treeTable.column('#0', minwidth=0, width=0)
                for item in value:
                    treeTable.insert('', 'end', values=item)
                treeTable.bind("<Button-1>", lambda event: self.window.destroy())

        def Run(self):
            # run button
            button_run = tk.Button(self.run_frame,
                                    text="Run",
                                    command=self.readPortfolioFile, 
                                    width=15,
                                    cursor="hand2")
            button_run.grid(row=0, column=0, padx=3, pady=3, sticky="NE")
    
            # close button
            button_close = tk.Button(self.run_frame,
                                    text="Close",
                                    command=self.master.destroy,
                                    width=15,
                                    cursor="hand2")
            button_close.grid(row=0, column=1, padx=3, pady=3, sticky="NE")
    
    root = tk.Tk()
    # Make window 600x570 and place at position (150,75)
    root.geometry("700x570+50+55")
    my_gui = Library_generation_cls(root)
    root.mainloop()

if __name__ == '__main__':
    Library_generation_fun()