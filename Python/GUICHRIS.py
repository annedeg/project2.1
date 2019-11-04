import sys
from tkinter import *
import serial
import time

from matplotlib import animation
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import datetime as dt
from random import randint
import numpy as np


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

import serial.tools.list_ports
import unknown_support
aantal = 0
aantal_huidig = 0
getallen = []
comPorts = list(serial.tools.list_ports.comports())
activeComPorts = []
arduinos = []
#poopy = 'Poppy'


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    unknown_support.set_Tk_var()
    top = Toplevel1(root)
    unknown_support.init(root, top)
    root.mainloop()

w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    unknown_support.set_Tk_var()
    top = Toplevel1(w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def get_temperatuur_1():
    return poopy

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("1032x754+478+139")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("CUCKS GUI")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
        [('selected', _compcolor), ('active', _ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.0, rely=0.0, relheight=1.003
                              , relwidth=1.002)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="Dashboard", compound="left", underline="-1"
                            , )
        self.TNotebook1_t0.configure(background="#d9d9d9")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Graph", compound="left", underline="-1", )
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(2, text="Config", compound="none", underline="-1", )
        self.TNotebook1_t2.configure(background="#d9d9d9")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")
        self.TNotebook1_t3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(3, text="Help", compound="none", underline="-1", )
        self.TNotebook1_t3.configure(background="#d9d9d9")
        self.TNotebook1_t3.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t3.configure(highlightcolor="black")

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.01, rely=0.767, height=54, width=277)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=unknown_support.OpenScherm)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''OPEN SCHERM''')

        self.Button23 = tk.Button(self.TNotebook1_t0)
        self.Button23.place(relx=0.01, rely=0.863, height=54, width=277)
        self.Button23.configure(activebackground="#ececec")
        self.Button23.configure(activeforeground="#000000")
        self.Button23.configure(background="#d9d9d9")
        self.Button23.configure(command=unknown_support.CloseScherm)
        self.Button23.configure(disabledforeground="#a3a3a3")
        self.Button23.configure(foreground="#000000")
        self.Button23.configure(highlightbackground="#d9d9d9")
        self.Button23.configure(highlightcolor="black")
        self.Button23.configure(pady="0")
        self.Button23.configure(text='''CLOSE SCHERM''')

        self.Listbox1 = tk.Listbox(self.TNotebook1_t0)
        self.Listbox1.place(relx=0.01, rely=0.014, relheight=0.236
                            , relwidth=0.272)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")

        self.TNotebook2 = ttk.Notebook(self.TNotebook1_t0)
        self.TNotebook2.place(relx=0.291, rely=0.014, relheight=0.241
                              , relwidth=0.68)
        self.TNotebook2.configure(takefocus="")
        self.TNotebook2_t0 = tk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.TNotebook2_t0, padding=3)
        self.TNotebook2.tab(0, text="Afstandsensor", compound="left"
                            , underline="-1", )
        self.TNotebook2_t0.configure(background="#d9d9d9")
        self.TNotebook2_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook2_t0.configure(highlightcolor="black")
        bar1 = Figure(figsize=(5, 2), dpi=75)
        self.ax1 = bar1.add_subplot(111)

        self.data1 = (20, 45, 30, 35)

        self.ind = np.arange(4)  # the x locations for the groups

        self.canvasbar1 = FigureCanvasTkAgg(bar1, master=self.TNotebook2_t0)
        self.canvasbar1.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.TNotebook2_t1 = tk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.TNotebook2_t1, padding=3)
        self.TNotebook2.tab(1, text="Lichtsensor", compound="left", underline="-1"
                            , )
        self.TNotebook2_t1.configure(background="#d9d9d9")
        self.TNotebook2_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook2_t1.configure(highlightcolor="black")
        bar2 = Figure(figsize=(5, 2), dpi=75)
        self.ax2 = bar2.add_subplot(111)

        self.data2 = (20, 35, 30, 35)

        self.canvasbar2 = FigureCanvasTkAgg(bar2, master=self.TNotebook2_t1)
        self.canvasbar2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.TNotebook2_t2 = tk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.TNotebook2_t2, padding=3)
        self.TNotebook2.tab(2, text="Temperatuur", compound="none", underline="-1"
                            , )
        self.TNotebook2_t2.configure(background="#d9d9d9")
        self.TNotebook2_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook2_t2.configure(highlightcolor="black")
        bar3 = Figure(figsize=(5, 2), dpi=75)
        self.ax3 = bar3.add_subplot(111)

        self.data3 = (20, 35, 30, 35)

        self.canvasbar3 = FigureCanvasTkAgg(bar3, master=self.TNotebook2_t2)
        self.canvasbar3.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


        self.Listbox2 = tk.Listbox(self.TNotebook1_t0)
        self.Listbox2.place(relx=0.01, rely=0.26, relheight=0.236
                            , relwidth=0.272)
        self.Listbox2.configure(background="white")
        self.Listbox2.configure(disabledforeground="#a3a3a3")
        self.Listbox2.configure(font="TkFixedFont")
        self.Listbox2.configure(foreground="#000000")
        self.Listbox2.configure(highlightbackground="#d9d9d9")
        self.Listbox2.configure(highlightcolor="black")
        self.Listbox2.configure(selectbackground="#c4c4c4")
        self.Listbox2.configure(selectforeground="black")

        self.Button68 = tk.Button(self.TNotebook1_t0)
        self.Button68.place(relx=0.01, rely=0.521, height=74, width=137)
        self.Button68.configure(activebackground="#ececec")
        self.Button68.configure(activeforeground="#000000")
        self.Button68.configure(background="#d9d9d9")
        self.Button68.configure(command=unknown_support.SwitchToArduino1)
        self.Button68.configure(disabledforeground="#a3a3a3")
        self.Button68.configure(foreground="#000000")
        self.Button68.configure(highlightbackground="#d9d9d9")
        self.Button68.configure(highlightcolor="black")
        self.Button68.configure(pady="0")
        self.Button68.configure(text='''Arduino 1''')

        self.Button69 = tk.Button(self.TNotebook1_t0)
        self.Button69.place(relx=0.155, rely=0.521, height=74, width=127)
        self.Button69.configure(activebackground="#ececec")
        self.Button69.configure(activeforeground="#000000")
        self.Button69.configure(background="#d9d9d9")
        self.Button69.configure(command=unknown_support.SwitchToArduino2)
        self.Button69.configure(disabledforeground="#a3a3a3")
        self.Button69.configure(foreground="#000000")
        self.Button69.configure(highlightbackground="#d9d9d9")
        self.Button69.configure(highlightcolor="black")
        self.Button69.configure(pady="0")
        self.Button69.configure(text='''Arduino 2''')

        self.Button70 = tk.Button(self.TNotebook1_t0)
        self.Button70.place(relx=0.01, rely=0.644, height=74, width=137)
        self.Button70.configure(activebackground="#ececec")
        self.Button70.configure(activeforeground="#000000")
        self.Button70.configure(background="#d9d9d9")
        self.Button70.configure(command=unknown_support.SwitchToArduino3)
        self.Button70.configure(disabledforeground="#a3a3a3")
        self.Button70.configure(foreground="#000000")
        self.Button70.configure(highlightbackground="#d9d9d9")
        self.Button70.configure(highlightcolor="black")
        self.Button70.configure(pady="0")
        self.Button70.configure(text='''Arduino 3''')

        self.Button71 = tk.Button(self.TNotebook1_t0)
        self.Button71.place(relx=0.155, rely=0.644, height=74, width=127)
        self.Button71.configure(activebackground="#ececec")
        self.Button71.configure(activeforeground="#000000")
        self.Button71.configure(background="#d9d9d9")
        self.Button71.configure(command=unknown_support.SwitchToArduino4)
        self.Button71.configure(disabledforeground="#a3a3a3")
        self.Button71.configure(foreground="#000000")
        self.Button71.configure(highlightbackground="#d9d9d9")
        self.Button71.configure(highlightcolor="black")
        self.Button71.configure(pady="0")
        self.Button71.configure(text='''Arduino 4''')

        self.TNotebook5 = ttk.Notebook(self.TNotebook1_t0)
        self.TNotebook5.place(relx=0.291, rely=0.26, relheight=0.721
                              , relwidth=0.693)
        self.TNotebook5.configure(takefocus="")
        self.TNotebook5_t0 = tk.Frame(self.TNotebook5)
        self.TNotebook5.add(self.TNotebook5_t0, padding=3)
        self.TNotebook5.tab(0, text="Afstand", compound="left", underline="-1", )
        self.TNotebook5_t0.configure(background="#d9d9d9")
        self.TNotebook5_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook5_t0.configure(highlightcolor="black")
        self.TNotebook5_t1 = tk.Frame(self.TNotebook5)
        self.TNotebook5.add(self.TNotebook5_t1, padding=3)
        self.TNotebook5.tab(1, text="Licht", compound="left", underline="-1", )
        self.TNotebook5_t1.configure(background="#d9d9d9")
        self.TNotebook5_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook5_t1.configure(highlightcolor="black")
        self.TNotebook5_t2 = tk.Frame(self.TNotebook5)
        self.TNotebook5.add(self.TNotebook5_t2, padding=3)
        self.TNotebook5.tab(2, text="Temperatuur", compound="none", underline="-1"
                            , )
        self.TNotebook5_t2.configure(background="#d9d9d9")
        self.TNotebook5_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook5_t2.configure(highlightcolor="black")

        self.fig1 = Figure(figsize=(5, 4), dpi=100)
        self.t = np.arange(0, 3, .01)
        self.canvas1 = self.fig1.add_subplot(1, 1, 1)
        self.canvasx = []
        self.canvas1y = []
        self.newx = 0

        self.canvas1a = FigureCanvasTkAgg(self.fig1, master=self.TNotebook5_t0)  # A tk.DrawingArea.


        self.toolbar = NavigationToolbar2Tk(self.canvas1a, self.TNotebook5_t0)
        self.toolbar.update()
        self.canvas1a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        fig2 = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        self.canvas2 = fig2.add_subplot(1,1,1)
        self.canvas2y = []
        self.canvas2x = []
        self.new2x = 0

        self.canvas2a = FigureCanvasTkAgg(fig2, master=self.TNotebook5_t1)  # A tk.DrawingArea.

        toolbar = NavigationToolbar2Tk(self.canvas2a, self.TNotebook5_t1)
        toolbar.update()
        self.canvas2a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        fig3 = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        self.canvas3 = fig3.add_subplot(1, 1, 1)
        self.canvas3y = []
        self.canvas3x = []
        self.new3x = 0

        self.canvas3a = FigureCanvasTkAgg(fig3, master=self.TNotebook5_t2)  # A tk.DrawingArea.

        toolbar = NavigationToolbar2Tk(self.canvas3a, self.TNotebook5_t2)
        toolbar.update()
        self.canvas3a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.TNotebook3 = ttk.Notebook(self.TNotebook1_t1)
        self.TNotebook3.place(relx=0.0, rely=0.014, relheight=0.995
                              , relwidth=1.004)
        self.TNotebook3.configure(takefocus="")
        self.TNotebook3_t0 = tk.Frame(self.TNotebook3)
        self.TNotebook3.add(self.TNotebook3_t0, padding=3)
        self.TNotebook3.tab(0, text="Arduino 1", compound="left", underline="-1"
                            , )
        self.TNotebook3_t0.configure(background="#d9d9d9")
        self.TNotebook3_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook3_t0.configure(highlightcolor="black")
        self.TNotebook3_t1 = tk.Frame(self.TNotebook3)
        self.TNotebook3.add(self.TNotebook3_t1, padding=3)
        self.TNotebook3.tab(1, text="Arduino 2", compound="left", underline="-1"
                            , )
        self.TNotebook3_t1.configure(background="#d9d9d9")
        self.TNotebook3_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook3_t1.configure(highlightcolor="black")
        self.TNotebook3_t2 = tk.Frame(self.TNotebook3)
        self.TNotebook3.add(self.TNotebook3_t2, padding=3)
        self.TNotebook3.tab(2, text="Arduino 3", compound="none", underline="-1"
                            , )
        self.TNotebook3_t2.configure(background="#d9d9d9")
        self.TNotebook3_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook3_t2.configure(highlightcolor="black")
        self.TNotebook3_t3 = tk.Frame(self.TNotebook3)
        self.TNotebook3.add(self.TNotebook3_t3, padding=3)
        self.TNotebook3.tab(3, text="Arduino 4", compound="none", underline="-1"
                            , )
        self.TNotebook3_t3.configure(background="#d9d9d9")
        self.TNotebook3_t3.configure(highlightbackground="#d9d9d9")
        self.TNotebook3_t3.configure(highlightcolor="black")

        fig4 = Figure(figsize=(5, 8), dpi=100)
        t = np.arange(0, 3, .01)
        self.canvas4 = fig4.add_subplot(1, 2, 1)
        self.canvas5 = fig4.add_subplot(1, 2, 2)
        self.canvas4y = []
        self.canvas5y = []
        self.canvas4x = []
        self.canvas5x = []
        self.new4x = 0
        self.new5x = 0

        self.canvas4a = FigureCanvasTkAgg(fig4, master=self.TNotebook3_t0)  # A tk.DrawingArea.

        toolbar = NavigationToolbar2Tk(self.canvas4a, self.TNotebook3_t0)
        toolbar.update()
        self.canvas4a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        fig5 = Figure(figsize=(5, 8), dpi=100)
        t = np.arange(0, 3, .01)
        self.canvas6 = fig5.add_subplot(1, 2, 1)
        self.canvas7 = fig5.add_subplot(1, 2, 2)
        self.canvas6y = []
        self.canvas7y = []
        self.canvas6x = []
        self.canvas7x = []
        self.new6x = 0
        self.new7x = 0

        self.canvas5a = FigureCanvasTkAgg(fig5, master=self.TNotebook3_t1)  # A tk.DrawingArea.

        toolbar = NavigationToolbar2Tk(self.canvas5a, self.TNotebook3_t1)
        toolbar.update()
        self.canvas5a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        fig6 = Figure(figsize=(5, 8), dpi=100)
        t = np.arange(0, 3, .01)
        self.canvas8 = fig6.add_subplot(1, 2, 1)
        self.canvas9 = fig6.add_subplot(1, 2, 2)
        self.canvas8y = []
        self.canvas9y = []
        self.canvas8x = []
        self.canvas9x = []
        self.new8x = 0
        self.new9x = 0

        self.canvas6a = FigureCanvasTkAgg(fig6, master=self.TNotebook3_t2)  # A tk.DrawingArea.

        toolbar = NavigationToolbar2Tk(self.canvas6a, self.TNotebook3_t2)
        toolbar.update()
        self.canvas6a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        fig7 = Figure(figsize=(5, 8), dpi=100)
        t = np.arange(0, 3, .01)
        self.canvas10 = fig7.add_subplot(1, 2, 1)
        self.canvas11 = fig7.add_subplot(1, 2, 2)
        self.canvas10y = []
        self.canvas11y = []
        self.canvas10x = []
        self.canvas11x = []
        self.new10x = 0
        self.new11x = 0

        self.canvas7a = FigureCanvasTkAgg(fig7, master=self.TNotebook3_t3)  # A tk.DrawingArea.

        toolbar = NavigationToolbar2Tk(self.canvas7a, self.TNotebook3_t3)
        toolbar.update()
        self.canvas7a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.TNotebook4 = ttk.Notebook(self.TNotebook1_t2)
        self.TNotebook4.place(relx=0.0, rely=0.014, relheight=0.981
                              , relwidth=0.994)
        self.TNotebook4.configure(takefocus="")
        self.TNotebook4_t0 = tk.Frame(self.TNotebook4)
        self.TNotebook4.add(self.TNotebook4_t0, padding=3)
        self.TNotebook4.tab(0, text="Temperatuur", compound="left", underline="-1"
                            , )
        self.TNotebook4_t0.configure(background="#d9d9d9")
        self.TNotebook4_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook4_t0.configure(highlightcolor="black")
        self.TNotebook4_t1 = tk.Frame(self.TNotebook4)
        self.TNotebook4.add(self.TNotebook4_t1, padding=3)
        self.TNotebook4.tab(1, text="Licht", compound="left", underline="-1", )
        self.TNotebook4_t1.configure(background="#d9d9d9")
        self.TNotebook4_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook4_t1.configure(highlightcolor="black")
        self.TNotebook4_t2 = tk.Frame(self.TNotebook4)
        self.TNotebook4.add(self.TNotebook4_t2, padding=3)
        self.TNotebook4.tab(2, text="Afstand", compound="none", underline="-1", )
        self.TNotebook4_t2.configure(background="#d9d9d9")
        self.TNotebook4_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook4_t2.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(self.TNotebook4_t0)
        self.Entry1.place(relx=0.088, rely=0.029, height=20, relwidth=0.161)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry2 = tk.Entry(self.TNotebook4_t0)
        self.Entry2.place(relx=0.088, rely=0.072, height=20, relwidth=0.161)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Entry3 = tk.Entry(self.TNotebook4_t0)
        self.Entry3.place(relx=0.088, rely=0.116, height=20, relwidth=0.161)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")

        self.Entry4 = tk.Entry(self.TNotebook4_t0)
        self.Entry4.place(relx=0.088, rely=0.159, height=20, relwidth=0.161)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")

        self.Entry5 = tk.Entry(self.TNotebook4_t0)
        self.Entry5.place(relx=0.088, rely=0.203, height=20, relwidth=0.161)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(selectbackground="#c4c4c4")
        self.Entry5.configure(selectforeground="black")

        self.Entry6 = tk.Entry(self.TNotebook4_t0)
        self.Entry6.place(relx=0.088, rely=0.246, height=20, relwidth=0.161)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(selectbackground="#c4c4c4")
        self.Entry6.configure(selectforeground="black")

        self.Entry7 = tk.Entry(self.TNotebook4_t0)
        self.Entry7.place(relx=0.088, rely=0.29, height=20, relwidth=0.161)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(highlightbackground="#d9d9d9")
        self.Entry7.configure(highlightcolor="black")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(selectbackground="#c4c4c4")
        self.Entry7.configure(selectforeground="black")

        self.Entry8 = tk.Entry(self.TNotebook4_t0)
        self.Entry8.place(relx=0.088, rely=0.333, height=20, relwidth=0.161)
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(highlightbackground="#d9d9d9")
        self.Entry8.configure(highlightcolor="black")
        self.Entry8.configure(insertbackground="black")
        self.Entry8.configure(selectbackground="#c4c4c4")
        self.Entry8.configure(selectforeground="black")

        self.Label2 = tk.Label(self.TNotebook4_t0)
        self.Label2.place(relx=0.0, rely=0.029, height=21, width=74)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Setting''')

        self.Label2 = tk.Label(self.TNotebook4_t0)
        self.Label2.place(relx=0.0, rely=0.072, height=21, width=74)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Setting''')

        self.Label2 = tk.Label(self.TNotebook4_t0)
        self.Label2.place(relx=0.0, rely=0.116, height=21, width=74)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Setting''')

        self.Label2 = tk.Label(self.TNotebook4_t0)
        self.Label2.place(relx=0.0, rely=0.159, height=21, width=74)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Setting''')

        self.Label2 = tk.Label(self.TNotebook4_t0)
        self.Label2.place(relx=0.0, rely=0.203, height=21, width=74)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Setting''')

        self.Label2 = tk.Label(self.TNotebook4_t0)
        self.Label2.place(relx=0.0, rely=0.246, height=21, width=74)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Setting''')

        self.Label2 = tk.Label(self.TNotebook4_t0)
        self.Label2.place(relx=0.0, rely=0.29, height=21, width=74)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Setting''')

        self.Label2 = tk.Label(self.TNotebook4_t0)
        self.Label2.place(relx=0.0, rely=0.333, height=21, width=74)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Setting''')

        self.Button2 = tk.Button(self.TNotebook4_t0)
        self.Button2.place(relx=0.265, rely=0.029, height=24, width=47)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=self.Set1Temperatuur)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Set''')

        self.Button3 = tk.Button(self.TNotebook4_t0)
        self.Button3.place(relx=0.324, rely=0.029, height=24, width=37)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(command=unknown_support.Reset1Temperatuur)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Reset''')

        self.Button4 = tk.Button(self.TNotebook4_t0)
        self.Button4.place(relx=0.324, rely=0.072, height=24, width=37)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(command=unknown_support.Reset2Temperatuur)
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Reset''')

        self.Button5 = tk.Button(self.TNotebook4_t0)
        self.Button5.place(relx=0.324, rely=0.116, height=24, width=37)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(command=unknown_support.Reset3Temperatuur)
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Reset''')

        self.Button6 = tk.Button(self.TNotebook4_t0)
        self.Button6.place(relx=0.324, rely=0.159, height=24, width=37)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(command=unknown_support.Reset4Temperatuur)
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Reset''')

        self.Button7 = tk.Button(self.TNotebook4_t0)
        self.Button7.place(relx=0.324, rely=0.203, height=24, width=37)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(command=unknown_support.Reset5Temperatuur)
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''Reset''')

        self.Button8 = tk.Button(self.TNotebook4_t0)
        self.Button8.place(relx=0.324, rely=0.246, height=24, width=37)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(command=unknown_support.Reset6Temperatuur)
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''Reset''')

        self.Button9 = tk.Button(self.TNotebook4_t0)
        self.Button9.place(relx=0.324, rely=0.29, height=24, width=37)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(command=unknown_support.Reset7Temperatuur)
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''Reset''')

        self.Button10 = tk.Button(self.TNotebook4_t0)
        self.Button10.place(relx=0.324, rely=0.333, height=24, width=37)
        self.Button10.configure(activebackground="#ececec")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="#d9d9d9")
        self.Button10.configure(command=unknown_support.Reset8Temperatuur)
        self.Button10.configure(disabledforeground="#a3a3a3")
        self.Button10.configure(foreground="#000000")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self.Button10.configure(pady="0")
        self.Button10.configure(text='''Reset''')

        self.Button11 = tk.Button(self.TNotebook4_t0)
        self.Button11.place(relx=0.265, rely=0.072, height=24, width=47)
        self.Button11.configure(activebackground="#ececec")
        self.Button11.configure(activeforeground="#000000")
        self.Button11.configure(background="#d9d9d9")
        self.Button11.configure(command=self.Set2Temperatuur)
        self.Button11.configure(disabledforeground="#a3a3a3")
        self.Button11.configure(foreground="#000000")
        self.Button11.configure(highlightbackground="#d9d9d9")
        self.Button11.configure(highlightcolor="black")
        self.Button11.configure(pady="0")
        self.Button11.configure(text='''Set''')

        self.Button12 = tk.Button(self.TNotebook4_t0)
        self.Button12.place(relx=0.265, rely=0.116, height=24, width=47)
        self.Button12.configure(activebackground="#ececec")
        self.Button12.configure(activeforeground="#000000")
        self.Button12.configure(background="#d9d9d9")
        self.Button12.configure(command=self.Set3Temperatuur)
        self.Button12.configure(disabledforeground="#a3a3a3")
        self.Button12.configure(foreground="#000000")
        self.Button12.configure(highlightbackground="#d9d9d9")
        self.Button12.configure(highlightcolor="black")
        self.Button12.configure(pady="0")
        self.Button12.configure(text='''Set''')

        self.Button13 = tk.Button(self.TNotebook4_t0)
        self.Button13.place(relx=0.265, rely=0.159, height=24, width=47)
        self.Button13.configure(activebackground="#ececec")
        self.Button13.configure(activeforeground="#000000")
        self.Button13.configure(background="#d9d9d9")
        self.Button13.configure(command=self.Set4Temperatuur)
        self.Button13.configure(disabledforeground="#a3a3a3")
        self.Button13.configure(foreground="#000000")
        self.Button13.configure(highlightbackground="#d9d9d9")
        self.Button13.configure(highlightcolor="black")
        self.Button13.configure(pady="0")
        self.Button13.configure(text='''Set''')

        self.Button14 = tk.Button(self.TNotebook4_t0)
        self.Button14.place(relx=0.265, rely=0.203, height=24, width=47)
        self.Button14.configure(activebackground="#ececec")
        self.Button14.configure(activeforeground="#000000")
        self.Button14.configure(background="#d9d9d9")
        self.Button14.configure(command=self.Set5Temperatuur)
        self.Button14.configure(disabledforeground="#a3a3a3")
        self.Button14.configure(foreground="#000000")
        self.Button14.configure(highlightbackground="#d9d9d9")
        self.Button14.configure(highlightcolor="black")
        self.Button14.configure(pady="0")
        self.Button14.configure(text='''Set''')

        self.Button15 = tk.Button(self.TNotebook4_t0)
        self.Button15.place(relx=0.265, rely=0.246, height=24, width=47)
        self.Button15.configure(activebackground="#ececec")
        self.Button15.configure(activeforeground="#000000")
        self.Button15.configure(background="#d9d9d9")
        self.Button15.configure(command=self.Set6Temperatuur)
        self.Button15.configure(disabledforeground="#a3a3a3")
        self.Button15.configure(foreground="#000000")
        self.Button15.configure(highlightbackground="#d9d9d9")
        self.Button15.configure(highlightcolor="black")
        self.Button15.configure(pady="0")
        self.Button15.configure(text='''Set''')

        self.Button16 = tk.Button(self.TNotebook4_t0)
        self.Button16.place(relx=0.265, rely=0.29, height=24, width=47)
        self.Button16.configure(activebackground="#ececec")
        self.Button16.configure(activeforeground="#000000")
        self.Button16.configure(background="#d9d9d9")
        self.Button16.configure(command=self.Set7Temperatuur)
        self.Button16.configure(disabledforeground="#a3a3a3")
        self.Button16.configure(foreground="#000000")
        self.Button16.configure(highlightbackground="#d9d9d9")
        self.Button16.configure(highlightcolor="black")
        self.Button16.configure(pady="0")
        self.Button16.configure(text='''Set''')

        self.Button17 = tk.Button(self.TNotebook4_t0)
        self.Button17.place(relx=0.265, rely=0.333, height=24, width=47)
        self.Button17.configure(activebackground="#ececec")
        self.Button17.configure(activeforeground="#000000")
        self.Button17.configure(background="#d9d9d9")
        self.Button17.configure(command=self.Set8Temperatuur)
        self.Button17.configure(disabledforeground="#a3a3a3")
        self.Button17.configure(foreground="#000000")
        self.Button17.configure(highlightbackground="#d9d9d9")
        self.Button17.configure(highlightcolor="black")
        self.Button17.configure(pady="0")
        self.Button17.configure(text='''Set''')

        self.Checkbutton1 = tk.Checkbutton(self.TNotebook4_t0)
        self.Checkbutton1.place(relx=0.088, rely=0.391, relheight=0.036
                                , relwidth=0.06)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Check''')
        self.Checkbutton1.configure(variable=unknown_support.che93)

        self.Checkbutton2 = tk.Checkbutton(self.TNotebook4_t0)
        self.Checkbutton2.place(relx=0.088, rely=0.435, relheight=0.036
                                , relwidth=0.06)
        self.Checkbutton2.configure(activebackground="#ececec")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#d9d9d9")
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify='left')
        self.Checkbutton2.configure(text='''Check''')
        self.Checkbutton2.configure(variable=unknown_support.che94)

        self.Checkbutton3 = tk.Checkbutton(self.TNotebook4_t0)
        self.Checkbutton3.place(relx=0.088, rely=0.478, relheight=0.036
                                , relwidth=0.06)
        self.Checkbutton3.configure(activebackground="#ececec")
        self.Checkbutton3.configure(activeforeground="#000000")
        self.Checkbutton3.configure(background="#d9d9d9")
        self.Checkbutton3.configure(disabledforeground="#a3a3a3")
        self.Checkbutton3.configure(foreground="#000000")
        self.Checkbutton3.configure(highlightbackground="#d9d9d9")
        self.Checkbutton3.configure(highlightcolor="black")
        self.Checkbutton3.configure(justify='left')
        self.Checkbutton3.configure(text='''Check''')
        self.Checkbutton3.configure(variable=unknown_support.che95)

        self.Checkbutton4 = tk.Checkbutton(self.TNotebook4_t0)
        self.Checkbutton4.place(relx=0.157, rely=0.391, relheight=0.036
                                , relwidth=0.06)
        self.Checkbutton4.configure(activebackground="#ececec")
        self.Checkbutton4.configure(activeforeground="#000000")
        self.Checkbutton4.configure(background="#d9d9d9")
        self.Checkbutton4.configure(disabledforeground="#a3a3a3")
        self.Checkbutton4.configure(foreground="#000000")
        self.Checkbutton4.configure(highlightbackground="#d9d9d9")
        self.Checkbutton4.configure(highlightcolor="black")
        self.Checkbutton4.configure(justify='left')
        self.Checkbutton4.configure(text='''Check''')
        self.Checkbutton4.configure(variable=unknown_support.che96)

        self.Checkbutton5 = tk.Checkbutton(self.TNotebook4_t0)
        self.Checkbutton5.place(relx=0.157, rely=0.435, relheight=0.036
                                , relwidth=0.06)
        self.Checkbutton5.configure(activebackground="#ececec")
        self.Checkbutton5.configure(activeforeground="#000000")
        self.Checkbutton5.configure(background="#d9d9d9")
        self.Checkbutton5.configure(disabledforeground="#a3a3a3")
        self.Checkbutton5.configure(foreground="#000000")
        self.Checkbutton5.configure(highlightbackground="#d9d9d9")
        self.Checkbutton5.configure(highlightcolor="black")
        self.Checkbutton5.configure(justify='left')
        self.Checkbutton5.configure(text='''Check''')
        self.Checkbutton5.configure(variable=unknown_support.che97)

        self.Checkbutton6 = tk.Checkbutton(self.TNotebook4_t0)
        self.Checkbutton6.place(relx=0.157, rely=0.478, relheight=0.036
                                , relwidth=0.06)
        self.Checkbutton6.configure(activebackground="#ececec")
        self.Checkbutton6.configure(activeforeground="#000000")
        self.Checkbutton6.configure(background="#d9d9d9")
        self.Checkbutton6.configure(disabledforeground="#a3a3a3")
        self.Checkbutton6.configure(foreground="#000000")
        self.Checkbutton6.configure(highlightbackground="#d9d9d9")
        self.Checkbutton6.configure(highlightcolor="black")
        self.Checkbutton6.configure(justify='left')
        self.Checkbutton6.configure(text='''Check''')
        self.Checkbutton6.configure(variable=unknown_support.che99)

        self.Button18 = tk.Button(self.TNotebook4_t0)
        self.Button18.place(relx=0.265, rely=0.391, height=24, width=47)
        self.Button18.configure(activebackground="#ececec")
        self.Button18.configure(activeforeground="#000000")
        self.Button18.configure(background="#d9d9d9")
        self.Button18.configure(command=unknown_support.Set9Temperatuur)
        self.Button18.configure(disabledforeground="#a3a3a3")
        self.Button18.configure(foreground="#000000")
        self.Button18.configure(highlightbackground="#d9d9d9")
        self.Button18.configure(highlightcolor="black")
        self.Button18.configure(pady="0")
        self.Button18.configure(text='''Set''')

        self.Button2 = tk.Button(self.TNotebook4_t0)
        self.Button2.place(relx=0.265, rely=0.435, height=24, width=47)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=unknown_support.Set10Temperatuur)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Set''')

        self.Button19 = tk.Button(self.TNotebook4_t0)
        self.Button19.place(relx=0.265, rely=0.478, height=24, width=47)
        self.Button19.configure(activebackground="#ececec")
        self.Button19.configure(activeforeground="#000000")
        self.Button19.configure(background="#d9d9d9")
        self.Button19.configure(command=unknown_support.Set11Temperatuur)
        self.Button19.configure(disabledforeground="#a3a3a3")
        self.Button19.configure(foreground="#000000")
        self.Button19.configure(highlightbackground="#d9d9d9")
        self.Button19.configure(highlightcolor="black")
        self.Button19.configure(pady="0")
        self.Button19.configure(text='''Set''')

        self.Button20 = tk.Button(self.TNotebook4_t0)
        self.Button20.place(relx=0.324, rely=0.391, height=24, width=39)
        self.Button20.configure(activebackground="#ececec")
        self.Button20.configure(activeforeground="#000000")
        self.Button20.configure(background="#d9d9d9")
        self.Button20.configure(command=unknown_support.Reset9Temperatuur)
        self.Button20.configure(disabledforeground="#a3a3a3")
        self.Button20.configure(foreground="#000000")
        self.Button20.configure(highlightbackground="#d9d9d9")
        self.Button20.configure(highlightcolor="black")
        self.Button20.configure(pady="0")
        self.Button20.configure(text='''Reset''')

        self.Button21 = tk.Button(self.TNotebook4_t0)
        self.Button21.place(relx=0.324, rely=0.435, height=24, width=39)
        self.Button21.configure(activebackground="#ececec")
        self.Button21.configure(activeforeground="#000000")
        self.Button21.configure(background="#d9d9d9")
        self.Button21.configure(command=unknown_support.Reset10Temperatuur)
        self.Button21.configure(disabledforeground="#a3a3a3")
        self.Button21.configure(foreground="#000000")
        self.Button21.configure(highlightbackground="#d9d9d9")
        self.Button21.configure(highlightcolor="black")
        self.Button21.configure(pady="0")
        self.Button21.configure(text='''Reset''')

        self.Button22 = tk.Button(self.TNotebook4_t0)
        self.Button22.place(relx=0.324, rely=0.478, height=24, width=39)
        self.Button22.configure(activebackground="#ececec")
        self.Button22.configure(activeforeground="#000000")
        self.Button22.configure(background="#d9d9d9")
        self.Button22.configure(command=unknown_support.Reset11Temperatuur)
        self.Button22.configure(disabledforeground="#a3a3a3")
        self.Button22.configure(foreground="#000000")
        self.Button22.configure(highlightbackground="#d9d9d9")
        self.Button22.configure(highlightcolor="black")
        self.Button22.configure(pady="0")
        self.Button22.configure(text='''Reset''')

        self.Entry9 = tk.Entry(self.TNotebook4_t1)
        self.Entry9.place(relx=0.088, rely=0.029, height=20, relwidth=0.161)
        self.Entry9.configure(background="white")
        self.Entry9.configure(disabledforeground="#a3a3a3")
        self.Entry9.configure(font="TkFixedFont")
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(highlightbackground="#d9d9d9")
        self.Entry9.configure(highlightcolor="black")
        self.Entry9.configure(insertbackground="black")
        self.Entry9.configure(selectbackground="#c4c4c4")
        self.Entry9.configure(selectforeground="black")

        self.Entry10 = tk.Entry(self.TNotebook4_t1)
        self.Entry10.place(relx=0.088, rely=0.072, height=20, relwidth=0.161)
        self.Entry10.configure(background="white")
        self.Entry10.configure(disabledforeground="#a3a3a3")
        self.Entry10.configure(font="TkFixedFont")
        self.Entry10.configure(foreground="#000000")
        self.Entry10.configure(highlightbackground="#d9d9d9")
        self.Entry10.configure(highlightcolor="black")
        self.Entry10.configure(insertbackground="black")
        self.Entry10.configure(selectbackground="#c4c4c4")
        self.Entry10.configure(selectforeground="black")

        self.Entry11 = tk.Entry(self.TNotebook4_t1)
        self.Entry11.place(relx=0.088, rely=0.116, height=20, relwidth=0.161)
        self.Entry11.configure(background="white")
        self.Entry11.configure(disabledforeground="#a3a3a3")
        self.Entry11.configure(font="TkFixedFont")
        self.Entry11.configure(foreground="#000000")
        self.Entry11.configure(highlightbackground="#d9d9d9")
        self.Entry11.configure(highlightcolor="black")
        self.Entry11.configure(insertbackground="black")
        self.Entry11.configure(selectbackground="#c4c4c4")
        self.Entry11.configure(selectforeground="black")

        self.Entry12 = tk.Entry(self.TNotebook4_t1)
        self.Entry12.place(relx=0.088, rely=0.159, height=20, relwidth=0.161)
        self.Entry12.configure(background="white")
        self.Entry12.configure(disabledforeground="#a3a3a3")
        self.Entry12.configure(font="TkFixedFont")
        self.Entry12.configure(foreground="#000000")
        self.Entry12.configure(highlightbackground="#d9d9d9")
        self.Entry12.configure(highlightcolor="black")
        self.Entry12.configure(insertbackground="black")
        self.Entry12.configure(selectbackground="#c4c4c4")
        self.Entry12.configure(selectforeground="black")

        self.Entry13 = tk.Entry(self.TNotebook4_t1)
        self.Entry13.place(relx=0.088, rely=0.203, height=20, relwidth=0.161)
        self.Entry13.configure(background="white")
        self.Entry13.configure(disabledforeground="#a3a3a3")
        self.Entry13.configure(font="TkFixedFont")
        self.Entry13.configure(foreground="#000000")
        self.Entry13.configure(highlightbackground="#d9d9d9")
        self.Entry13.configure(highlightcolor="black")
        self.Entry13.configure(insertbackground="black")
        self.Entry13.configure(selectbackground="#c4c4c4")
        self.Entry13.configure(selectforeground="black")

        self.Entry14 = tk.Entry(self.TNotebook4_t1)
        self.Entry14.place(relx=0.088, rely=0.246, height=20, relwidth=0.161)
        self.Entry14.configure(background="white")
        self.Entry14.configure(disabledforeground="#a3a3a3")
        self.Entry14.configure(font="TkFixedFont")
        self.Entry14.configure(foreground="#000000")
        self.Entry14.configure(highlightbackground="#d9d9d9")
        self.Entry14.configure(highlightcolor="black")
        self.Entry14.configure(insertbackground="black")
        self.Entry14.configure(selectbackground="#c4c4c4")
        self.Entry14.configure(selectforeground="black")

        self.Entry15 = tk.Entry(self.TNotebook4_t1)
        self.Entry15.place(relx=0.088, rely=0.29, height=20, relwidth=0.161)
        self.Entry15.configure(background="white")
        self.Entry15.configure(disabledforeground="#a3a3a3")
        self.Entry15.configure(font="TkFixedFont")
        self.Entry15.configure(foreground="#000000")
        self.Entry15.configure(highlightbackground="#d9d9d9")
        self.Entry15.configure(highlightcolor="black")
        self.Entry15.configure(insertbackground="black")
        self.Entry15.configure(selectbackground="#c4c4c4")
        self.Entry15.configure(selectforeground="black")

        self.Label3 = tk.Label(self.TNotebook4_t1)
        self.Label3.place(relx=0.02, rely=0.029, height=21, width=43)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Setting''')

        self.Label4 = tk.Label(self.TNotebook4_t1)
        self.Label4.place(relx=0.02, rely=0.072, height=21, width=43)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Setting''')

        self.Label5 = tk.Label(self.TNotebook4_t1)
        self.Label5.place(relx=0.02, rely=0.116, height=21, width=43)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Setting''')

        self.Label6 = tk.Label(self.TNotebook4_t1)
        self.Label6.place(relx=0.02, rely=0.159, height=21, width=43)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Setting''')

        self.Label7 = tk.Label(self.TNotebook4_t1)
        self.Label7.place(relx=0.02, rely=0.203, height=21, width=43)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Setting''')

        self.Label8 = tk.Label(self.TNotebook4_t1)
        self.Label8.place(relx=0.02, rely=0.246, height=21, width=43)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Setting''')

        self.Label9 = tk.Label(self.TNotebook4_t1)
        self.Label9.place(relx=0.02, rely=0.29, height=21, width=43)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''Setting''')

        self.Button24 = tk.Button(self.TNotebook4_t1)
        self.Button24.place(relx=0.265, rely=0.029, height=24, width=47)
        self.Button24.configure(activebackground="#ececec")
        self.Button24.configure(activeforeground="#000000")
        self.Button24.configure(background="#d9d9d9")
        self.Button24.configure(command=self.Set1Licht)
        self.Button24.configure(disabledforeground="#a3a3a3")
        self.Button24.configure(foreground="#000000")
        self.Button24.configure(highlightbackground="#d9d9d9")
        self.Button24.configure(highlightcolor="black")
        self.Button24.configure(pady="0")
        self.Button24.configure(text='''Set''')

        self.Button25 = tk.Button(self.TNotebook4_t1)
        self.Button25.place(relx=0.265, rely=0.072, height=24, width=47)
        self.Button25.configure(activebackground="#ececec")
        self.Button25.configure(activeforeground="#000000")
        self.Button25.configure(background="#d9d9d9")
        self.Button25.configure(command=self.Set2Licht)
        self.Button25.configure(disabledforeground="#a3a3a3")
        self.Button25.configure(foreground="#000000")
        self.Button25.configure(highlightbackground="#d9d9d9")
        self.Button25.configure(highlightcolor="black")
        self.Button25.configure(pady="0")
        self.Button25.configure(text='''Set''')

        self.Button26 = tk.Button(self.TNotebook4_t1)
        self.Button26.place(relx=0.265, rely=0.116, height=24, width=47)
        self.Button26.configure(activebackground="#ececec")
        self.Button26.configure(activeforeground="#000000")
        self.Button26.configure(background="#d9d9d9")
        self.Button26.configure(command=self.Set3Licht)
        self.Button26.configure(disabledforeground="#a3a3a3")
        self.Button26.configure(foreground="#000000")
        self.Button26.configure(highlightbackground="#d9d9d9")
        self.Button26.configure(highlightcolor="black")
        self.Button26.configure(pady="0")
        self.Button26.configure(text='''Set''')

        self.Button27 = tk.Button(self.TNotebook4_t1)
        self.Button27.place(relx=0.265, rely=0.159, height=24, width=47)
        self.Button27.configure(activebackground="#ececec")
        self.Button27.configure(activeforeground="#000000")
        self.Button27.configure(background="#d9d9d9")
        self.Button27.configure(command=self.Set4Licht)
        self.Button27.configure(disabledforeground="#a3a3a3")
        self.Button27.configure(foreground="#000000")
        self.Button27.configure(highlightbackground="#d9d9d9")
        self.Button27.configure(highlightcolor="black")
        self.Button27.configure(pady="0")
        self.Button27.configure(text='''Set''')

        self.Button28 = tk.Button(self.TNotebook4_t1)
        self.Button28.place(relx=0.265, rely=0.203, height=24, width=47)
        self.Button28.configure(activebackground="#ececec")
        self.Button28.configure(activeforeground="#000000")
        self.Button28.configure(background="#d9d9d9")
        self.Button28.configure(command=self.Set5Licht)
        self.Button28.configure(disabledforeground="#a3a3a3")
        self.Button28.configure(foreground="#000000")
        self.Button28.configure(highlightbackground="#d9d9d9")
        self.Button28.configure(highlightcolor="black")
        self.Button28.configure(pady="0")
        self.Button28.configure(text='''Set''')

        self.Button29 = tk.Button(self.TNotebook4_t1)
        self.Button29.place(relx=0.265, rely=0.246, height=24, width=47)
        self.Button29.configure(activebackground="#ececec")
        self.Button29.configure(activeforeground="#000000")
        self.Button29.configure(background="#d9d9d9")
        self.Button29.configure(command=self.Set6Licht)
        self.Button29.configure(disabledforeground="#a3a3a3")
        self.Button29.configure(foreground="#000000")
        self.Button29.configure(highlightbackground="#d9d9d9")
        self.Button29.configure(highlightcolor="black")
        self.Button29.configure(pady="0")
        self.Button29.configure(text='''Set''')

        self.Button30 = tk.Button(self.TNotebook4_t1)
        self.Button30.place(relx=0.265, rely=0.29, height=24, width=47)
        self.Button30.configure(activebackground="#ececec")
        self.Button30.configure(activeforeground="#000000")
        self.Button30.configure(background="#d9d9d9")
        self.Button30.configure(command=self.Set7Licht)
        self.Button30.configure(disabledforeground="#a3a3a3")
        self.Button30.configure(foreground="#000000")
        self.Button30.configure(highlightbackground="#d9d9d9")
        self.Button30.configure(highlightcolor="black")
        self.Button30.configure(pady="0")
        self.Button30.configure(text='''Set''')

        self.Button32 = tk.Button(self.TNotebook4_t1)
        self.Button32.place(relx=0.324, rely=0.072, height=24, width=39)
        self.Button32.configure(activebackground="#ececec")
        self.Button32.configure(activeforeground="#000000")
        self.Button32.configure(background="#d9d9d9")
        self.Button32.configure(command=unknown_support.Reset2Licht)
        self.Button32.configure(disabledforeground="#a3a3a3")
        self.Button32.configure(foreground="#000000")
        self.Button32.configure(highlightbackground="#d9d9d9")
        self.Button32.configure(highlightcolor="black")
        self.Button32.configure(pady="0")
        self.Button32.configure(text='''Reset''')

        self.Button33 = tk.Button(self.TNotebook4_t1)
        self.Button33.place(relx=0.324, rely=0.116, height=24, width=39)
        self.Button33.configure(activebackground="#ececec")
        self.Button33.configure(activeforeground="#000000")
        self.Button33.configure(background="#d9d9d9")
        self.Button33.configure(command=unknown_support.Reset3Licht)
        self.Button33.configure(disabledforeground="#a3a3a3")
        self.Button33.configure(foreground="#000000")
        self.Button33.configure(highlightbackground="#d9d9d9")
        self.Button33.configure(highlightcolor="black")
        self.Button33.configure(pady="0")
        self.Button33.configure(text='''Reset''')

        self.Button34 = tk.Button(self.TNotebook4_t1)
        self.Button34.place(relx=0.324, rely=0.159, height=24, width=39)
        self.Button34.configure(activebackground="#ececec")
        self.Button34.configure(activeforeground="#000000")
        self.Button34.configure(background="#d9d9d9")
        self.Button34.configure(command=unknown_support.Reset4Licht)
        self.Button34.configure(disabledforeground="#a3a3a3")
        self.Button34.configure(foreground="#000000")
        self.Button34.configure(highlightbackground="#d9d9d9")
        self.Button34.configure(highlightcolor="black")
        self.Button34.configure(pady="0")
        self.Button34.configure(text='''Reset''')

        self.Button35 = tk.Button(self.TNotebook4_t1)
        self.Button35.place(relx=0.324, rely=0.203, height=24, width=39)
        self.Button35.configure(activebackground="#ececec")
        self.Button35.configure(activeforeground="#000000")
        self.Button35.configure(background="#d9d9d9")
        self.Button35.configure(command=unknown_support.Reset5Licht)
        self.Button35.configure(disabledforeground="#a3a3a3")
        self.Button35.configure(foreground="#000000")
        self.Button35.configure(highlightbackground="#d9d9d9")
        self.Button35.configure(highlightcolor="black")
        self.Button35.configure(pady="0")
        self.Button35.configure(text='''Reset''')

        self.Button36 = tk.Button(self.TNotebook4_t1)
        self.Button36.place(relx=0.324, rely=0.246, height=24, width=39)
        self.Button36.configure(activebackground="#ececec")
        self.Button36.configure(activeforeground="#000000")
        self.Button36.configure(background="#d9d9d9")
        self.Button36.configure(command=unknown_support.Reset6Licht)
        self.Button36.configure(disabledforeground="#a3a3a3")
        self.Button36.configure(foreground="#000000")
        self.Button36.configure(highlightbackground="#d9d9d9")
        self.Button36.configure(highlightcolor="black")
        self.Button36.configure(pady="0")
        self.Button36.configure(text='''Reset''')

        self.Button37 = tk.Button(self.TNotebook4_t1)
        self.Button37.place(relx=0.324, rely=0.29, height=24, width=39)
        self.Button37.configure(activebackground="#ececec")
        self.Button37.configure(activeforeground="#000000")
        self.Button37.configure(background="#d9d9d9")
        self.Button37.configure(command=unknown_support.Reset7Licht)
        self.Button37.configure(disabledforeground="#a3a3a3")
        self.Button37.configure(foreground="#000000")
        self.Button37.configure(highlightbackground="#d9d9d9")
        self.Button37.configure(highlightcolor="black")
        self.Button37.configure(pady="0")
        self.Button37.configure(text='''Reset''')

        self.Button31 = tk.Button(self.TNotebook4_t1)
        self.Button31.place(relx=0.324, rely=0.029, height=24, width=39)
        self.Button31.configure(activebackground="#ececec")
        self.Button31.configure(activeforeground="#000000")
        self.Button31.configure(background="#d9d9d9")
        self.Button31.configure(command=unknown_support.Reset1Licht)
        self.Button31.configure(disabledforeground="#a3a3a3")
        self.Button31.configure(foreground="#000000")
        self.Button31.configure(highlightbackground="#d9d9d9")
        self.Button31.configure(highlightcolor="black")
        self.Button31.configure(pady="0")
        self.Button31.configure(text='''Reset''')

        self.Checkbutton7 = tk.Checkbutton(self.TNotebook4_t1)
        self.Checkbutton7.place(relx=0.088, rely=0.391, relheight=0.036
                                , relwidth=0.06)
        self.Checkbutton7.configure(activebackground="#ececec")
        self.Checkbutton7.configure(activeforeground="#000000")
        self.Checkbutton7.configure(background="#d9d9d9")
        self.Checkbutton7.configure(disabledforeground="#a3a3a3")
        self.Checkbutton7.configure(foreground="#000000")
        self.Checkbutton7.configure(highlightbackground="#d9d9d9")
        self.Checkbutton7.configure(highlightcolor="black")
        self.Checkbutton7.configure(justify='left')
        self.Checkbutton7.configure(text='''Check''')
        self.Checkbutton7.configure(variable=unknown_support.che72)

        self.Checkbutton8 = tk.Checkbutton(self.TNotebook4_t1)
        self.Checkbutton8.place(relx=0.088, rely=0.435, relheight=0.036
                                , relwidth=0.06)
        self.Checkbutton8.configure(activebackground="#ececec")
        self.Checkbutton8.configure(activeforeground="#000000")
        self.Checkbutton8.configure(background="#d9d9d9")
        self.Checkbutton8.configure(disabledforeground="#a3a3a3")
        self.Checkbutton8.configure(foreground="#000000")
        self.Checkbutton8.configure(highlightbackground="#d9d9d9")
        self.Checkbutton8.configure(highlightcolor="black")
        self.Checkbutton8.configure(justify='left')
        self.Checkbutton8.configure(text='''Check''')
        self.Checkbutton8.configure(variable=unknown_support.che73)

        self.Checkbutton9 = tk.Checkbutton(self.TNotebook4_t1)
        self.Checkbutton9.place(relx=0.088, rely=0.478, relheight=0.036
                                , relwidth=0.06)
        self.Checkbutton9.configure(activebackground="#ececec")
        self.Checkbutton9.configure(activeforeground="#000000")
        self.Checkbutton9.configure(background="#d9d9d9")
        self.Checkbutton9.configure(disabledforeground="#a3a3a3")
        self.Checkbutton9.configure(foreground="#000000")
        self.Checkbutton9.configure(highlightbackground="#d9d9d9")
        self.Checkbutton9.configure(highlightcolor="black")
        self.Checkbutton9.configure(justify='left')
        self.Checkbutton9.configure(text='''Check''')
        self.Checkbutton9.configure(variable=unknown_support.che74)

        self.Checkbutton10 = tk.Checkbutton(self.TNotebook4_t1)
        self.Checkbutton10.place(relx=0.157, rely=0.391, relheight=0.036
                                 , relwidth=0.06)
        self.Checkbutton10.configure(activebackground="#ececec")
        self.Checkbutton10.configure(activeforeground="#000000")
        self.Checkbutton10.configure(background="#d9d9d9")
        self.Checkbutton10.configure(disabledforeground="#a3a3a3")
        self.Checkbutton10.configure(foreground="#000000")
        self.Checkbutton10.configure(highlightbackground="#d9d9d9")
        self.Checkbutton10.configure(highlightcolor="black")
        self.Checkbutton10.configure(justify='left')
        self.Checkbutton10.configure(text='''Check''')
        self.Checkbutton10.configure(variable=unknown_support.che75)

        self.Checkbutton11 = tk.Checkbutton(self.TNotebook4_t1)
        self.Checkbutton11.place(relx=0.157, rely=0.435, relheight=0.036
                                 , relwidth=0.06)
        self.Checkbutton11.configure(activebackground="#ececec")
        self.Checkbutton11.configure(activeforeground="#000000")
        self.Checkbutton11.configure(background="#d9d9d9")
        self.Checkbutton11.configure(disabledforeground="#a3a3a3")
        self.Checkbutton11.configure(foreground="#000000")
        self.Checkbutton11.configure(highlightbackground="#d9d9d9")
        self.Checkbutton11.configure(highlightcolor="black")
        self.Checkbutton11.configure(justify='left')
        self.Checkbutton11.configure(text='''Check''')
        self.Checkbutton11.configure(variable=unknown_support.che76)

        self.Checkbutton12 = tk.Checkbutton(self.TNotebook4_t1)
        self.Checkbutton12.place(relx=0.157, rely=0.478, relheight=0.036
                                 , relwidth=0.06)
        self.Checkbutton12.configure(activebackground="#ececec")
        self.Checkbutton12.configure(activeforeground="#000000")
        self.Checkbutton12.configure(background="#d9d9d9")
        self.Checkbutton12.configure(disabledforeground="#a3a3a3")
        self.Checkbutton12.configure(foreground="#000000")
        self.Checkbutton12.configure(highlightbackground="#d9d9d9")
        self.Checkbutton12.configure(highlightcolor="black")
        self.Checkbutton12.configure(justify='left')
        self.Checkbutton12.configure(text='''Check''')
        self.Checkbutton12.configure(variable=unknown_support.che77)

        self.Button38 = tk.Button(self.TNotebook4_t1)
        self.Button38.place(relx=0.265, rely=0.333, height=24, width=47)
        self.Button38.configure(activebackground="#ececec")
        self.Button38.configure(activeforeground="#000000")
        self.Button38.configure(background="#d9d9d9")
        self.Button38.configure(command=self.Set8Licht)
        self.Button38.configure(disabledforeground="#a3a3a3")
        self.Button38.configure(foreground="#000000")
        self.Button38.configure(highlightbackground="#d9d9d9")
        self.Button38.configure(highlightcolor="black")
        self.Button38.configure(pady="0")
        self.Button38.configure(text='''Set''')

        self.Button39 = tk.Button(self.TNotebook4_t1)
        self.Button39.place(relx=0.265, rely=0.391, height=24, width=47)
        self.Button39.configure(activebackground="#ececec")
        self.Button39.configure(activeforeground="#000000")
        self.Button39.configure(background="#d9d9d9")
        self.Button39.configure(command=unknown_support.Set9Licht)
        self.Button39.configure(disabledforeground="#a3a3a3")
        self.Button39.configure(foreground="#000000")
        self.Button39.configure(highlightbackground="#d9d9d9")
        self.Button39.configure(highlightcolor="black")
        self.Button39.configure(pady="0")
        self.Button39.configure(text='''Set''')

        self.Button40 = tk.Button(self.TNotebook4_t1)
        self.Button40.place(relx=0.265, rely=0.435, height=24, width=47)
        self.Button40.configure(activebackground="#ececec")
        self.Button40.configure(activeforeground="#000000")
        self.Button40.configure(background="#d9d9d9")
        self.Button40.configure(command=unknown_support.Set10Licht)
        self.Button40.configure(disabledforeground="#a3a3a3")
        self.Button40.configure(foreground="#000000")
        self.Button40.configure(highlightbackground="#d9d9d9")
        self.Button40.configure(highlightcolor="black")
        self.Button40.configure(pady="0")
        self.Button40.configure(text='''Set''')

        self.Button41 = tk.Button(self.TNotebook4_t1)
        self.Button41.place(relx=0.324, rely=0.333, height=24, width=39)
        self.Button41.configure(activebackground="#ececec")
        self.Button41.configure(activeforeground="#000000")
        self.Button41.configure(background="#d9d9d9")
        self.Button41.configure(command=unknown_support.Reset8Licht)
        self.Button41.configure(disabledforeground="#a3a3a3")
        self.Button41.configure(foreground="#000000")
        self.Button41.configure(highlightbackground="#d9d9d9")
        self.Button41.configure(highlightcolor="black")
        self.Button41.configure(pady="0")
        self.Button41.configure(text='''Reset''')

        self.Button42 = tk.Button(self.TNotebook4_t1)
        self.Button42.place(relx=0.324, rely=0.391, height=24, width=39)
        self.Button42.configure(activebackground="#ececec")
        self.Button42.configure(activeforeground="#000000")
        self.Button42.configure(background="#d9d9d9")
        self.Button42.configure(command=unknown_support.Reset9Licht)
        self.Button42.configure(disabledforeground="#a3a3a3")
        self.Button42.configure(foreground="#000000")
        self.Button42.configure(highlightbackground="#d9d9d9")
        self.Button42.configure(highlightcolor="black")
        self.Button42.configure(pady="0")
        self.Button42.configure(text='''Reset''')

        self.Button43 = tk.Button(self.TNotebook4_t1)
        self.Button43.place(relx=0.324, rely=0.435, height=24, width=39)
        self.Button43.configure(activebackground="#ececec")
        self.Button43.configure(activeforeground="#000000")
        self.Button43.configure(background="#d9d9d9")
        self.Button43.configure(command=unknown_support.Reset10Licht)
        self.Button43.configure(disabledforeground="#a3a3a3")
        self.Button43.configure(foreground="#000000")
        self.Button43.configure(highlightbackground="#d9d9d9")
        self.Button43.configure(highlightcolor="black")
        self.Button43.configure(pady="0")
        self.Button43.configure(text='''Reset''')

        self.Entry24 = tk.Entry(self.TNotebook4_t1)
        self.Entry24.place(relx=0.088, rely=0.333, height=20, relwidth=0.161)
        self.Entry24.configure(background="white")
        self.Entry24.configure(disabledforeground="#a3a3a3")
        self.Entry24.configure(font="TkFixedFont")
        self.Entry24.configure(foreground="#000000")
        self.Entry24.configure(highlightbackground="#d9d9d9")
        self.Entry24.configure(highlightcolor="black")
        self.Entry24.configure(insertbackground="black")
        self.Entry24.configure(selectbackground="#c4c4c4")
        self.Entry24.configure(selectforeground="black")

        self.Button66 = tk.Button(self.TNotebook4_t1)
        self.Button66.place(relx=0.265, rely=0.478, height=24, width=47)
        self.Button66.configure(activebackground="#ececec")
        self.Button66.configure(activeforeground="#000000")
        self.Button66.configure(background="#d9d9d9")
        self.Button66.configure(command=unknown_support.Set11Licht)
        self.Button66.configure(disabledforeground="#a3a3a3")
        self.Button66.configure(foreground="#000000")
        self.Button66.configure(highlightbackground="#d9d9d9")
        self.Button66.configure(highlightcolor="black")
        self.Button66.configure(pady="0")
        self.Button66.configure(text='''Set''')

        self.Button67 = tk.Button(self.TNotebook4_t1)
        self.Button67.place(relx=0.324, rely=0.478, height=24, width=39)
        self.Button67.configure(activebackground="#ececec")
        self.Button67.configure(activeforeground="#000000")
        self.Button67.configure(background="#d9d9d9")
        self.Button67.configure(command=unknown_support.Reset11Licht)
        self.Button67.configure(disabledforeground="#a3a3a3")
        self.Button67.configure(foreground="#000000")
        self.Button67.configure(highlightbackground="#d9d9d9")
        self.Button67.configure(highlightcolor="black")
        self.Button67.configure(pady="0")
        self.Button67.configure(text='''Reset''')

        self.Label18 = tk.Label(self.TNotebook4_t1)
        self.Label18.place(relx=0.02, rely=0.333, height=21, width=43)
        self.Label18.configure(activebackground="#f9f9f9")
        self.Label18.configure(activeforeground="black")
        self.Label18.configure(background="#d9d9d9")
        self.Label18.configure(disabledforeground="#a3a3a3")
        self.Label18.configure(foreground="#000000")
        self.Label18.configure(highlightbackground="#d9d9d9")
        self.Label18.configure(highlightcolor="black")
        self.Label18.configure(text='''Setting''')

        self.Entry16 = tk.Entry(self.TNotebook4_t2)
        self.Entry16.place(relx=0.088, rely=0.029, height=20, relwidth=0.161)
        self.Entry16.configure(background="white")
        self.Entry16.configure(disabledforeground="#a3a3a3")
        self.Entry16.configure(font="TkFixedFont")
        self.Entry16.configure(foreground="#000000")
        self.Entry16.configure(highlightbackground="#d9d9d9")
        self.Entry16.configure(highlightcolor="black")
        self.Entry16.configure(insertbackground="black")
        self.Entry16.configure(selectbackground="#c4c4c4")
        self.Entry16.configure(selectforeground="black")

        self.Entry17 = tk.Entry(self.TNotebook4_t2)
        self.Entry17.place(relx=0.088, rely=0.072, height=20, relwidth=0.161)
        self.Entry17.configure(background="white")
        self.Entry17.configure(disabledforeground="#a3a3a3")
        self.Entry17.configure(font="TkFixedFont")
        self.Entry17.configure(foreground="#000000")
        self.Entry17.configure(highlightbackground="#d9d9d9")
        self.Entry17.configure(highlightcolor="black")
        self.Entry17.configure(insertbackground="black")
        self.Entry17.configure(selectbackground="#c4c4c4")
        self.Entry17.configure(selectforeground="black")

        self.Entry18 = tk.Entry(self.TNotebook4_t2)
        self.Entry18.place(relx=0.088, rely=0.116, height=20, relwidth=0.161)
        self.Entry18.configure(background="white")
        self.Entry18.configure(disabledforeground="#a3a3a3")
        self.Entry18.configure(font="TkFixedFont")
        self.Entry18.configure(foreground="#000000")
        self.Entry18.configure(highlightbackground="#d9d9d9")
        self.Entry18.configure(highlightcolor="black")
        self.Entry18.configure(insertbackground="black")
        self.Entry18.configure(selectbackground="#c4c4c4")
        self.Entry18.configure(selectforeground="black")

        self.Entry19 = tk.Entry(self.TNotebook4_t2)
        self.Entry19.place(relx=0.088, rely=0.159, height=20, relwidth=0.161)
        self.Entry19.configure(background="white")
        self.Entry19.configure(disabledforeground="#a3a3a3")
        self.Entry19.configure(font="TkFixedFont")
        self.Entry19.configure(foreground="#000000")
        self.Entry19.configure(highlightbackground="#d9d9d9")
        self.Entry19.configure(highlightcolor="black")
        self.Entry19.configure(insertbackground="black")
        self.Entry19.configure(selectbackground="#c4c4c4")
        self.Entry19.configure(selectforeground="black")

        self.Entry20 = tk.Entry(self.TNotebook4_t2)
        self.Entry20.place(relx=0.088, rely=0.203, height=20, relwidth=0.161)
        self.Entry20.configure(background="white")
        self.Entry20.configure(disabledforeground="#a3a3a3")
        self.Entry20.configure(font="TkFixedFont")
        self.Entry20.configure(foreground="#000000")
        self.Entry20.configure(highlightbackground="#d9d9d9")
        self.Entry20.configure(highlightcolor="black")
        self.Entry20.configure(insertbackground="black")
        self.Entry20.configure(selectbackground="#c4c4c4")
        self.Entry20.configure(selectforeground="black")

        self.Entry21 = tk.Entry(self.TNotebook4_t2)
        self.Entry21.place(relx=0.088, rely=0.246, height=20, relwidth=0.161)
        self.Entry21.configure(background="white")
        self.Entry21.configure(disabledforeground="#a3a3a3")
        self.Entry21.configure(font="TkFixedFont")
        self.Entry21.configure(foreground="#000000")
        self.Entry21.configure(highlightbackground="#d9d9d9")
        self.Entry21.configure(highlightcolor="black")
        self.Entry21.configure(insertbackground="black")
        self.Entry21.configure(selectbackground="#c4c4c4")
        self.Entry21.configure(selectforeground="black")

        self.Entry22 = tk.Entry(self.TNotebook4_t2)
        self.Entry22.place(relx=0.088, rely=0.29, height=20, relwidth=0.161)
        self.Entry22.configure(background="white")
        self.Entry22.configure(disabledforeground="#a3a3a3")
        self.Entry22.configure(font="TkFixedFont")
        self.Entry22.configure(foreground="#000000")
        self.Entry22.configure(highlightbackground="#d9d9d9")
        self.Entry22.configure(highlightcolor="black")
        self.Entry22.configure(insertbackground="black")
        self.Entry22.configure(selectbackground="#c4c4c4")
        self.Entry22.configure(selectforeground="black")

        self.Entry23 = tk.Entry(self.TNotebook4_t2)
        self.Entry23.place(relx=0.088, rely=0.333, height=20, relwidth=0.161)
        self.Entry23.configure(background="white")
        self.Entry23.configure(disabledforeground="#a3a3a3")
        self.Entry23.configure(font="TkFixedFont")
        self.Entry23.configure(foreground="#000000")
        self.Entry23.configure(highlightbackground="#d9d9d9")
        self.Entry23.configure(highlightcolor="black")
        self.Entry23.configure(insertbackground="black")
        self.Entry23.configure(selectbackground="#c4c4c4")
        self.Entry23.configure(selectforeground="black")

        self.Label10 = tk.Label(self.TNotebook4_t2)
        self.Label10.place(relx=0.02, rely=0.029, height=21, width=43)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(text='''Setting''')

        self.Label11 = tk.Label(self.TNotebook4_t2)
        self.Label11.place(relx=0.02, rely=0.072, height=21, width=44)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(highlightbackground="#d9d9d9")
        self.Label11.configure(highlightcolor="black")
        self.Label11.configure(text='''Setting''')

        self.Label12 = tk.Label(self.TNotebook4_t2)
        self.Label12.place(relx=0.02, rely=0.116, height=21, width=43)
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(activeforeground="black")
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(highlightbackground="#d9d9d9")
        self.Label12.configure(highlightcolor="black")
        self.Label12.configure(text='''Setting''')

        self.Label13 = tk.Label(self.TNotebook4_t2)
        self.Label13.place(relx=0.02, rely=0.159, height=21, width=43)
        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(activeforeground="black")
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(highlightbackground="#d9d9d9")
        self.Label13.configure(highlightcolor="black")
        self.Label13.configure(text='''Setting''')

        self.Label14 = tk.Label(self.TNotebook4_t2)
        self.Label14.place(relx=0.02, rely=0.203, height=21, width=43)
        self.Label14.configure(activebackground="#f9f9f9")
        self.Label14.configure(activeforeground="black")
        self.Label14.configure(background="#d9d9d9")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(highlightbackground="#d9d9d9")
        self.Label14.configure(highlightcolor="black")
        self.Label14.configure(text='''Setting''')

        self.Label15 = tk.Label(self.TNotebook4_t2)
        self.Label15.place(relx=0.02, rely=0.246, height=21, width=43)
        self.Label15.configure(activebackground="#f9f9f9")
        self.Label15.configure(activeforeground="black")
        self.Label15.configure(background="#d9d9d9")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(highlightbackground="#d9d9d9")
        self.Label15.configure(highlightcolor="black")
        self.Label15.configure(text='''Setting''')

        self.Label16 = tk.Label(self.TNotebook4_t2)
        self.Label16.place(relx=0.02, rely=0.29, height=21, width=43)
        self.Label16.configure(activebackground="#f9f9f9")
        self.Label16.configure(activeforeground="black")
        self.Label16.configure(background="#d9d9d9")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(highlightbackground="#d9d9d9")
        self.Label16.configure(highlightcolor="black")
        self.Label16.configure(text='''Setting''')

        self.Label17 = tk.Label(self.TNotebook4_t2)
        self.Label17.place(relx=0.02, rely=0.333, height=21, width=43)
        self.Label17.configure(activebackground="#f9f9f9")
        self.Label17.configure(activeforeground="black")
        self.Label17.configure(background="#d9d9d9")
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(foreground="#000000")
        self.Label17.configure(highlightbackground="#d9d9d9")
        self.Label17.configure(highlightcolor="black")
        self.Label17.configure(text='''Setting''')

        self.Button44 = tk.Button(self.TNotebook4_t2)
        self.Button44.place(relx=0.265, rely=0.029, height=24, width=47)
        self.Button44.configure(activebackground="#ececec")
        self.Button44.configure(activeforeground="#000000")
        self.Button44.configure(background="#d9d9d9")
        self.Button44.configure(command=self.Set1Afstand)
        self.Button44.configure(disabledforeground="#a3a3a3")
        self.Button44.configure(foreground="#000000")
        self.Button44.configure(highlightbackground="#d9d9d9")
        self.Button44.configure(highlightcolor="black")
        self.Button44.configure(pady="0")
        self.Button44.configure(text='''Set''')

        self.Button45 = tk.Button(self.TNotebook4_t2)
        self.Button45.place(relx=0.265, rely=0.072, height=24, width=47)
        self.Button45.configure(activebackground="#ececec")
        self.Button45.configure(activeforeground="#000000")
        self.Button45.configure(background="#d9d9d9")
        self.Button45.configure(command=self.Set2Afstand)
        self.Button45.configure(disabledforeground="#a3a3a3")
        self.Button45.configure(foreground="#000000")
        self.Button45.configure(highlightbackground="#d9d9d9")
        self.Button45.configure(highlightcolor="black")
        self.Button45.configure(pady="0")
        self.Button45.configure(text='''Set''')

        self.Button46 = tk.Button(self.TNotebook4_t2)
        self.Button46.place(relx=0.265, rely=0.116, height=24, width=47)
        self.Button46.configure(activebackground="#ececec")
        self.Button46.configure(activeforeground="#000000")
        self.Button46.configure(background="#d9d9d9")
        self.Button46.configure(command=self.Set3Afstand)
        self.Button46.configure(disabledforeground="#a3a3a3")
        self.Button46.configure(foreground="#000000")
        self.Button46.configure(highlightbackground="#d9d9d9")
        self.Button46.configure(highlightcolor="black")
        self.Button46.configure(pady="0")
        self.Button46.configure(text='''Set''')

        self.Button47 = tk.Button(self.TNotebook4_t2)
        self.Button47.place(relx=0.265, rely=0.159, height=24, width=47)
        self.Button47.configure(activebackground="#ececec")
        self.Button47.configure(activeforeground="#000000")
        self.Button47.configure(background="#d9d9d9")
        self.Button47.configure(command=self.Set4Afstand)
        self.Button47.configure(disabledforeground="#a3a3a3")
        self.Button47.configure(foreground="#000000")
        self.Button47.configure(highlightbackground="#d9d9d9")
        self.Button47.configure(highlightcolor="black")
        self.Button47.configure(pady="0")
        self.Button47.configure(text='''Set''')

        self.Button48 = tk.Button(self.TNotebook4_t2)
        self.Button48.place(relx=0.265, rely=0.203, height=24, width=47)
        self.Button48.configure(activebackground="#ececec")
        self.Button48.configure(activeforeground="#000000")
        self.Button48.configure(background="#d9d9d9")
        self.Button48.configure(command=self.Set5Afstand)
        self.Button48.configure(disabledforeground="#a3a3a3")
        self.Button48.configure(foreground="#000000")
        self.Button48.configure(highlightbackground="#d9d9d9")
        self.Button48.configure(highlightcolor="black")
        self.Button48.configure(pady="0")
        self.Button48.configure(text='''Set''')

        self.Button49 = tk.Button(self.TNotebook4_t2)
        self.Button49.place(relx=0.265, rely=0.246, height=24, width=47)
        self.Button49.configure(activebackground="#ececec")
        self.Button49.configure(activeforeground="#000000")
        self.Button49.configure(background="#d9d9d9")
        self.Button49.configure(command=self.Set6Afstand)
        self.Button49.configure(disabledforeground="#a3a3a3")
        self.Button49.configure(foreground="#000000")
        self.Button49.configure(highlightbackground="#d9d9d9")
        self.Button49.configure(highlightcolor="black")
        self.Button49.configure(pady="0")
        self.Button49.configure(text='''Set''')

        self.Button50 = tk.Button(self.TNotebook4_t2)
        self.Button50.place(relx=0.265, rely=0.29, height=24, width=47)
        self.Button50.configure(activebackground="#ececec")
        self.Button50.configure(activeforeground="#000000")
        self.Button50.configure(background="#d9d9d9")
        self.Button50.configure(command=self.Set7Afstand)
        self.Button50.configure(disabledforeground="#a3a3a3")
        self.Button50.configure(foreground="#000000")
        self.Button50.configure(highlightbackground="#d9d9d9")
        self.Button50.configure(highlightcolor="black")
        self.Button50.configure(pady="0")
        self.Button50.configure(text='''Set''')

        self.Button51 = tk.Button(self.TNotebook4_t2)
        self.Button51.place(relx=0.265, rely=0.333, height=24, width=47)
        self.Button51.configure(activebackground="#ececec")
        self.Button51.configure(activeforeground="#000000")
        self.Button51.configure(background="#d9d9d9")
        self.Button51.configure(command=self.Set8Afstand)
        self.Button51.configure(disabledforeground="#a3a3a3")
        self.Button51.configure(foreground="#000000")
        self.Button51.configure(highlightbackground="#d9d9d9")
        self.Button51.configure(highlightcolor="black")
        self.Button51.configure(pady="0")
        self.Button51.configure(text='''Set''')

        self.Button52 = tk.Button(self.TNotebook4_t2)
        self.Button52.place(relx=0.324, rely=0.029, height=24, width=39)
        self.Button52.configure(activebackground="#ececec")
        self.Button52.configure(activeforeground="#000000")
        self.Button52.configure(background="#d9d9d9")
        self.Button52.configure(command=unknown_support.Reset1Afstand)
        self.Button52.configure(disabledforeground="#a3a3a3")
        self.Button52.configure(foreground="#000000")
        self.Button52.configure(highlightbackground="#d9d9d9")
        self.Button52.configure(highlightcolor="black")
        self.Button52.configure(pady="0")
        self.Button52.configure(text='''Reset''')

        self.Button53 = tk.Button(self.TNotebook4_t2)
        self.Button53.place(relx=0.324, rely=0.072, height=24, width=39)
        self.Button53.configure(activebackground="#ececec")
        self.Button53.configure(activeforeground="#000000")
        self.Button53.configure(background="#d9d9d9")
        self.Button53.configure(command=unknown_support.Reset2Afstand)
        self.Button53.configure(disabledforeground="#a3a3a3")
        self.Button53.configure(foreground="#000000")
        self.Button53.configure(highlightbackground="#d9d9d9")
        self.Button53.configure(highlightcolor="black")
        self.Button53.configure(pady="0")
        self.Button53.configure(text='''Reset''')

        self.Button54 = tk.Button(self.TNotebook4_t2)
        self.Button54.place(relx=0.324, rely=0.116, height=24, width=39)
        self.Button54.configure(activebackground="#ececec")
        self.Button54.configure(activeforeground="#000000")
        self.Button54.configure(background="#d9d9d9")
        self.Button54.configure(command=unknown_support.Reset3Afstand)
        self.Button54.configure(disabledforeground="#a3a3a3")
        self.Button54.configure(foreground="#000000")
        self.Button54.configure(highlightbackground="#d9d9d9")
        self.Button54.configure(highlightcolor="black")
        self.Button54.configure(pady="0")
        self.Button54.configure(text='''Reset''')

        self.Button55 = tk.Button(self.TNotebook4_t2)
        self.Button55.place(relx=0.324, rely=0.159, height=24, width=39)
        self.Button55.configure(activebackground="#ececec")
        self.Button55.configure(activeforeground="#000000")
        self.Button55.configure(background="#d9d9d9")
        self.Button55.configure(command=unknown_support.Reset4Afstand)
        self.Button55.configure(disabledforeground="#a3a3a3")
        self.Button55.configure(foreground="#000000")
        self.Button55.configure(highlightbackground="#d9d9d9")
        self.Button55.configure(highlightcolor="black")
        self.Button55.configure(pady="0")
        self.Button55.configure(text='''Reset''')

        self.Button56 = tk.Button(self.TNotebook4_t2)
        self.Button56.place(relx=0.324, rely=0.203, height=24, width=39)
        self.Button56.configure(activebackground="#ececec")
        self.Button56.configure(activeforeground="#000000")
        self.Button56.configure(background="#d9d9d9")
        self.Button56.configure(command=unknown_support.Reset5Afstand)
        self.Button56.configure(disabledforeground="#a3a3a3")
        self.Button56.configure(foreground="#000000")
        self.Button56.configure(highlightbackground="#d9d9d9")
        self.Button56.configure(highlightcolor="black")
        self.Button56.configure(pady="0")
        self.Button56.configure(text='''Reset''')

        self.Button57 = tk.Button(self.TNotebook4_t2)
        self.Button57.place(relx=0.324, rely=0.246, height=24, width=39)
        self.Button57.configure(activebackground="#ececec")
        self.Button57.configure(activeforeground="#000000")
        self.Button57.configure(background="#d9d9d9")
        self.Button57.configure(command=unknown_support.Reset6Afstand)
        self.Button57.configure(disabledforeground="#a3a3a3")
        self.Button57.configure(foreground="#000000")
        self.Button57.configure(highlightbackground="#d9d9d9")
        self.Button57.configure(highlightcolor="black")
        self.Button57.configure(pady="0")
        self.Button57.configure(text='''Reset''')

        self.Button58 = tk.Button(self.TNotebook4_t2)
        self.Button58.place(relx=0.324, rely=0.29, height=24, width=39)
        self.Button58.configure(activebackground="#ececec")
        self.Button58.configure(activeforeground="#000000")
        self.Button58.configure(background="#d9d9d9")
        self.Button58.configure(command=unknown_support.Reset7Afstand)
        self.Button58.configure(disabledforeground="#a3a3a3")
        self.Button58.configure(foreground="#000000")
        self.Button58.configure(highlightbackground="#d9d9d9")
        self.Button58.configure(highlightcolor="black")
        self.Button58.configure(pady="0")
        self.Button58.configure(text='''Reset''')

        self.Button59 = tk.Button(self.TNotebook4_t2)
        self.Button59.place(relx=0.324, rely=0.333, height=24, width=39)
        self.Button59.configure(activebackground="#ececec")
        self.Button59.configure(activeforeground="#000000")
        self.Button59.configure(background="#d9d9d9")
        self.Button59.configure(command=unknown_support.Reset8Afstand)
        self.Button59.configure(disabledforeground="#a3a3a3")
        self.Button59.configure(foreground="#000000")
        self.Button59.configure(highlightbackground="#d9d9d9")
        self.Button59.configure(highlightcolor="black")
        self.Button59.configure(pady="0")
        self.Button59.configure(text='''Reset''')

        self.Checkbutton13 = tk.Checkbutton(self.TNotebook4_t2)
        self.Checkbutton13.place(relx=0.088, rely=0.391, relheight=0.036
                                 , relwidth=0.06)
        self.Checkbutton13.configure(activebackground="#ececec")
        self.Checkbutton13.configure(activeforeground="#000000")
        self.Checkbutton13.configure(background="#d9d9d9")
        self.Checkbutton13.configure(disabledforeground="#a3a3a3")
        self.Checkbutton13.configure(foreground="#000000")
        self.Checkbutton13.configure(highlightbackground="#d9d9d9")
        self.Checkbutton13.configure(highlightcolor="black")
        self.Checkbutton13.configure(justify='left')
        self.Checkbutton13.configure(text='''Check''')
        self.Checkbutton13.configure(variable=unknown_support.che120)

        self.Checkbutton14 = tk.Checkbutton(self.TNotebook4_t2)
        self.Checkbutton14.place(relx=0.088, rely=0.435, relheight=0.036
                                 , relwidth=0.06)
        self.Checkbutton14.configure(activebackground="#ececec")
        self.Checkbutton14.configure(activeforeground="#000000")
        self.Checkbutton14.configure(background="#d9d9d9")
        self.Checkbutton14.configure(disabledforeground="#a3a3a3")
        self.Checkbutton14.configure(foreground="#000000")
        self.Checkbutton14.configure(highlightbackground="#d9d9d9")
        self.Checkbutton14.configure(highlightcolor="black")
        self.Checkbutton14.configure(justify='left')
        self.Checkbutton14.configure(text='''Check''')
        self.Checkbutton14.configure(variable=unknown_support.che121)

        self.Checkbutton15 = tk.Checkbutton(self.TNotebook4_t2)
        self.Checkbutton15.place(relx=0.088, rely=0.478, relheight=0.036
                                 , relwidth=0.06)
        self.Checkbutton15.configure(activebackground="#ececec")
        self.Checkbutton15.configure(activeforeground="#000000")
        self.Checkbutton15.configure(background="#d9d9d9")
        self.Checkbutton15.configure(disabledforeground="#a3a3a3")
        self.Checkbutton15.configure(foreground="#000000")
        self.Checkbutton15.configure(highlightbackground="#d9d9d9")
        self.Checkbutton15.configure(highlightcolor="black")
        self.Checkbutton15.configure(justify='left')
        self.Checkbutton15.configure(text='''Check''')
        self.Checkbutton15.configure(variable=unknown_support.che122)

        self.Checkbutton16 = tk.Checkbutton(self.TNotebook4_t2)
        self.Checkbutton16.place(relx=0.157, rely=0.391, relheight=0.036
                                 , relwidth=0.06)
        self.Checkbutton16.configure(activebackground="#ececec")
        self.Checkbutton16.configure(activeforeground="#000000")
        self.Checkbutton16.configure(background="#d9d9d9")
        self.Checkbutton16.configure(disabledforeground="#a3a3a3")
        self.Checkbutton16.configure(foreground="#000000")
        self.Checkbutton16.configure(highlightbackground="#d9d9d9")
        self.Checkbutton16.configure(highlightcolor="black")
        self.Checkbutton16.configure(justify='left')
        self.Checkbutton16.configure(text='''Check''')
        self.Checkbutton16.configure(variable=unknown_support.che123)

        self.Checkbutton17 = tk.Checkbutton(self.TNotebook4_t2)
        self.Checkbutton17.place(relx=0.157, rely=0.435, relheight=0.036
                                 , relwidth=0.06)
        self.Checkbutton17.configure(activebackground="#ececec")
        self.Checkbutton17.configure(activeforeground="#000000")
        self.Checkbutton17.configure(background="#d9d9d9")
        self.Checkbutton17.configure(disabledforeground="#a3a3a3")
        self.Checkbutton17.configure(foreground="#000000")
        self.Checkbutton17.configure(highlightbackground="#d9d9d9")
        self.Checkbutton17.configure(highlightcolor="black")
        self.Checkbutton17.configure(justify='left')
        self.Checkbutton17.configure(text='''Check''')
        self.Checkbutton17.configure(variable=unknown_support.che124)

        self.Checkbutton18 = tk.Checkbutton(self.TNotebook4_t2)
        self.Checkbutton18.place(relx=0.157, rely=0.478, relheight=0.036
                                 , relwidth=0.06)
        self.Checkbutton18.configure(activebackground="#ececec")
        self.Checkbutton18.configure(activeforeground="#000000")
        self.Checkbutton18.configure(background="#d9d9d9")
        self.Checkbutton18.configure(disabledforeground="#a3a3a3")
        self.Checkbutton18.configure(foreground="#000000")
        self.Checkbutton18.configure(highlightbackground="#d9d9d9")
        self.Checkbutton18.configure(highlightcolor="black")
        self.Checkbutton18.configure(justify='left')
        self.Checkbutton18.configure(text='''Check''')
        self.Checkbutton18.configure(variable=unknown_support.che125)

        self.Button60 = tk.Button(self.TNotebook4_t2)
        self.Button60.place(relx=0.265, rely=0.391, height=24, width=47)
        self.Button60.configure(activebackground="#ececec")
        self.Button60.configure(activeforeground="#000000")
        self.Button60.configure(background="#d9d9d9")
        self.Button60.configure(command=unknown_support.Set9Afstand)
        self.Button60.configure(disabledforeground="#a3a3a3")
        self.Button60.configure(foreground="#000000")
        self.Button60.configure(highlightbackground="#d9d9d9")
        self.Button60.configure(highlightcolor="black")
        self.Button60.configure(pady="0")
        self.Button60.configure(text='''Set''')

        self.Button61 = tk.Button(self.TNotebook4_t2)
        self.Button61.place(relx=0.265, rely=0.435, height=24, width=47)
        self.Button61.configure(activebackground="#ececec")
        self.Button61.configure(activeforeground="#000000")
        self.Button61.configure(background="#d9d9d9")
        self.Button61.configure(command=unknown_support.Set10Afstand)
        self.Button61.configure(disabledforeground="#a3a3a3")
        self.Button61.configure(foreground="#000000")
        self.Button61.configure(highlightbackground="#d9d9d9")
        self.Button61.configure(highlightcolor="black")
        self.Button61.configure(pady="0")
        self.Button61.configure(text='''Set''')

        self.Button62 = tk.Button(self.TNotebook4_t2)
        self.Button62.place(relx=0.265, rely=0.478, height=24, width=47)
        self.Button62.configure(activebackground="#ececec")
        self.Button62.configure(activeforeground="#000000")
        self.Button62.configure(background="#d9d9d9")
        self.Button62.configure(command=unknown_support.Set11Afstand)
        self.Button62.configure(disabledforeground="#a3a3a3")
        self.Button62.configure(foreground="#000000")
        self.Button62.configure(highlightbackground="#d9d9d9")
        self.Button62.configure(highlightcolor="black")
        self.Button62.configure(pady="0")
        self.Button62.configure(text='''Set''')

        self.Button63 = tk.Button(self.TNotebook4_t2)
        self.Button63.place(relx=0.324, rely=0.391, height=24, width=39)
        self.Button63.configure(activebackground="#ececec")
        self.Button63.configure(activeforeground="#000000")
        self.Button63.configure(background="#d9d9d9")
        self.Button63.configure(command=unknown_support.Reset9Afstand)
        self.Button63.configure(disabledforeground="#a3a3a3")
        self.Button63.configure(foreground="#000000")
        self.Button63.configure(highlightbackground="#d9d9d9")
        self.Button63.configure(highlightcolor="black")
        self.Button63.configure(pady="0")
        self.Button63.configure(text='''Reset''')

        self.Button64 = tk.Button(self.TNotebook4_t2)
        self.Button64.place(relx=0.324, rely=0.435, height=24, width=39)
        self.Button64.configure(activebackground="#ececec")
        self.Button64.configure(activeforeground="#000000")
        self.Button64.configure(background="#d9d9d9")
        self.Button64.configure(command=unknown_support.Reset10Afstand)
        self.Button64.configure(disabledforeground="#a3a3a3")
        self.Button64.configure(foreground="#000000")
        self.Button64.configure(highlightbackground="#d9d9d9")
        self.Button64.configure(highlightcolor="black")
        self.Button64.configure(pady="0")
        self.Button64.configure(text='''Reset''')

        self.Button65 = tk.Button(self.TNotebook4_t2)
        self.Button65.place(relx=0.324, rely=0.478, height=24, width=39)
        self.Button65.configure(activebackground="#ececec")
        self.Button65.configure(activeforeground="#000000")
        self.Button65.configure(background="#d9d9d9")
        self.Button65.configure(command=unknown_support.Reset11Afstand)
        self.Button65.configure(disabledforeground="#a3a3a3")
        self.Button65.configure(foreground="#000000")
        self.Button65.configure(highlightbackground="#d9d9d9")
        self.Button65.configure(highlightcolor="black")
        self.Button65.configure(pady="0")
        self.Button65.configure(text='''Reset''')

        self.Label1 = tk.Label(self.TNotebook1_t3)
        self.Label1.place(relx=0.01, rely=0.014, height=391, width=674)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Cuckservative
From Wikipedia, the free encyclopedia
Jump to navigationJump to search
"Cuckservative" is a pejorative[1] formed as a portmanteau of "cuck", a shortened form of the word cuckold, and the political designation conservative.[2] It has become a label used by white nationalists and the alt-right in the United States.[3][4][5][6]

The word "cuckservative" reached a high level of mainstream political conversation around mid-July 2015, where it gained media attention just a few weeks before the start of the first Republican primary debate for the 2016 United States presidential election.[4][7]

The term, as well as the shortened form "cuck" for cuckold, originated on websites such as 4chan (specifically the /pol/ imageboard) and 8chan, the right-wing message board My Posting Career,[1][3] the blog The Right Stuff,[8] and other sites in the alt-right movement.[3][9][10]''')

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)
        self.s = 1
        self.x2 = 50
        self.y2 = 0
        self.running = True
        self.setup_arduinos()
        time.sleep(5)
        self.counter = 0
        self.loop()

    def setup_arduinos(self):
        global comPorts, activeComPorts
        for i in comPorts:
            l = str(i).split()
            activeComPorts.append(l[0])

        for comPort in activeComPorts:
            ser = serial.Serial(comPort, 19200)
            time.sleep(3)
            test = bytearray(b'\xf3')
            ser.write(test)
            if ser.read() == bytearray(b'\xf3'):
                arduinos.append(ser)


    def loop(self):
        global aantal, getallen, aantal_huidig, arduinos
        if self.counter == 50:
            self.animatecanvas1(randint(0,5))
            self.animatecanvas2(randint(0, 5))
            self.animatecanvas3(randint(0, 5))
            self.animatecanvas4(randint(0, 5))
            self.animatecanvas5(randint(0, 5))
            self.animatecanvas6(randint(0, 5))
            self.animatecanvas7(randint(0, 5))
            self.animatecanvas8(randint(0, 5))
            self.animatecanvas9(randint(0, 5))
            self.animatecanvas10(randint(0, 5))
            self.animatecanvas11(randint(0, 5))
            self.counter = 0
        for ser in arduinos:
            if ser.in_waiting > 0:
                if ser.read().hex() == 'ff':
                    scale = 16
                    num_of_bits = 8
                    binary_value = ""
                    for i in range(4):
                        binary_value = binary_value + str(bin(int(ser.read().hex(), scale))[2:].zfill(num_of_bits))
                    binary_value = str(binary_value)
                    light = binary_value[0:2]
                    light = light[::-1]
                    temp = binary_value[10:20]
                    temp = temp[::-1]
                    distance = binary_value[2:10]
                    distance = distance[::-1]
                    light2 = binary_value[20:27]
                    light2 = light2[::-1]
                    bit_controle = binary_value[27:]
                    bit_controle = bit_controle[::-1]
                    temp = int(temp, 2)
                    light2 = int(light2, 2)
                    distance = int(distance, 2)
                    light = int(light, 2)
                    bit_controle = int(bit_controle, 2)
                    print("Temperatuur: " + str(temp), "Lichtsensor: " + str(light2), "Distance: " + str(distance),
                          "What light: " + str(light), "Controle: " + str(bit_controle))
                    getallen.append(int(distance))
                    aantal+=1
                if aantal > aantal_huidig:
                    aantal_huidig = aantal
        self.counter += 1
        root.after(10, self.loop)

    def animatecanvas1(self, y):
        self.canvasx.append(self.newx)
        if len(self.canvasx) > 20:
            del self.canvasx[0]
            del self.canvas1y[0]
            self.canvas1.clear()
        self.canvas1y.append(y)
        self.newx += 1
        self.canvas1.plot(self.canvasx, self.canvas1y , color= "blue")
        self.canvas1a.draw()

    def animatecanvas2(self, y):
        self.canvas2x.append(self.new2x)
        if len(self.canvas2x) > 20:
            del self.canvas2x[0]
            del self.canvas2y[0]
            self.canvas2.clear()
        self.canvas2y.append(y)
        self.new2x += 1
        self.canvas2.plot(self.canvas2x, self.canvas2y , color= "blue")
        self.canvas2a.draw()

    def animatecanvas3(self, y):
        self.canvas3x.append(self.new3x)
        if len(self.canvas3x) > 20:
            del self.canvas3x[0]
            del self.canvas3y[0]
            self.canvas3.clear()
        self.canvas3y.append(y)
        self.new3x += 1
        self.canvas3.plot(self.canvas3x, self.canvas3y , color= "blue")
        self.canvas3a.draw()

    def animatecanvas4(self, y):
        self.canvas4x.append(self.new4x)
        if len(self.canvas4x) > 20:
            del self.canvas4x[0]
            del self.canvas4y[0]
            self.canvas4.clear()
        self.canvas4y.append(y)
        self.new4x += 1
        self.canvas4.plot(self.canvas4x, self.canvas4y , color= "blue")
        self.canvas4a.draw()

    def animatecanvas5(self, y):
        self.canvas5x.append(self.new5x)
        if len(self.canvas5x) > 20:
            del self.canvas5x[0]
            del self.canvas5y[0]
            self.canvas5.clear()
        self.canvas5y.append(y)
        self.new5x += 1
        self.canvas5.plot(self.canvas5x, self.canvas5y , color= "blue")
        self.canvas4a.draw()

    def animatecanvas6(self, y):
        self.canvas6x.append(self.new6x)
        if len(self.canvas6x) > 20:
            del self.canvas6x[0]
            del self.canvas6y[0]
            self.canvas6.clear()
        self.canvas6y.append(y)
        self.new6x += 1
        self.canvas6.plot(self.canvas6x, self.canvas6y , color= "blue")
        self.canvas5a.draw()

    def animatecanvas7(self, y):
        self.canvas7x.append(self.new7x)
        if len(self.canvas7x) > 20:
            del self.canvas7x[0]
            del self.canvas7y[0]
            self.canvas7.clear()
        self.canvas7y.append(y)
        self.new7x += 1
        self.canvas7.plot(self.canvas7x, self.canvas7y , color= "blue")
        self.canvas5a.draw()

    def animatecanvas8(self, y):
        self.canvas8x.append(self.new8x)
        if len(self.canvas8x) > 20:
            del self.canvas8x[0]
            del self.canvas8y[0]
            self.canvas8.clear()
        self.canvas8y.append(y)
        self.new8x += 1
        self.canvas8.plot(self.canvas8x, self.canvas8y , color= "blue")
        self.canvas6a.draw()

    def animatecanvas9(self, y):
        self.canvas9x.append(self.new9x)
        if len(self.canvas9x) > 20:
            del self.canvas9x[0]
            del self.canvas9y[0]
            self.canvas9.clear()
        self.canvas9y.append(y)
        self.new9x += 1
        self.canvas9.plot(self.canvas9x, self.canvas9y , color= "blue")
        self.canvas6a.draw()

    def animatecanvas10(self, y):
        self.canvas10x.append(self.new10x)
        if len(self.canvas10x) > 20:
            del self.canvas10x[0]
            del self.canvas10y[0]
            self.canvas10.clear()
        self.canvas10y.append(y)
        self.new10x += 1
        self.canvas10.plot(self.canvas10x, self.canvas10y , color= "blue")
        self.canvas7a.draw()

    def animatecanvas11(self, y):
        self.canvas11x.append(self.new11x)
        if len(self.canvas11x) > 20:
            del self.canvas11x[0]
            del self.canvas11y[0]
            self.canvas11.clear()
        self.canvas11y.append(y)
        self.new11x += 1
        self.canvas11.plot(self.canvas11x, self.canvas11y , color= "blue")
        self.canvas7a.draw()

    def Set1Temperatuur(self):
        print(self.Entry1.get())

    def Set2Temperatuur(self):
        print(self.Entry2.get())

    def Set3Temperatuur(self):
        print(self.Entry3.get())

    def Set4Temperatuur(self):
        print(self.Entry4.get())

    def Set5Temperatuur(self):
        print(self.Entry5.get())

    def Set6Temperatuur(self):
        print(self.Entry6.get())

    def Set7Temperatuur(self):
        print(self.Entry7.get())

    def Set8Temperatuur(self):
        print(self.Entry8.get())

    def Set1Licht(self):
        print(self.Entry9.get())

    def Set2Licht(self):
        print(self.Entry10.get())

    def Set3Licht(self):
        print(self.Entry11.get())

    def Set4Licht(self):
        print(self.Entry12.get())

    def Set5Licht(self):
        print(self.Entry13.get())

    def Set6Licht(self):
        print(self.Entry14.get())

    def Set7Licht(self):
        print(self.Entry15.get())

    def Set8Licht(self):
        print(self.Entry24.get())

    def Set1Afstand(self):
        print(self.Entry16.get())

    def Set2Afstand(self):
        print(self.Entry17.get())

    def Set3Afstand(self):
        print(self.Entry18.get())

    def Set4Afstand(self):
        print(self.Entry19.get())

    def Set5Afstand(self):
        print(self.Entry20.get())

    def Set6Afstand(self):
        print(self.Entry21.get())

    def Set7Afstand(self):
        print(self.Entry22.get())

    def Set8Afstand(self):
        print(self.Entry23.get())

    def SetBar1Data(self, AD1, AD2, AD3, AD4):
        self.data1 = (AD1, AD2, AD3, AD4)
        self.ax1.clear()
        self.ax1.bar(self.ind, self.data1, .5)
        self.canvasbar1.draw()

    def SetBar2Data(self, AD1, AD2, AD3, AD4):
        self.data2 = (AD1, AD2, AD3, AD4)
        self.ax2.clear()
        self.ax2.bar(self.ind, self.data1, .5)
        self.canvasbar2.draw()

    def SetBar3Data(self, AD1, AD2, AD3, AD4):
        self.data3 = (AD1, AD2, AD3, AD4)
        self.ax3.clear()
        self.ax3.bar(self.ind, self.data1, .5)
        self.canvasbar3.draw()

    def FillListbox1(self, string):
        self.Listbox1.delete(0, END)
        self.Listbox1.insert(1, string)

    def FillListbox2(self, string):
        self.Listbox2.delete(0, END)
        self.Listbox2.insert(1, string)

if __name__ == '__main__':
    vp_start_gui()



