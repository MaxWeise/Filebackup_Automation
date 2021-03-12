""" Create a Tkinter gui
    this script is executed in the gui_main.py file

Created on: 06.03.2021
Last Revision: 12.03.2021
@author: Max Weise
"""

# TODO: Refactor the code. Provide public setter mehtods, which change the label text

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory

class __User_Gui(object):
    """ Parent class for all user interfaces

        @authot
            Max Weise
    """
    def __init__(self):
        self.root = Tk()
        self.root.resizable(0, 0)
        self.back = Frame(master=self.root)
        self.back.pack(padx=5, pady=5)

    def run(self):
        """ Run the interface."""
        self.root.mainloop()

class Text_Input_Interface(__User_Gui):
    """ Generate an interface for the user to input text

        @author
            Max Weise
    """
    def __init__(self, title=''):
        super().__init__()
        self.root.title(title)
        self.root.geometry('350x200')

        # Attrebutes
        self.__textbox_content = None

        # Textbox
        self.user_input = Text(self.root, height=1, width=25)
        self.user_input.place(x=50, y=100)

        # Labels
        self.header = Label(self.root, text='Please provide the filetypes (no ".")')
        self.header.place(x=50, y=30)

        # Buttons
        self.start_button = Button(self.root, text='Start', command=self.start_procedure)
        self.start_button.place(x=50, y=150)
        
        self.cancle_button = Button(self.root, text='Cancle', command=self.cancle)
        self.cancle_button.place(x=150, y=150)

    # Getter
    def get_textbox_content(self) -> str:
        """ Return the content of the textbox."""
        return self.__textbox_content
    
    def start_procedure(self):
        """ Set the instance variable and close the window."""
        self.__textbox_content = self.user_input.get('1.0', END)
        self.root.destroy()
       
    def cancle(self):
        """ Close the window and ensure the instance variable yields None."""
        self.__textbox_content = None
        self.root.destroy()

class Yes_No_Interface(__User_Gui):
    """ Simple GUI to authorize a process (using a yes / no answer)

        @author:
            Max Weise
    """
    def __init__(self, title='', header=''):
        self.__confirmation_value = False

        # Create a non resizabel window
        self.root = Tk()
        self.root.title(title)
        self.root.geometry('300x130')
        self.root.resizable(0, 0)
        self.back = Frame(master=self.root)
        self.back.pack(padx=5, pady=5)

        # Labels
        self.header1 = Label(self.root, text=header)
        self.header1.pack()

        # Buttons
        self.start_button = Button(self.root, text='Yes', command=self.set_value_true)
        self.start_button.place(x=120, y=80)
        
        self.cancle_button = Button(self.root, text='No', command=self.set_value_false)
        self.cancle_button.place(x=180, y=80)

    # Getter
    def get_confirmation_value(self) -> bool:
        """ Return the yes/no descition given by the user."""
        return self.__confirmation_value


    def set_value_true(self):
        """ Set the confirmation value to true and close the window."""
        self.__confirmation_value = True
        self.root.destroy()
    
    def set_value_false(self):
        """ Set the confirmation value to false and close the window."""
        self.__confirmation_value = False
        self.root.destroy()

class GUI(__User_Gui):
    """ Initialize a GUI to facilitate the process of backing up files

        @author:
            Max Weise
    """
    def __init__(self):
        """ Initialize a GUI object""" 
        # Create a non resizable window
        self.root = Tk()
        self.root.title('Backup Automation')
        self.root.geometry('600x200')
        self.root.resizable(0, 0)
        self.back = Frame(master=self.root)
        self.back.pack(padx=5, pady=5)
        
        # Strings in labels
        self.display_source = StringVar()
        self.display_source.set('Source :')
        self.display_destin = StringVar() 
        self.display_destin.set('Destination :')

        # Global attrebutes
        self.__left_margin = 20
        self.__procedure = StringVar()
        self.__src_path = StringVar()
        self.__dst_path = StringVar()
        self.__program_parameters = None    #! Tuple of the form (source, dest, method of backup)

        # Labels
        self.header1 = Label(self.root, text='Please provide a source and destination folder')
        self.header1.place(x=self.__left_margin, y=5)
        
        self.header2 = Label(self.root, text='Please choose backup procedure to backup your files')
        self.header2.place(x=self.__left_margin, y=100)

        self.show_src_path = Label(self.root, textvariable=self.display_source)
        self.show_src_path.place(x=80, y=30)

        self.show_dst_path = Label(self.root, textvariable=self.display_destin)
        self.show_dst_path.place(x=80, y=70)

        # Buttons
        self.chose_src = Button(self.root, text='Browse', command=self.open_src)
        self.chose_src.place(x=self.__left_margin, y=30)

        self.chose_dst = Button(self.root, text='Browse', command=self.open_dst)
        self.chose_dst.place(x=self.__left_margin, y=70)

        self.start_button = Button(self.root, text='Start', command=self.start_procedure)
        self.start_button.place(x=self.__left_margin, y=150)

        self.cancle_button = Button(self.root, text='Cancle', command=self.stop_program)
        self.cancle_button.place(x=self.__left_margin + 80, y=150)

        # Radiobuttons
        self.f_backup = ttk.Radiobutton(self.root, text='File Backup', variable=self.__procedure, value='File Backup')
        self.f_backup.place(x=self.__left_margin, y=120)

        self.ft_backup = ttk.Radiobutton(self.root, text='File Type Backup', variable=self.__procedure, value='File Type Backup')
        self.ft_backup.place(x=self.__left_margin + 150, y=120)

    # Getter 
    def get_source_path(self) -> str:
        """ Return the user given source path."""
        return self.__src_path.get()

    def get_destin_path(self) -> str:
        """ Return the user given destination path."""
        return self.__dst_path.get()

    def get_procedure(self) -> str:
        """ Return the backup procedure chosen by the user."""
        return self.__procedure.get()

    def get_program_params(self) -> tuple:
        """ Return a tuple which contains all the data used by the programm

            Tuple format: (source_path, destination_path, backup_procedure)"""
        if self.__program_parameters is None:
            print('Sorry, could not find this attrebute, maybe its value is None?')
        else:
            return self.__program_parameters


    # Setter 
    def set_source_path(self, new_str: str):
        """ Set the source path."""
        self.__src_path.set(new_str)

    def set_destin_path(self, new_str: str):
        """ Set the destination path."""
        self.__dst_path.set(new_str)

    def set_procedure(self, new_str: str):
        """ Set the backup procedure."""
        self.__procedure.set(new_str)

    def set_program_params(self, new_program_params: tuple):
        """ Set the tuple wich yields all neccessary programm parameters."""
        if type(new_program_params) is tuple:
            self.__program_parameters = new_program_params
        else:
            print('Incorrect Type, the type must be tuple')

    def open_src(self):
        """ Open a filedialog to choose a source directory and set the attribute and labeltext accordingly."""
        self.set_source_path(askdirectory())
        self.display_source.set('Source : ' + self.get_source_path())

    def open_dst(self):
        """ Open a filedialog to choose a destination directory and set the attribute and labeltext accordingly."""
        self.set_destin_path(askdirectory())
        self.display_destin.set('Destination : ' + self.get_destin_path())

    def stop_program(self):
        """ Close the GUI window."""
        self.root.destroy()

    def start_procedure(self):
        """ Set all the neccessary data and close the GUI window."""
        config_tupel = (self.get_source_path(), self.get_destin_path(), self.get_procedure())
        self.set_program_params(config_tupel)
        self.root.destroy()
