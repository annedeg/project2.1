import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


def set_Tk_var():
    global che71
    che71 = tk.IntVar()
    global che93
    che93 = tk.IntVar()
    global che94
    che94 = tk.IntVar()
    global che95
    che95 = tk.IntVar()
    global che96
    che96 = tk.IntVar()
    global che97
    che97 = tk.IntVar()
    global che99
    che99 = tk.IntVar()
    global che72
    che72 = tk.IntVar()
    global che73
    che73 = tk.IntVar()
    global che74
    che74 = tk.IntVar()
    global che75
    che75 = tk.IntVar()
    global che76
    che76 = tk.IntVar()
    global che77
    che77 = tk.IntVar()
    global che120
    che120 = tk.IntVar()
    global che121
    che121 = tk.IntVar()
    global che122
    che122 = tk.IntVar()
    global che123
    che123 = tk.IntVar()
    global che124
    che124 = tk.IntVar()
    global che125
    che125 = tk.IntVar()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import unknown

    unknown.vp_start_gui()


