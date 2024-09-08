from tkinter import * 
from tkinter import filedialog
from tkinter import messagebox



#Window Setup
window=Tk()
window.config(bg="white")
window.title("Text Editor")
window.geometry("600x400")



#Text Area
editor = Text(window,wrap="word")
editor.pack(fill="both",expand=True)


#Function

def Open_File():
    pass

def Save_File():
    file_path = filedialog.asksaveasfilename(filetypes=[("Text File","*.txt")])
    if file_path:
        with open(file_path,"w") as file:
            file.write(editor.get(1.0,END))







#Menu
menu_bar = Menu(window)
window.config(menu=menu_bar)

#Add File Menu
file = Menu(menu_bar)
menu_bar.add_cascade(label="File",menu=file)
file.add_command(label="Open",command=Open_File)
file.add_command(label="Save",command=Save_File)





window.mainloop()