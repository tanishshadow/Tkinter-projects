from tkinter import *
from tkinter import messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
#  Command for menus-
    
def newFile():
    global crfile
    crfile = None
    txtarea.delete(1.0,END)

def saveFile():
    global crfile
    if crfile == None:
        crfile = asksaveasfilename(initialfile="Untitled.txt",
        defaultextension=".txt"
        , filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if crfile == "":
            crfile = None
        else:
            # Save as new file 
            with open(crfile, "w") as f:
                f.write(txtarea.get(1.0, END))
                root.title(os.path.basename(crfile + "- Tanish's Notepad"))
    else:
        # Save the file
        with open(crfile, "w") as f:
                f.write(txtarea.get(1.0, END))
                root.title(os.path.basename(crfile + "- Tanish's Notepad"))

        

def openFile():
    global crfile
    crfile = askopenfilename(defaultextension=".txt"
    , filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if crfile == "":
        crfile = None
    else:
        root.title(os.path.basename(crfile) + "-" + "Tanish's Notepad")
        txtarea.delete(1.0, END)
        with open(crfile,"r") as f:
            txtarea.insert(1.0,f.read())

# commands for edit menu-

def copy():
    txtarea.event_generate(("<<Copy>>"))

def paste():
    txtarea.event_generate(("<<Paste>>"))

def cut():
    txtarea.event_generate(("<<Cut>>"))

#commands for help menu-


def About():
    msg.showinfo("Tanish's Notepad -Help","This is a simple notepad made by Tanish Sarmah")
if __name__ == "__main__":
    # Basic tkinter startup

    root = Tk()
    root.geometry("800x700")
    root.title("Tanish's Notepad-Untitled-1")
    root.wm_iconbitmap("noteicon.ico")
    # TODO COMMANDS----
    


    # TODO Menus
    mainmenu = Menu(root, tearoff="0")
    # file menu
    file = Menu(mainmenu, tearoff=0)
    file.add_command(label="New", command=newFile)  # CCreating new file
    file.add_command(label="Save", command=saveFile)  # Saving the current file
    # Opening a Pre-Existing file
    file.add_command(label="Open", command=openFile)
    file.add_separator()
    file.add_command(label="Exit", command=root.destroy) #Exit command
    mainmenu.add_cascade(menu=file, label="File")
    root.config(menu=mainmenu)

    # Edit menu---
    edit = Menu(mainmenu, tearoff=0)
    edit.add_command(label="Cut", command=cut) #To cut any part of the Textarea
    edit.add_command(label="Copy", command=copy) #To copy any part of the Textarea
    edit.add_command(label="Paste", command=paste) #To paste any cut or copied Text.
    mainmenu.add_cascade(menu=edit, label="Edit")
    root.config(menu=mainmenu)

    # Help menu---
    helpm = Menu(mainmenu, tearoff=0)
    helpm.add_command(label="About",command=About) #Displays about the notepad
    mainmenu.add_cascade(menu=helpm, label="Help") 
    root.config(menu=mainmenu)

    # TODO Text widget---
    global scbar
    txtarea = Text(root)
    crfile = None
    txtarea.pack(expand=True, fill=BOTH)
    
    # TODO Scrollbar---
    scbar = Scrollbar(txtarea)
    txtarea.config(yscrollcommand=scbar.set)
    scbar.config(command=txtarea.yview)
    scbar.pack(side=RIGHT,fill=BOTH)
    root.mainloop()
