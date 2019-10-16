import tkinter as tk                    # imports
from tkinter import ttk
win = tk.Tk()                           # Create instance
win.title("Python GUI")
s = ttk.Style()
s.theme_create("MyStyle", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
    "TNotebook.Tab": {"configure": {"padding": [50, 10],
                                    "font": ('URW Gothic L', '11', 'bold')}, }})
s.theme_use("MyStyle")
# Add a title
tabControl = ttk.Notebook(win, width=600, height=300)          # Create Tab Control
tab1 = ttk.Frame(tabControl, width=600, height=300)
tab2 = ttk.Frame(tabControl, width=600, height=300)
tab3 = ttk.Frame(tabControl, width=600, height=300)
tab4 = ttk.Frame(tabControl, width=600, height=300)   # Create a tab
tabControl.add(tab1, text='Dashboard')  # Add the tab
tabControl.add(tab2, text='Grafieken')  # Add the tab
tabControl.add(tab3, text='Config')  # Add the tab
tabControl.add(tab4, text='Help')  # Add the tab
tabControl.pack(expand=1, fill="both")  # Pack to make visible

w = tk.Label(tab1, text="Hello")
w.pack()
w = tk.Label(tab2, text="Bye")
w.pack()
win.mainloop()                          # Start GUI