""" Create a Tkinter gui
    this script is executed in the gui_main.py file

Created on: 06.03.2021
Last Revision: 07.03.2021
@author: Max Weise
"""

from tkinter import *
from tkinter import ttk

class GUI(object):
    def __init__(self):
        # Global attrebutes
        self.__left_margin = 20

        # Create a non resizable window
        self.root = Tk()
        self.root.title('Backup Automation')
        self.root.geometry('600x200')
        self.root.resizable(0, 0)
        self.back = Frame(master=self.root)
        self.back.pack(padx=5, pady=5)
        
        # Labels
        self.label1 = Label(self.root, text='Please provide a source and destination folder')
        self.label1.place(x=self.__left_margin, y=5)
        
        self.label2 = Label(self.root, text='Please choose backup procedure to backup your files')
        self.label2.place(x=self.__left_margin, y=100)
        # Buttons
        chose_src = Button(self.root, text='Browse')
        chose_src.place(x=self.__left_margin, y=30)
        
        chose_dst = Button(self.root, text='Browse')
        chose_dst.place(x=self.__left_margin, y=70)
        
        start_procedure = Button(self.root, text='Start')
        start_procedure.place(x=self.__left_margin, y=150)
        
        cancle_button = Button(self.root, text='Cancle', command=self.cancle)
        cancle_button.place(x=self.__left_margin + 80, y=150)

        # Textboxes
        show_src_path = Text(self.root, height=1, width=50)
        show_src_path.place(x=80, y=30)

        show_dst_path = Text(self.root, height=1, width=50)
        show_dst_path.place(x=80, y=70)

        # Radiobuttons
        procedure = StringVar()
        f_backup = ttk.Radiobutton(self.root, text='File Backup', variable=procedure, value='File Backup')
        f_backup.place(x=self.__left_margin, y=120)

        ft_backup = ttk.Radiobutton(self.root, text='File Type Backup', variable=procedure, value='File Type Backup')
        ft_backup.place(x=self.__left_margin + 150, y=120)

    # def cancle():
    #     self.label1.set('Test')

    def run(self):
        self.root.mainloop()

def run_gui():
    # Functions on button press

    
    root.mainloop() # display the gui