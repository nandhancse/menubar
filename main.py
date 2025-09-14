from tkinter import*

def openfile():
    print('You opened a file')
def closefile():
    print('You closed a file')
def savefile():
     print('You saved a file')
def cutfile():
     print('You cut a file')
def copyfile():
     print('You copied a file')
def pastefile():
     print('You pasted a file')
window =Tk()

menubar=Menu(window)
window.config(menu=menubar)
filemenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='open',command=openfile)
filemenu.add_command(label='save',command=savefile)
filemenu.add_separator()
filemenu.add_command(label= 'exit',command=quit)

editmenu = Menu(menubar, tearoff=False)

menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut',command=cutfile)
editmenu.add_command(label='Copy',command=copyfile)
editmenu.add_command(label='Paste',command=pastefile)


window.mainloop()