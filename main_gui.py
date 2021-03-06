def run_gui():
    # Global values
    left_margin = 20

    # Create a non resizable frame
    root = Tk()
    root.title('Backup Automation')
    root.geometry('600x200')
    root.resizable(0, 0)
    back = Frame(master=root)
    back.pack(pady=5)

    # Labels
    label1 = Label(root, text='Please provide a source and destination path')
    label1.place(x=left_margin, y=5)

    label2 = Label(root, text='Please choose backup procedure to backup your files')
    label2.place(x=left_margin, y=100)

    # Buttons
    chose_src = Button(root, text='Browse')
    chose_src.place(x=left_margin, y=30)

    chose_dst = Button(root, text='Browse')
    chose_dst.place(x=left_margin, y=70)

    start_procedure = Button(root, text='Start')
    start_procedure.place(x=left_margin, y=150)

    cancle = Button(root, text='Cancle')
    cancle.place(x=left_margin + 80, y=150)

    # Textboxes
    show_src_path = Text(root, height=1, width=50)
    show_src_path.place(x=80, y=30)
    
    show_dst_path = Text(root, height=1, width=50)
    show_dst_path.place(x=80, y=70)

    # Radiobuttons
    procedure = StringVar()
    f_backup = ttk.Radiobutton(root, text='File Backup', variable=procedure, value='File Backup')
    f_backup.place(x=left_margin, y=120)

    ft_backup = ttk.Radiobutton(root, text='File Type Backup', variable=procedure, value='File Type Backup')
    ft_backup.place(x=left_margin + 150, y=120)
    
    root.mainloop() # display the gui