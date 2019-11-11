import sys
from tkinter import *
import serial
import time
from send_data import *

import _thread
import queue
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


aantal = 0
aantal_huidig = 0
getallen = []
comPorts = []


class ThreadSafeConsole(Text):
    def __init__(self, master, **options):
        Text.__init__(self, master, **options)
        self.queue = queue.Queue()
        self.update_me()
    
    def write(self, line):
        self.queue.put(line)
    
    def clear(self):
        self.queue.put(None)
    
    def update_me(self):
        try:
            while 1:
                line = self.queue.get_nowait()
                if line is None:
                    self.delete(1.0, END)
                else:
                    self.insert(END, str(line))
                self.see(END)
                self.update_idletasks()
        except queue.Empty:
            pass
        self.after(100, self.update_me)


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    ding = ThreadSafeConsole(root)
    top = TopLevel1(root)
    _thread.start_new(loop_loop, ())
    root.mainloop()


w = None


def create_toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = TopLevel1(w)
    return w, top


def destroy_toplevel1():
    global w
    w.destroy()
    w = None


class TopLevel1:
    def __init__(self, top=None):
        self.arduinos = []
        self.activeComPorts = []
        self.total_data = [[], [], [], [], []]
        self.maxtemp = 25
        self.maxlight = 80
        self.mindistance = 20
        self.maxdistance = 140
        self.run_config = True
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        self.buttonstyle = ttk.Style()
        self.redbutton = ttk.Style()
        self.greenbutton = ttk.Style()
        self.buttonstyle.configure('Custom.TButton', padding=1, relief="flat", background="black")
        self.redbutton.configure('Red.TButton', padding=1, relief="flat", background="red", foreground="black")
        self.greenbutton.configure('Green.TButton', padding=1, relief="flat", background="green", foreground="black")
        top.geometry("1400x840+478+139")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("CUCKS GUI")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.style.configure('TNotebook.Tab', background=_bgcolor, foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=[('selected', _compcolor), ('active', _ana2color)])
        self.t_notebook_1 = ttk.Notebook(top)
        self.t_notebook_1.place(relx=0.0, rely=0.0, relheight=1.003, relwidth=1.002)
        self.t_notebook_1.configure(takefocus="")

        self.t_notebook_1_t0 = tk.Frame(self.t_notebook_1)
        self.t_notebook_1.add(self.t_notebook_1_t0, padding=3)
        self.t_notebook_1.tab(0, text="Dashboard", compound="left", underline="-1", )
        self.t_notebook_1_t0.configure(highlightbackground="#d9d9d9", background="#d9d9d9", highlightcolor="black")

        self.t_notebook_1_t1 = tk.Frame(self.t_notebook_1)
        self.t_notebook_1.add(self.t_notebook_1_t1, padding=3)
        self.t_notebook_1.tab(1, text="Graph", compound="left", underline="-1", )
        self.t_notebook_1_t1.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        self.t_notebook_1_t2 = tk.Frame(self.t_notebook_1)
        self.t_notebook_1.add(self.t_notebook_1_t2, padding=3)
        self.t_notebook_1.tab(2, text="Config", compound="none", underline="-1", )
        self.t_notebook_1_t2.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        self.t_notebook_1_t3 = tk.Frame(self.t_notebook_1)
        self.t_notebook_1.add(self.t_notebook_1_t3, padding=3)
        self.t_notebook_1.tab(3, text="Help", compound="none", underline="-1", )
        self.t_notebook_1_t3.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        self.t_notebook_2 = ttk.Notebook(self.t_notebook_1_t0)
        self.t_notebook_2.place(relx=0.291, rely=0.014, relheight=0.241, relwidth=0.68)
        self.t_notebook_2.configure(takefocus="")
        self.t_notebook_2_t0 = tk.Frame(self.t_notebook_2)
        self.t_notebook_2.add(self.t_notebook_2_t0, padding=3)
        self.t_notebook_2.tab(0, text="Afstandsensor", compound="left", underline="-1", )
        self.t_notebook_2_t0.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")
        bar1 = Figure(figsize=(5, 2), dpi=75)
        self.ax1 = bar1.add_subplot(111)

        self.data1 = (20, 45, 30, 35)
        self.ax1.set_title('NIET AANGESLOTEN', color="red")
        self.ind = np.arange(5)  # the x locations for the groups

        self.t_notebook_2_t1 = tk.Frame(self.t_notebook_2)
        self.t_notebook_2.add(self.t_notebook_2_t1, padding=3)
        self.t_notebook_2.tab(1, text="Lichtsensor", compound="left", underline="-1")
        self.t_notebook_2_t1.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")
        bar2 = Figure(figsize=(5, 2), dpi=75)
        self.ax2 = bar2.add_subplot(111)
        self.ax2.set_title('NIET AANGESLOTEN', color="red")
        self.data2 = (20, 35, 30, 35)

        self.t_notebook_2_t2 = tk.Frame(self.t_notebook_2)
        self.t_notebook_2.add(self.t_notebook_2_t2, padding=3)
        self.t_notebook_2.tab(2, text="Temperatuur", compound="none", underline="-1")
        self.t_notebook_2_t2.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        self.t_notebook_3 = ttk.Notebook(self.t_notebook_1_t1)
        self.t_notebook_3.place(relx=0.0, rely=0.014, relheight=0.995, relwidth=1.004)
        self.t_notebook_3.configure(takefocus="")
        self.t_notebook_3_t0 = tk.Frame(self.t_notebook_3)
        self.t_notebook_3.add(self.t_notebook_3_t0, padding=3)
        self.t_notebook_3.tab(0, text="Arduino 1", compound="left", underline="-1")
        self.t_notebook_3_t0.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")
        self.t_notebook_3_t1 = tk.Frame(self.t_notebook_3)
        self.t_notebook_3.add(self.t_notebook_3_t1, padding=3)
        self.t_notebook_3.tab(1, text="Arduino 2", compound="left", underline="-1")
        self.t_notebook_3_t1.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")
        self.t_notebook_3_t2 = tk.Frame(self.t_notebook_3)
        self.t_notebook_3.add(self.t_notebook_3_t2, padding=3)
        self.t_notebook_3.tab(2, text="Arduino 3", compound="none", underline="-1")
        self.t_notebook_3_t2.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")
        self.t_notebook_3_t3 = tk.Frame(self.t_notebook_3)
        self.t_notebook_3.add(self.t_notebook_3_t3, padding=3)
        self.t_notebook_3.tab(3, text="Arduino 4", compound="none", underline="-1")
        self.t_notebook_3_t3.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")
        self.t_notebook_3_t4 = tk.Frame(self.t_notebook_3)
        self.t_notebook_3.add(self.t_notebook_3_t4, padding=3)
        self.t_notebook_3.tab(4, text="Arduino 5", compound="none", underline="-1")
        self.t_notebook_3_t4.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        self.t_notebook_4 = ttk.Notebook(self.t_notebook_1_t2)
        self.t_notebook_4.place(relx=0.0, rely=0.014, relheight=0.981, relwidth=0.994)
        self.t_notebook_4.configure(takefocus="")

        self.t_notebook_4_t0 = tk.Frame(self.t_notebook_4)
        self.t_notebook_4.add(self.t_notebook_4_t0, padding=3)
        self.t_notebook_4.tab(0, text="Set zonnescherm config", compound="left", underline="-1")
        self.t_notebook_4_t0.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        # self.t_notebook_4_t1 = tk.Frame(self.t_notebook_4)
        # self.t_notebook_4.add(self.t_notebook_4_t1, padding=3)
        # self.t_notebook_4.tab(1, text="Licht", compound="left", underline="-1", )
        # self.t_notebook_4_t1.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")
        # self.t_notebook_4_t2 = tk.Frame(self.t_notebook_4)
        # self.t_notebook_4.add(self.t_notebook_4_t2, padding=3)
        # self.t_notebook_4.tab(2, text="Afstand", compound="none", underline="-1", )
        # self.t_notebook_4_t2.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        self.t_notebook_5 = ttk.Notebook(self.t_notebook_1_t0)
        self.t_notebook_5.place(relx=0.291, rely=0.26, relheight=0.721, relwidth=0.693)
        self.t_notebook_5.configure(takefocus="")
        self.t_notebook_5_t0 = tk.Frame(self.t_notebook_5)
        self.t_notebook_5.add(self.t_notebook_5_t0, padding=3)
        self.t_notebook_5.tab(0, text="Afstand", compound="left", underline="-1", )
        self.t_notebook_5_t0.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        self.t_notebook_5_t1 = tk.Frame(self.t_notebook_5)
        self.t_notebook_5.add(self.t_notebook_5_t1, padding=3)
        self.t_notebook_5.tab(1, text="Licht", compound="left", underline="-1", )
        self.t_notebook_5_t1.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        self.t_notebook_5_t2 = tk.Frame(self.t_notebook_5)
        self.t_notebook_5.add(self.t_notebook_5_t2, padding=3)
        self.t_notebook_5.tab(2, text="Temperatuur", compound="none", underline="-1", )
        self.t_notebook_5_t2.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")
        bar3 = Figure(figsize=(5, 2), dpi=75)
        self.ax3 = bar3.add_subplot(111)
        self.ax3.set_title('NIET AANGESLOTEN', color="red")
        self.data3 = (20, 35, 30, 35)

        self.Button23 = ttk.Button(self.t_notebook_1_t0, style='Red.TButton')
        self.Button23.place(relx=0.01, rely=0.863, height=54, relwidth=0.270)
        self.Button23.configure(command=close_zonnescherm,  text='''CLOSE SCHERM''')

        self.button_1 = ttk.Button(self.t_notebook_1_t0, style='Green.TButton')
        self.button_1.place(relx=0.01, rely=0.767, height=54, relwidth=0.270)
        self.button_1.configure(command=open_zonnescherm, text='''OPEN SCHERM''')

        self.button_2 = ttk.Button(self.t_notebook_4_t0, style='Green.TButton')
        self.button_2.place(relx=0.265, rely=0.029, height=24, relwidth=0.05)
        self.button_2.configure(command=self.set_temp, text='''Set''')

        self.button_3 = ttk.Button(self.t_notebook_4_t0, style='Green.TButton')
        self.button_3.place(relx=0.265, rely=0.072, height=24, relwidth=0.05)
        self.button_3.configure(command=self.set_light, text='''Set''')

        self.button_4 = ttk.Button(self.t_notebook_4_t0, style='Red.TButton')
        self.button_4.place(relx=0.324, rely=0.029, height=24, relwidth=0.05)
        self.button_4.configure(command=self.reset_temp, text='''Reset''')

        self.button_5 = ttk.Button(self.t_notebook_4_t0, style='Red.TButton')
        self.button_5.place(relx=0.324, rely=0.072, height=24, relwidth=0.05)
        self.button_5.configure(command=self.reset_light, text='''Reset''')

        self.Button6 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        self.Button6.place(relx=0.265, rely=0.116, height=24, relwidth=0.05)
        self.Button6.configure(command=self.set_min_distance, text='''Set''')

        self.Button7 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        self.Button7.place(relx=0.265, rely=0.159, height=24, relwidth=0.05)
        self.Button7.configure(command=self.set_max_distance, text='''Set''')

        self.Button8 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        self.Button8.place(relx=0.324, rely=0.116, height=24, relwidth=0.05)
        self.Button8.configure(command=self.reset_min_distance, text='''Reset''')

        self.Button9 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        self.Button9.place(relx=0.324, rely=0.159, height=24, relwidth=0.05)
        self.Button9.configure(command=self.reset_max_distance, text='''Reset''')

        # self.Button7 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        # self.Button7.place(relx=0.324, rely=0.203, height=24, width=37)
        # self.Button7.configure(command=unknown_support.Reset5Temperatuur, text='''Reset''')
        #
        # self.Button8 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        # self.Button8.place(relx=0.324, rely=0.246, height=24, width=37)
        # self.Button8.configure(command=unknown_support.Reset6Temperatuur, text='''Reset''')
        #
        # self.Button9 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        # self.Button9.place(relx=0.324, rely=0.29, height=24, width=37)
        # self.Button9.configure(command=unknown_support.Reset7Temperatuur, text='''Reset''')
        #
        # self.Button10 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        # self.Button10.place(relx=0.324, rely=0.333, height=24, width=37)
        # self.Button10.configure(command=unknown_support.Reset8Temperatuur, text='''Reset''')
        #
        # self.Button11 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        # self.Button11.place(relx=0.265, rely=0.072, height=24, width=47)
        # self.Button11.configure(command=self.Set2Temperatuur, text='''Set''')

        # self.Button14 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        # self.Button14.place(relx=0.265, rely=0.203, height=24, width=47)
        # self.Button14.configure(command=self.Set5Temperatuur, text='''Set''')
        #
        # self.Button15 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        # self.Button15.place(relx=0.265, rely=0.246, height=24, width=47)
        # self.Button15.configure(command=self.Set6Temperatuur, text='''Set''')
        #
        # self.Button16 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        # self.Button16.place(relx=0.265, rely=0.29, height=24, width=47)
        # self.Button16.configure(command=self.Set7Temperatuur, text='''Set''')
        #
        # self.Button17 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        # self.Button17.place(relx=0.265, rely=0.333, height=24, width=47)
        # self.Button17.configure(command=self.Set8Temperatuur, text='''Set''')
        #
        # self.Button18 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        # self.Button18.place(relx=0.265, rely=0.391, height=24, width=47)
        # self.Button18.configure(command=unknown_support.Set9Temperatuur, text='''Set''')
        #
        # self.Button19 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        # self.Button19.place(relx=0.265, rely=0.478, height=24, width=47)
        # self.Button19.configure(command=unknown_support.Set11Temperatuur, text='''Set''')
        #
        # self.Button20 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        # self.Button20.place(relx=0.324, rely=0.391, height=24, width=39)
        # self.Button20.configure(command=unknown_support.Reset9Temperatuur, text='''Reset''')
        #
        # self.Button21 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        # self.Button21.place(relx=0.324, rely=0.435, height=24, width=39)
        # self.Button21.configure(command=unknown_support.Reset10Temperatuur, text='''Reset''')
        #
        # self.Button22 = ttk.Button(self.t_notebook_4_t0, style='Custom.TButton')
        # self.Button22.place(relx=0.324, rely=0.478, height=24, width=39)
        # self.Button22.configure(command=unknown_support.Reset11Temperatuur, text='''Reset''')
        #
        # self.Button23 = ttk.Button(self.t_notebook_1_t0, style='Custom.TButton')
        # self.Button23.place(relx=0.01, rely=0.863, height=54, width=277)
        # self.Button23.configure(command=self.close_zonnescherm,  text='''CLOSE SCHERM''')
        #
        # self.Button24 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button24.place(relx=0.265, rely=0.029, height=24, width=47)
        # self.Button24.configure(command=self.Set1Licht, text='''Set''')
        #
        # self.Button25 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button25.place(relx=0.265, rely=0.072, height=24, width=47)
        # self.Button25.configure(command=self.Set2Licht, text='''Set''')
        #
        # self.Button26 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button26.place(relx=0.265, rely=0.116, height=24, width=47)
        # self.Button26.configure(command=self.Set3Licht, text='''Set''')
        #
        # self.Button27 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button27.place(relx=0.265, rely=0.159, height=24, width=47)
        # self.Button27.configure(command=self.Set4Licht, text='''Set''')
        #
        # self.Button28 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button28.place(relx=0.265, rely=0.203, height=24, width=47)
        # self.Button28.configure(command=self.Set5Licht, text='''Set''')
        #
        # self.Button29 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button29.place(relx=0.265, rely=0.246, height=24, width=47)
        # self.Button29.configure(command=self.Set6Licht, text='''Set''')
        #
        # self.Button30 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button30.place(relx=0.265, rely=0.29, height=24, width=47)
        # self.Button30.configure(command=self.Set7Licht, text='''Set''')
        #
        # self.Button31 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button31.place(relx=0.324, rely=0.029, height=24, width=39)
        # self.Button31.configure(command=unknown_support.Reset1Licht, text='''Reset''')
        #
        # self.Button32 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button32.place(relx=0.324, rely=0.072, height=24, width=39)
        # self.Button32.configure(command=unknown_support.Reset2Licht, text='''Reset''')
        #
        # self.Button33 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button33.place(relx=0.324, rely=0.116, height=24, width=39)
        # self.Button33.configure(command=unknown_support.Reset3Licht, text='''Reset''')
        #
        # self.Button34 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button34.place(relx=0.324, rely=0.159, height=24, width=39)
        # self.Button34.configure(command=unknown_support.Reset4Licht, text='''Reset''')
        #
        # self.Button35 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button35.place(relx=0.324, rely=0.203, height=24, width=39)
        # self.Button35.configure(command=unknown_support.Reset5Licht, text='''Reset''')
        #
        # self.Button36 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button36.place(relx=0.324, rely=0.246, height=24, width=39)
        # self.Button36.configure(command=unknown_support.Reset6Licht, text='''Reset''')
        #
        # self.Button37 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button37.place(relx=0.324, rely=0.29, height=24, width=39)
        # self.Button37.configure(command=unknown_support.Reset7Licht, text='''Reset''')
        #
        # self.Button38 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button38.place(relx=0.265, rely=0.333, height=24, width=47)
        # self.Button38.configure(command=self.Set8Licht, text='''Set''')
        #
        # self.Button39 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button39.place(relx=0.265, rely=0.391, height=24, width=47)
        # self.Button39.configure(command=unknown_support.Set9Licht, text='''Set''')
        #
        # self.Button40 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button40.place(relx=0.265, rely=0.435, height=24, width=47)
        # self.Button40.configure(command=unknown_support.Set10Licht, text='''Set''')
        #
        # self.Button41 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button41.place(relx=0.324, rely=0.333, height=24, width=39)
        # self.Button41.configure(command=unknown_support.Reset8Licht, text='''Reset''')
        #
        # self.Button42 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button42.place(relx=0.324, rely=0.391, height=24, width=39)
        # self.Button42.configure(command=unknown_support.Reset9Licht, text='''Reset''')
        #
        # self.Button43 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button43.place(relx=0.324, rely=0.435, height=24, width=39)
        # self.Button43.configure(command=unknown_support.Reset10Licht, text='''Reset''')
        #
        # self.Button44 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button44.place(relx=0.265, rely=0.029, height=24, width=47)
        # self.Button44.configure(command=self.Set1Afstand, text='''Set''')
        #
        # self.Button45 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button45.place(relx=0.265, rely=0.072, height=24, width=47)
        # self.Button45.configure(command=self.Set2Afstand, text='''Set''')
        #
        # self.Button46 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button46.place(relx=0.265, rely=0.116, height=24, width=47)
        # self.Button46.configure(command=self.Set3Afstand, text='''Set''')
        #
        # self.Button47 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button47.place(relx=0.265, rely=0.159, height=24, width=47)
        # self.Button47.configure(command=self.Set4Afstand, text='''Set''')
        #
        # self.Button48 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button48.place(relx=0.265, rely=0.203, height=24, width=47)
        # self.Button48.configure(command=self.Set5Afstand, text='''Set''')
        #
        # self.Button49 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button49.place(relx=0.265, rely=0.246, height=24, width=47)
        # self.Button49.configure(command=self.Set6Afstand, text='''Set''')
        #
        # self.Button50 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button50.place(relx=0.265, rely=0.29, height=24, width=47)
        # self.Button50.configure(command=self.Set7Afstand, text='''Set''')
        #
        # self.Button51 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button51.place(relx=0.265, rely=0.333, height=24, width=47)
        # self.Button51.configure(command=self.Set8Afstand, text='''Set''')
        #
        # self.Button52 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button52.place(relx=0.324, rely=0.029, height=24, width=39)
        # self.Button52.configure(command=unknown_support.Reset1Afstand, text='''Reset''')
        #
        # self.Button53 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button53.place(relx=0.324, rely=0.072, height=24, width=39)
        # self.Button53.configure(command=unknown_support.Reset2Afstand, text='''Reset''')
        #
        # self.Button54 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button54.place(relx=0.324, rely=0.116, height=24, width=39)
        # self.Button54.configure(command=unknown_support.Reset3Afstand, text='''Reset''')
        #
        # self.Button55 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button55.place(relx=0.324, rely=0.159, height=24, width=39)
        # self.Button55.configure(command=unknown_support.Reset4Afstand, text='''Reset''')
        #
        # self.Button56 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button56.place(relx=0.324, rely=0.203, height=24, width=39)
        # self.Button56.configure(command=unknown_support.Reset5Afstand, text='''Reset''')
        #
        # self.Button57 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button57.place(relx=0.324, rely=0.246, height=24, width=39)
        # self.Button57.configure(command=unknown_support.Reset6Afstand, text='''Reset''')
        #
        # self.Button58 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button58.place(relx=0.324, rely=0.29, height=24, width=39)
        # self.Button58.configure(command=unknown_support.Reset7Afstand, text='''Reset''')
        #
        # self.Button59 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button59.place(relx=0.324, rely=0.333, height=24, width=39)
        # self.Button59.configure(command=unknown_support.Reset8Afstand, text='''Reset''')
        #
        # self.Button60 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button60.place(relx=0.265, rely=0.391, height=24, width=47)
        # self.Button60.configure(command=unknown_support.Set9Afstand, text='''Set''')
        #
        # self.Button61 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button61.place(relx=0.265, rely=0.435, height=24, width=47)
        # self.Button61.configure(command=unknown_support.Set10Afstand, text='''Set''')
        #
        # self.Button62 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button62.place(relx=0.265, rely=0.478, height=24, width=47)
        # self.Button62.configure(command=unknown_support.Set11Afstand, text='''Set''')
        #
        # self.Button63 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button63.place(relx=0.324, rely=0.391, height=24, width=39)
        # self.Button63.configure(command=unknown_support.Reset9Afstand, text='''Reset''')
        #
        # self.Button64 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button64.place(relx=0.324, rely=0.435, height=24, width=39)
        # self.Button64.configure(command=unknown_support.Reset10Afstand, text='''Reset''')
        #
        # self.Button65 = ttk.Button(self.t_notebook_4_t2, style='Custom.TButton')
        # self.Button65.place(relx=0.324, rely=0.478, height=24, width=39)
        # self.Button65.configure(command=unknown_support.Reset11Afstand, text='''Reset''')
        #
        # self.Button66 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button66.place(relx=0.265, rely=0.478, height=24, width=47)
        # self.Button66.configure(command=unknown_support.Set11Licht, text='''Set''')
        #
        # self.Button67 = ttk.Button(self.t_notebook_4_t1, style='Custom.TButton')
        # self.Button67.place(relx=0.324, rely=0.478, height=24, width=39)
        # self.Button67.configure(command=unknown_support.Reset11Licht, text='''Reset''')

        self.button_68 = ttk.Button(self.t_notebook_1_t0, style='Custom.TButton')
        self.button_68.place(relx=0.01, rely=0.521, height=74, relwidth=0.080)
        self.button_68.configure(command=self.switch_to_arduino, text='''Arduino 1''')

        self.button_69 = ttk.Button(self.t_notebook_1_t0, style='Custom.TButton')
        self.button_69.place(relx=0.105, rely=0.521, height=74, relwidth=0.080)
        self.button_69.configure(command=self.switch_to_arduino_2, text='''Arduino 2''')

        self.button_70 = ttk.Button(self.t_notebook_1_t0, style='Custom.TButton')
        self.button_70.place(relx=0.200, rely=0.521, height=74, relwidth=0.080)
        self.button_70.configure(command=self.switch_to_arduino_3, text='''Arduino 3''')

        self.button_71 = ttk.Button(self.t_notebook_1_t0, style='Custom.TButton')
        self.button_71.place(relx=0.05, rely=0.644, height=74, relwidth=0.080)
        self.button_71.configure(command=self.switch_to_arduino_4, text='''Arduino 4''')

        self.button_72 = ttk.Button(self.t_notebook_1_t0, style='Custom.TButton')
        self.button_72.place(relx=0.155, rely=0.644, height=74, relwidth=0.080)
        self.button_72.configure(command=self.switch_to_arduino_5, text='''Arduino 5''')

        self.checkbuttonstyle = ttk.Style()
        self.checkbuttonstyle.configure('Custom.TCheckbutton', activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                        disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                        highlightcolor="black", justify='left')

        self.Checkbutton1 = ttk.Checkbutton(self.t_notebook_4_t0, style='Custom.TCheckbutton')
        self.Checkbutton1.place(relx=0.101, rely=0.203, relheight=0.036, relwidth=39)
        self.Checkbutton1.configure(variable=self.run_config, onvalue=True, offvalue=False,
                                    text='''Use the above config''')

        # self.Checkbutton2 = ttk.Checkbutton(self.t_notebook_4_t0, style='Custom.TCheckbutton')
        # self.Checkbutton2.place(relx=0.088, rely=0.435, relheight=0.036
        #                         , relwidth=0.06)
        # self.Checkbutton2.configure(variable=unknown_support.che94, text='''Check''')
        #
        # self.Checkbutton3 = ttk.Checkbutton(self.t_notebook_4_t0, style='Custom.TCheckbutton')
        # self.Checkbutton3.place(relx=0.088, rely=0.478, relheight=0.036
        #                         , relwidth=0.06)
        # self.Checkbutton3.configure(variable=unknown_support.che95, text='''Check''')
        #
        # self.Checkbutton4 = ttk.Checkbutton(self.t_notebook_4_t0, style='Custom.TCheckbutton')
        # self.Checkbutton4.place(relx=0.157, rely=0.391, relheight=0.036
        #                         , relwidth=0.06)
        # self.Checkbutton4.configure(variable=unknown_support.che96, text='''Check''')
        #
        # self.Checkbutton5 = ttk.Checkbutton(self.t_notebook_4_t0, style='Custom.TCheckbutton')
        # self.Checkbutton5.place(relx=0.157, rely=0.435, relheight=0.036
        #                         , relwidth=0.06)
        # self.Checkbutton5.configure(variable=unknown_support.che97, text='''Check''')
        #
        # self.Checkbutton6 = ttk.Checkbutton(self.t_notebook_4_t0, style='Custom.TCheckbutton')
        # self.Checkbutton6.place(relx=0.157, rely=0.478, relheight=0.036
        #                         , relwidth=0.06)
        # self.Checkbutton6.configure(variable=unknown_support.che99, text='''Check''')
        #
        # # self.Checkbutton7 = ttk.Checkbutton(self.t_notebook_4_t1, style='Custom.TCheckbutton')
        # self.Checkbutton7.place(relx=0.088, rely=0.391, relheight=0.036
        #                         , relwidth=0.06)
        # self.Checkbutton7.configure(variable=unknown_support.che72, text='''Check''')
        #
        # self.Checkbutton8 = ttk.Checkbutton(self.t_notebook_4_t1, style='Custom.TCheckbutton')
        # self.Checkbutton8.place(relx=0.088, rely=0.435, relheight=0.036
        #                         , relwidth=0.06)
        # self.Checkbutton8.configure(variable=unknown_support.che73, text='''Check''')
        #
        # self.Checkbutton9 = ttk.Checkbutton(self.t_notebook_4_t1, style='Custom.TCheckbutton')
        # self.Checkbutton9.place(relx=0.088, rely=0.478, relheight=0.036
        #                         , relwidth=0.06)
        # self.Checkbutton9.configure(variable=unknown_support.che74, text='''Check''')
        #
        # self.Checkbutton10 = ttk.Checkbutton(self.t_notebook_4_t1, style='Custom.TCheckbutton')
        # self.Checkbutton10.place(relx=0.157, rely=0.391, relheight=0.036
        #                          , relwidth=0.06)
        # self.Checkbutton10.configure(variable=unknown_support.che75, text='''Check''')
        #
        # self.Checkbutton11 = ttk.Checkbutton(self.t_notebook_4_t1, style='Custom.TCheckbutton')
        # self.Checkbutton11.place(relx=0.157, rely=0.435, relheight=0.036
        #                          , relwidth=0.06)
        # self.Checkbutton11.configure(variable=unknown_support.che76, text='''Check''')
        #
        # self.Checkbutton12 = ttk.Checkbutton(self.t_notebook_4_t1, style='Custom.TCheckbutton')
        # self.Checkbutton12.place(relx=0.157, rely=0.478, relheight=0.036
        #                          , relwidth=0.06)
        # self.Checkbutton12.configure(variable=unknown_support.che77, text='''Check''')
        #
        # self.Checkbutton13 = ttk.Checkbutton(self.t_notebook_4_t2, style='Custom.TCheckbutton')
        # self.Checkbutton13.place(relx=0.088, rely=0.391, relheight=0.036
        #                          , relwidth=0.06)
        # self.Checkbutton13.configure(variable=unknown_support.che120, text='''Check''')
        #
        # self.Checkbutton14 = ttk.Checkbutton(self.t_notebook_4_t2, style='Custom.TCheckbutton')
        # self.Checkbutton14.place(relx=0.088, rely=0.435, relheight=0.036
        #                          , relwidth=0.06)
        # self.Checkbutton14.configure(variable=unknown_support.che121, text='''Check''')
        #
        # self.Checkbutton15 = ttk.Checkbutton(self.t_notebook_4_t2, style='Custom.TCheckbutton')
        # self.Checkbutton15.place(relx=0.088, rely=0.478, relheight=0.036
        #                          , relwidth=0.06)
        # self.Checkbutton15.configure(variable=unknown_support.che122, text='''Check''')
        #
        # self.Checkbutton16 = ttk.Checkbutton(self.t_notebook_4_t2, style='Custom.TCheckbutton')
        # self.Checkbutton16.place(relx=0.157, rely=0.391, relheight=0.036
        #                          , relwidth=0.06)
        # self.Checkbutton16.configure(variable=unknown_support.che123, text='''Check''')
        #
        # self.Checkbutton17 = ttk.Checkbutton(self.t_notebook_4_t2, style='Custom.TCheckbutton')
        # self.Checkbutton17.place(relx=0.157, rely=0.435, relheight=0.036
        #                          , relwidth=0.06)
        # self.Checkbutton17.configure(variable=unknown_support.che124, text='''Check''')
        #
        # self.Checkbutton18 = ttk.Checkbutton(self.t_notebook_4_t2, style='Custom.TCheckbutton')
        # self.Checkbutton18.place(relx=0.157, rely=0.478, relheight=0.036
        #                          , relwidth=0.06)
        # self.Checkbutton18.configure(variable=unknown_support.che125, text='''Check''')

        self.listbox_1 = tk.Listbox(self.t_notebook_1_t0)
        self.listbox_1.place(relx=0.01, rely=0.014, relheight=0.236, relwidth=0.272)
        self.listbox_1.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                 foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                 selectbackground="#c4c4c4", selectforeground="black")

        self.listbox_2 = tk.Listbox(self.t_notebook_1_t0)
        self.listbox_2.place(relx=0.01, rely=0.26, relheight=0.236, relwidth=0.272)
        self.listbox_2.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                 foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                 selectbackground="#c4c4c4", selectforeground="black")

        self.canvasbar1 = FigureCanvasTkAgg(bar1, master=self.t_notebook_2_t0)
        self.canvasbar1.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.canvasbar2 = FigureCanvasTkAgg(bar2, master=self.t_notebook_2_t1)
        self.canvasbar2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.canvasbar3 = FigureCanvasTkAgg(bar3, master=self.t_notebook_2_t2)
        self.canvasbar3.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.fig1 = Figure(figsize=(5, 4), dpi=100)
        self.t = np.arange(0, 3, .01)
        self.canvas1 = self.fig1.add_subplot(1, 1, 1)
        self.canvasx = []
        self.canvas1y = []
        self.newx = 0

        self.canvas1a = FigureCanvasTkAgg(self.fig1, master=self.t_notebook_5_t0)  # A tk.DrawingArea.

        self.toolbar = NavigationToolbar2Tk(self.canvas1a, self.t_notebook_5_t0)
        self.toolbar.update()
        self.canvas1a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        fig2 = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        self.canvas2 = fig2.add_subplot(1, 1, 1)
        self.canvas2y = []
        self.canvas2x = []
        self.new2x = 0

        self.canvas2a = FigureCanvasTkAgg(fig2, master=self.t_notebook_5_t1)  # A tk.DrawingArea.

        toolbar = NavigationToolbar2Tk(self.canvas2a, self.t_notebook_5_t1)
        toolbar.update()
        self.canvas2a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        fig3 = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        self.canvas3 = fig3.add_subplot(1, 1, 1)
        self.canvas3y = []
        self.canvas3x = []
        self.new3x = 0

        self.canvas3a = FigureCanvasTkAgg(fig3, master=self.t_notebook_5_t2)  # A tk.DrawingArea.

        toolbar = NavigationToolbar2Tk(self.canvas3a, self.t_notebook_5_t2)
        toolbar.update()
        self.canvas3a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        fig4 = Figure(figsize=(5, 8), dpi=100)
        t = np.arange(0, 3, .01)
        self.canvas4 = fig4.add_subplot(1, 3, 1)
        self.canvas5 = fig4.add_subplot(1, 3, 2)
        self.canvas12 = fig4.add_subplot(1, 3, 3)
        self.canvas4y = []
        self.canvas5y = []
        self.canvas4x = []
        self.canvas5x = []
        self.canvas12y = []
        self.canvas12x = []
        self.new4x = 0
        self.new5x = 0
        self.new12x = 0

        self.canvas4a = FigureCanvasTkAgg(fig4, master=self.t_notebook_3_t0)  # A tk.DrawingArea.

        toolbar = NavigationToolbar2Tk(self.canvas4a, self.t_notebook_3_t0)
        toolbar.update()
        self.canvas4a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        fig5 = Figure(figsize=(5, 8), dpi=100)
        t = np.arange(0, 3, .01)
        self.canvas6 = fig5.add_subplot(1, 3, 1)
        self.canvas7 = fig5.add_subplot(1, 3, 2)
        self.canvas13 = fig5.add_subplot(1, 3, 3)
        self.canvas6y = []
        self.canvas7y = []
        self.canvas6x = []
        self.canvas7x = []
        self.canvas13x = []
        self.canvas13y = []
        self.new6x = 0
        self.new7x = 0
        self.new13x = 0

        self.canvas5a = FigureCanvasTkAgg(fig5, master=self.t_notebook_3_t1)  # A tk.DrawingArea.

        toolbar = NavigationToolbar2Tk(self.canvas5a, self.t_notebook_3_t1)
        toolbar.update()
        self.canvas5a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        fig6 = Figure(figsize=(5, 8), dpi=100)
        t = np.arange(0, 3, .01)
        self.canvas8 = fig6.add_subplot(1, 3, 1)
        self.canvas9 = fig6.add_subplot(1, 3, 2)
        self.canvas14 = fig6.add_subplot(1, 3, 3)
        self.canvas8y = []
        self.canvas9y = []
        self.canvas8x = []
        self.canvas9x = []
        self.canvas14x = []
        self.canvas14y = []
        self.new8x = 0
        self.new9x = 0
        self.new14x = 0

        self.canvas6a = FigureCanvasTkAgg(fig6, master=self.t_notebook_3_t2)  # A tk.DrawingArea.

        toolbar = NavigationToolbar2Tk(self.canvas6a, self.t_notebook_3_t2)
        toolbar.update()
        self.canvas6a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        fig7 = Figure(figsize=(5, 8), dpi=100)
        t = np.arange(0, 3, .01)
        self.canvas10 = fig7.add_subplot(1, 3, 1)
        self.canvas11 = fig7.add_subplot(1, 3, 2)
        self.canvas15 = fig7.add_subplot(1, 3, 3)
        self.canvas10y = []
        self.canvas11y = []
        self.canvas10x = []
        self.canvas11x = []
        self.canvas15x = []
        self.canvas15y = []
        self.new10x = 0
        self.new11x = 0
        self.new15x = 0

        self.canvas7a = FigureCanvasTkAgg(fig7, master=self.t_notebook_3_t3)  # A tk.DrawingArea.

        toolbar = NavigationToolbar2Tk(self.canvas7a, self.t_notebook_3_t3)
        toolbar.update()
        self.canvas7a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        fig8 = Figure(figsize=(5, 8), dpi=100)
        t = np.arange(0, 3, .01)
        self.canvas16 = fig8.add_subplot(1, 3, 1)
        self.canvas17 = fig8.add_subplot(1, 3, 2)
        self.canvas18 = fig8.add_subplot(1, 3, 3)
        self.canvas16y = []
        self.canvas17y = []
        self.canvas16x = []
        self.canvas17x = []
        self.canvas18x = []
        self.canvas18y = []
        self.new16x = 0
        self.new17x = 0
        self.new18x = 0

        self.canvas8a = FigureCanvasTkAgg(fig8, master=self.t_notebook_3_t4)  # A tk.DrawingArea.

        toolbar = NavigationToolbar2Tk(self.canvas8a, self.t_notebook_3_t4)
        toolbar.update()
        self.canvas8a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.entry_style = ttk.Style()
        self.entry_style.configure('Custom.TEntry', background="white", disabledforeground="#a3a3a3",
                                   font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                                   highlightcolor="black", insertbackground="black", selectbackground="#c4c4c4",
                                   selectforeground="black")

        self.entry_1 = ttk.Entry(self.t_notebook_4_t0, style='Custom.TEntry')
        self.entry_1.place(relx=0.101, rely=0.029, height=20, relwidth=0.161)

        self.entry_2 = ttk.Entry(self.t_notebook_4_t0, style='Custom.TEntry')
        self.entry_2.place(relx=0.101, rely=0.072, height=20, relwidth=0.161)

        self.entry_3 = ttk.Entry(self.t_notebook_4_t0, style='Custom.TEntry')
        self.entry_3.place(relx=0.101, rely=0.116, height=20, relwidth=0.161)

        self.entry_4 = ttk.Entry(self.t_notebook_4_t0, style='Custom.TEntry')
        self.entry_4.place(relx=0.101, rely=0.159, height=20, relwidth=0.161)

        # self.Entry5 = ttk.Entry(self.t_notebook_4_t0, style='Custom.TEntry')
        # self.Entry5.place(relx=0.088, rely=0.203, height=20, relwidth=0.161)
        #
        # self.Entry6 = ttk.Entry(self.t_notebook_4_t0, style='Custom.TEntry')
        # self.Entry6.place(relx=0.088, rely=0.246, height=20, relwidth=0.161)
        #
        # self.Entry7 = ttk.Entry(self.t_notebook_4_t0, style='Custom.TEntry')
        # self.Entry7.place(relx=0.088, rely=0.29, height=20, relwidth=0.161)
        #
        # self.Entry8 = ttk.Entry(self.t_notebook_4_t0, style='Custom.TEntry')
        # self.Entry8.place(relx=0.088, rely=0.333, height=20, relwidth=0.161)
        #
        # self.Entry9 = ttk.Entry(self.t_notebook_4_t1, style='Custom.TEntry')
        # self.Entry9.place(relx=0.088, rely=0.029, height=20, relwidth=0.161)
        #
        # self.Entry10 = ttk.Entry(self.t_notebook_4_t1, style='Custom.TEntry')
        # self.Entry10.place(relx=0.088, rely=0.072, height=20, relwidth=0.161)
        #
        # self.Entry11 = ttk.Entry(self.t_notebook_4_t1, style='Custom.TEntry')
        # self.Entry11.place(relx=0.088, rely=0.116, height=20, relwidth=0.161)
        #
        # self.Entry12 = ttk.Entry(self.t_notebook_4_t1, style='Custom.TEntry')
        # self.Entry12.place(relx=0.088, rely=0.159, height=20, relwidth=0.161)
        #
        # self.Entry13 = ttk.Entry(self.t_notebook_4_t1, style='Custom.TEntry')
        # self.Entry13.place(relx=0.088, rely=0.203, height=20, relwidth=0.161)
        #
        # self.Entry14 = ttk.Entry(self.t_notebook_4_t1, style='Custom.TEntry')
        # self.Entry14.place(relx=0.088, rely=0.246, height=20, relwidth=0.161)
        #
        # self.Entry15 = ttk.Entry(self.t_notebook_4_t1, style='Custom.TEntry')
        # self.Entry15.place(relx=0.088, rely=0.29, height=20, relwidth=0.161)
        #
        # self.Entry16 = ttk.Entry(self.t_notebook_4_t2, style='Custom.TEntry')
        # self.Entry16.place(relx=0.088, rely=0.029, height=20, relwidth=0.161)
        #
        # self.Entry17 = ttk.Entry(self.t_notebook_4_t2, style='Custom.TEntry')
        # self.Entry17.place(relx=0.088, rely=0.072, height=20, relwidth=0.161)
        #
        # self.Entry18 = ttk.Entry(self.t_notebook_4_t2, style='Custom.TEntry')
        # self.Entry18.place(relx=0.088, rely=0.116, height=20, relwidth=0.161)
        #
        # self.Entry19 = ttk.Entry(self.t_notebook_4_t2, style='Custom.TEntry')
        # self.Entry19.place(relx=0.088, rely=0.159, height=20, relwidth=0.161)
        #
        # self.Entry20 = ttk.Entry(self.t_notebook_4_t2, style='Custom.TEntry')
        # self.Entry20.place(relx=0.088, rely=0.203, height=20, relwidth=0.161)
        #
        # self.Entry21 = ttk.Entry(self.t_notebook_4_t2, style='Custom.TEntry')
        # self.Entry21.place(relx=0.088, rely=0.246, height=20, relwidth=0.161)
        #
        # self.Entry22 = ttk.Entry(self.t_notebook_4_t2, style='Custom.TEntry')
        # self.Entry22.place(relx=0.088, rely=0.29, height=20, relwidth=0.161)
        #
        # self.Entry23 = ttk.Entry(self.t_notebook_4_t2, style='Custom.TEntry')
        # self.Entry23.place(relx=0.088, rely=0.333, height=20, relwidth=0.161)
        #
        # self.Entry24 = ttk.Entry(self.t_notebook_4_t1, style='Custom.TEntry')
        # self.Entry24.place(relx=0.088, rely=0.333, height=20, relwidth=0.161)

        self.label_style = ttk.Style()
        self.label_style.configure('Custom.TLabel', activebackground="#f9f9f9", activeforeground="black",
                                   background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                                   highlightbackground="#d9d9d9", highlightcolor="black")

        self.label_1 = ttk.Label(self.t_notebook_1_t3, style='Custom.TLabel')
        self.label_1.place(relx=0.01, rely=0.014, height=674, width=674)
        self.label_1.configure(text='''INSTRUCTIONS:
        
        DASHBOARD:
        The dashboard shows an overview of the application, including graphs showing the current distance (between the
        sun blind and it's lowest point, as a check whether or not the sun blind is functioning correctly), temperature 
        (in °C), and light level (in Lux), as well as controls for the sunblind, bar graphs showing average values, and
        controls to determine which Arduino is shown in the graphs.
        
        GRAPH:
        The graph tab shows all data from all arduino's in seperate graphs. Use the tabs to switch between which Arduino
        to display.
    
        CONFIG:
        The config window allows you to configure at what settings you want the sun screen to automatically open/close.
        
        The Temprature field allows a user to set a minimum temperature (in °C) through the set button. 
        If the temperature falls below this value the screen will automatically close, if the temperature exceeds the
        set minimum the screen will automatically open.
        
        The Light field allows a user to set a minimum light value (in Lux) through the set button.
        If the light value falls below this value the screen will automaticall close, if the light value exceeds the
        set minimum the screen will automatically open.
        
        The reset buttons will set the minimum temprature/light value (depending on the reset button used) back to their
        default value.
        
        The "Use the above config" checkbox determines whether or not the screen will atuomatically open/close if
        minimum values are reached/exceeded.
        
        HELP:
        This current window
        
        Free Hong Kong!
        A revolution in our generation!''')

        self.label_2 = ttk.Label(self.t_notebook_4_t0, style='Custom.TLabel')
        self.label_2.place(relx=0.0, rely=0.029, height=21, relwidth=0.1)
        self.label_2.configure(text='''Set temperatuur''')

        self.label_2 = ttk.Label(self.t_notebook_4_t0, style='Custom.TLabel')
        self.label_2.place(relx=0.0, rely=0.072, height=21, relwidth=0.1)
        self.label_2.configure(text='''Set light''')

        self.Label2 = ttk.Label(self.t_notebook_4_t0, style='Custom.TLabel')
        self.Label2.place(relx=0.0, rely=0.116, height=21, relwidth=0.1)
        self.Label2.configure(text='''Set minimal distance''')

        self.Label2 = ttk.Label(self.t_notebook_4_t0, style='Custom.TLabel')
        self.Label2.place(relx=0.0, rely=0.159, height=21, relwidth=0.1)
        self.Label2.configure(text='''Set maximum distance''')

        # self.Label2 = ttk.Label(self.t_notebook_4_t0, style='Custom.TLabel')
        # self.Label2.place(relx=0.0, rely=0.203, height=21, width=74)
        # self.Label2.configure(text='''Setting''')
        #
        # self.Label2 = ttk.Label(self.t_notebook_4_t0, style='Custom.TLabel')
        # self.Label2.place(relx=0.0, rely=0.246, height=21, width=74)
        # self.Label2.configure(text='''Setting''')
        #
        # self.Label2 = ttk.Label(self.t_notebook_4_t0, style='Custom.TLabel')
        # self.Label2.place(relx=0.0, rely=0.29, height=21, width=74)
        # self.Label2.configure(text='''Setting''')
        #
        # self.Label2 = ttk.Label(self.t_notebook_4_t0, style='Custom.TLabel')
        # self.Label2.place(relx=0.0, rely=0.333, height=21, width=74)
        # self.Label2.configure(text='''Setting''')
        #TODO waarom plaats je Label2 8 keer met identieke code?

        # self.Label3 = ttk.Label(self.t_notebook_4_t1, style='Custom.TLabel')
        # self.Label3.place(relx=0.02, rely=0.029, height=21, width=43)
        # self.Label3.configure(text='''Setting''')
        #
        # self.Label4 = ttk.Label(self.t_notebook_4_t1, style='Custom.TLabel')
        # self.Label4.place(relx=0.02, rely=0.072, height=21, width=43)
        # self.Label4.configure(text='''Setting''')
        #
        # self.Label5 = ttk.Label(self.t_notebook_4_t1, style='Custom.TLabel')
        # self.Label5.place(relx=0.02, rely=0.116, height=21, width=43)
        # self.Label5.configure(text='''Setting''')
        #
        # self.Label6 = ttk.Label(self.t_notebook_4_t1, style='Custom.TLabel')
        # self.Label6.place(relx=0.02, rely=0.159, height=21, width=43)
        # self.Label6.configure(text='''Setting''')
        #
        # self.Label7 = ttk.Label(self.t_notebook_4_t1, style='Custom.TLabel')
        # self.Label7.place(relx=0.02, rely=0.203, height=21, width=43)
        # self.Label7.configure(text='''Setting''')
        #
        # self.Label8 = ttk.Label(self.t_notebook_4_t1, style='Custom.TLabel')
        # self.Label8.place(relx=0.02, rely=0.246, height=21, width=43)
        # self.Label8.configure(text='''Setting''')
        #
        # self.Label9 = ttk.Label(self.t_notebook_4_t1, style='Custom.TLabel')
        # self.Label9.place(relx=0.02, rely=0.29, height=21, width=43)
        # self.Label9.configure(text='''Setting''')
        #
        # self.Label10 = ttk.Label(self.t_notebook_4_t2, style='Custom.TLabel')
        # self.Label10.place(relx=0.02, rely=0.029, height=21, width=43)
        # self.Label10.configure(text='''Setting''')
        #
        # self.Label11 = ttk.Label(self.t_notebook_4_t2, style='Custom.TLabel')
        # self.Label11.place(relx=0.02, rely=0.072, height=21, width=44)
        # self.Label11.configure(text='''Setting''')
        #
        # self.Label12 = ttk.Label(self.t_notebook_4_t2, style='Custom.TLabel')
        # self.Label12.place(relx=0.02, rely=0.116, height=21, width=43)
        # self.Label12.configure(text='''Setting''')
        #
        # self.Label13 = ttk.Label(self.t_notebook_4_t2, style='Custom.TLabel')
        # self.Label13.place(relx=0.02, rely=0.159, height=21, width=43)
        # self.Label13.configure(text='''Setting''')
        #
        # self.Label14 = ttk.Label(self.t_notebook_4_t2, style='Custom.TLabel')
        # self.Label14.place(relx=0.02, rely=0.203, height=21, width=43)
        # self.Label14.configure(text='''Setting''')
        #
        # self.Label15 = ttk.Label(self.t_notebook_4_t2, style='Custom.TLabel')
        # self.Label15.place(relx=0.02, rely=0.246, height=21, width=43)
        # self.Label15.configure(text='''Setting''')
        #
        # self.Label16 = ttk.Label(self.t_notebook_4_t2, style='Custom.TLabel')
        # self.Label16.place(relx=0.02, rely=0.29, height=21, width=43)
        # self.Label16.configure(text='''Setting''')
        #
        # self.Label17 = ttk.Label(self.t_notebook_4_t2, style='Custom.TLabel')
        # self.Label17.place(relx=0.02, rely=0.333, height=21, width=43)
        # self.Label17.configure(text='''Setting''')
        #
        # self.Label18 = ttk.Label(self.t_notebook_4_t1, style='Custom.TLabel')
        # self.Label18.place(relx=0.02, rely=0.333, height=21, width=43)
        # self.Label18.configure(text='''Setting''')

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)
        self.s = 1
        self.x2 = 50
        self.y2 = 0
        self.running = True
        self.counter = 0
        self.dubbel_counter = 0
        self.huidige_grafiek = 0
        self.loop()
        self.fix_grafieken()

    def loop(self):
        global counter, getallen, aantal_huidig, arduinos
        self.open_or_close(temp_gemiddelde, light_gemiddelde, distance_gemiddelde)
        self.fix_grafieken()
        root.after(1000, self.loop)

    # def fill_listbox_1(self, string_list, index):

    def fix_grafieken(self):
        gemiddelde = 0
        aantal = 0
        aantal_live = len(arduinos)
        self.listbox_1.delete(0, END)
        self.listbox_2.delete(0, END)
        status = get_zonnescherm()
        if status == 0:
            self.fill_listbox_2(str("Zonnescherm is dicht "), 1)
        else:
            self.fill_listbox_2(str("Zonnescherm is open "), 1)
        for i in range(4):
            if i+1 <= aantal_live:
                self.fill_listbox_1(str("Arduino ") + str(i+1) + str(" is live"), i+1)
            else:
                self.fill_listbox_1(str("Arduino ") + str(i+1) + str(" is niet live"), i+1)
        self.animatecanvas1(distance_gemiddelde[self.huidige_grafiek])
        self.animatecanvas3(temp_gemiddelde[self.huidige_grafiek])
        self.animatecanvas2(light_gemiddelde[self.huidige_grafiek])

        self.animatecanvas4(distance_gemiddelde[0])
        self.animatecanvas5(light_gemiddelde[0])
        self.animatecanvas12(temp_gemiddelde[0])
        self.animatecanvas6(distance_gemiddelde[1])
        self.animatecanvas7(light_gemiddelde[1])
        self.animatecanvas13(temp_gemiddelde[1])
        self.animatecanvas8(distance_gemiddelde[2])
        self.animatecanvas9(light_gemiddelde[2])
        self.animatecanvas14(temp_gemiddelde[2])
        self.animatecanvas10(distance_gemiddelde[3])
        self.animatecanvas11(light_gemiddelde[3])
        self.animatecanvas15(temp_gemiddelde[3])
        self.animatecanvas16(distance_gemiddelde[4])
        self.animatecanvas17(light_gemiddelde[4])
        self.animatecanvas18(temp_gemiddelde[4])

        self.set_bar1_data(distance_gemiddelde[0], distance_gemiddelde[1], distance_gemiddelde[2],
                           distance_gemiddelde[3], distance_gemiddelde[4])
        self.set_bar2_data(light_gemiddelde[0], light_gemiddelde[1], light_gemiddelde[2], light_gemiddelde[3], light_gemiddelde[4])
        self.set_bar3_data(temp_gemiddelde[0], temp_gemiddelde[1], temp_gemiddelde[2], temp_gemiddelde[3], temp_gemiddelde[4])

    def open_or_close(self, gemiddelde_temp, gemiddelde_light, gemiddelde_afstand):
        aantal_light = 0
        aantal_temp = 0
        aantal_afstand = 0
        light = 0
        temp = 0
        afstand = 0
        for i in gemiddelde_temp:
            if i != 0:
                aantal_temp += 1
                temp += i

        for i in gemiddelde_light:
            if i != 0:
                aantal_light += 1
                light += i

        for i in gemiddelde_afstand:
            if i != 0:
                aantal_afstand += 1
                afstand += i

        if aantal_light == 0:
            aantal_light = 1
        if aantal_afstand == 0:
            aantal_afstand = 1
        if aantal_temp == 0:
            aantal_temp = 1
        light = int(light/aantal_light)
        temp = int(temp/aantal_temp)
        if self.run_config:
            if light > self.maxlight:
                print("licht")
                open_zonnescherm()

            if temp > self.maxtemp:
                print("temp")
                open_zonnescherm()

            if light < self.maxlight and temp < self.maxtemp:
                close_zonnescherm()

    def animatecanvas1(self, y):
        self.canvasx.append(self.newx)
        if len(self.canvasx) > 20:
            del self.canvasx[0]
            del self.canvas1y[0]
            self.canvas1.clear()
        self.canvas1y.append(y)
        self.newx += 1
        self.canvas1.set_ylim(0, 300)  # change this if the max limit has to change
        self.canvas1.set_title('Gemiddelde Afstand')
        self.canvas1.set_ylabel('Afstand (cm)')
        self.canvas1.set_xlabel('Tijd')
        self.canvas1.plot(self.canvasx, self.canvas1y, color="blue")
        self.canvas1a.draw()

    def animatecanvas2(self, y):
        self.canvas2x.append(self.new2x)
        if len(self.canvas2x) > 20:
            del self.canvas2x[0]
            del self.canvas2y[0]
            self.canvas2.clear()
        self.canvas2y.append(y)
        self.new2x += 1
        self.canvas2.set_ylim(0, 120)  # change this if the max limit has to change
        self.canvas2.set_title('Gemiddelde Lichtintensiteit')
        self.canvas2.set_ylabel('Licht (lux)')
        self.canvas2.set_xlabel('Tijd')
        self.canvas2.plot(self.canvas2x, self.canvas2y, color="yellow")
        self.canvas2a.draw()

    def animatecanvas3(self, y):
        self.canvas3x.append(self.new3x)
        if len(self.canvas3x) > 20:
            del self.canvas3x[0]
            del self.canvas3y[0]
            self.canvas3.clear()
        self.canvas3y.append(y)
        self.new3x += 1
        self.canvas3.set_ylim(0, 80)  # change this if the max limit has to change
        self.canvas3.set_title('Gemiddelde Temperatuur')
        self.canvas3.set_ylabel('Temperatuur (°C)')
        self.canvas3.set_xlabel('Tijd')
        self.canvas3.plot(self.canvas3x, self.canvas3y, color="red")
        self.canvas3a.draw()

    def animatecanvas4(self, y):
        self.canvas4x.append(self.new4x)
        if len(self.canvas4x) > 20:
            del self.canvas4x[0]
            del self.canvas4y[0]
            self.canvas4.clear()
        self.canvas4y.append(y)
        self.new4x += 1
        self.canvas4.set_ylim(0, 300)  # change this if the max limit has to change
        self.canvas4.set_title('Gemiddelde Afstand')
        self.canvas4.set_ylabel('Afstand (cm)')
        self.canvas4.set_xlabel('Tijd')
        self.canvas4.plot(self.canvas4x, self.canvas4y, color="blue")
        self.canvas4a.draw()

    def animatecanvas5(self, y):
        self.canvas5x.append(self.new5x)
        if len(self.canvas5x) > 20:
            del self.canvas5x[0]
            del self.canvas5y[0]
            self.canvas5.clear()
        self.canvas5y.append(y)
        self.new5x += 1
        self.canvas5.set_ylim(0, 80)  # change this if the max limit has to change
        self.canvas5.set_title('Gemiddelde Temperatuur')
        self.canvas5.set_ylabel('Temperatuur (°C)')
        self.canvas5.set_xlabel('Tijd')
        self.canvas5.plot(self.canvas5x, self.canvas5y, color="red")
        self.canvas4a.draw()

    def animatecanvas6(self, y):
        self.canvas6x.append(self.new6x)
        if len(self.canvas6x) > 20:
            del self.canvas6x[0]
            del self.canvas6y[0]
            self.canvas6.clear()
        self.canvas6y.append(y)
        self.new6x += 1
        self.canvas6.set_ylim(0, 300)  # change this if the max limit has to change
        self.canvas6.set_title('Gemiddelde Afstand')
        self.canvas6.set_ylabel('Afstand (cm)')
        self.canvas6.set_xlabel('Tijd')
        self.canvas6.plot(self.canvas6x, self.canvas6y, color="blue")
        self.canvas5a.draw()

    def animatecanvas7(self, y):
        self.canvas7x.append(self.new7x)
        if len(self.canvas7x) > 20:
            del self.canvas7x[0]
            del self.canvas7y[0]
            self.canvas7.clear()
        self.canvas7y.append(y)
        self.new7x += 1
        self.canvas7.set_ylim(0, 80)  # change this if the max limit has to change
        self.canvas7.set_title('Gemiddelde Temperatuur')
        self.canvas7.set_ylabel('Temperatuur (°C)')
        self.canvas7.set_xlabel('Tijd')
        self.canvas7.plot(self.canvas7x, self.canvas7y, color="red")
        self.canvas5a.draw()

    def animatecanvas8(self, y):
        self.canvas8x.append(self.new8x)
        if len(self.canvas8x) > 20:
            del self.canvas8x[0]
            del self.canvas8y[0]
            self.canvas8.clear()
        self.canvas8y.append(y)
        self.new8x += 1
        self.canvas8.set_ylim(0, 300)  # change this if the max limit has to change
        self.canvas8.set_title('Gemiddelde Afstand')
        self.canvas8.set_ylabel('Afstand (cm)')
        self.canvas8.set_xlabel('Tijd')
        self.canvas8.plot(self.canvas8x, self.canvas8y, color="blue")
        self.canvas6a.draw()

    def animatecanvas9(self, y):
        self.canvas9x.append(self.new9x)
        if len(self.canvas9x) > 20:
            del self.canvas9x[0]
            del self.canvas9y[0]
            self.canvas9.clear()
        self.canvas9y.append(y)
        self.new9x += 1
        self.canvas9.set_ylim(0, 80)  # change this if the max limit has to change
        self.canvas9.set_title('Gemiddelde Temperatuur')
        self.canvas9.set_ylabel('Temperatuur (°C)')
        self.canvas9.set_xlabel('Tijd')
        self.canvas9.plot(self.canvas9x, self.canvas9y, color="red")
        self.canvas6a.draw()

    def animatecanvas10(self, y):
        self.canvas10x.append(self.new10x)
        if len(self.canvas10x) > 20:
            del self.canvas10x[0]
            del self.canvas10y[0]
            self.canvas10.clear()
        self.canvas10y.append(y)
        self.new10x += 1
        self.canvas10.set_ylim(0, 300)  # change this if the max limit has to change
        self.canvas10.set_title('Gemiddelde Afstand')
        self.canvas10.set_ylabel('Afstand (cm)')
        self.canvas10.set_xlabel('Tijd')
        self.canvas10.plot(self.canvas10x, self.canvas10y, color="blue")
        self.canvas7a.draw()

    def animatecanvas11(self, y):
        self.canvas11x.append(self.new11x)
        if len(self.canvas11x) > 20:
            del self.canvas11x[0]
            del self.canvas11y[0]
            self.canvas11.clear()
        self.canvas11y.append(y)
        self.new11x += 1
        self.canvas11.set_ylim(0, 80)  # change this if the max limit has to change
        self.canvas11.set_title('Gemiddelde Temperatuur')
        self.canvas11.set_ylabel('Temperatuur (°C)')
        self.canvas11.set_xlabel('Tijd')
        self.canvas11.plot(self.canvas11x, self.canvas11y, color="red")
        self.canvas7a.draw()

    def animatecanvas12(self, y):
        self.canvas12x.append(self.new12x)
        if len(self.canvas12x) > 20:
            del self.canvas12x[0]
            del self.canvas12y[0]
            self.canvas12.clear()
        self.canvas12y.append(y)
        self.new12x += 1
        self.canvas12.set_ylim(0, 120)  # change this if the max limit has to change
        self.canvas12.set_title('Gemiddelde Lichtintensiteit')
        self.canvas12.set_ylabel('Licht (lux)')
        self.canvas12.set_xlabel('Tijd')
        self.canvas12.plot(self.canvas12x, self.canvas12y, color="yellow")
        self.canvas4a.draw()

    def animatecanvas13(self, y):
        self.canvas13x.append(self.new13x)
        if len(self.canvas13x) > 20:
            del self.canvas13x[0]
            del self.canvas13y[0]
            self.canvas13.clear()
        self.canvas13y.append(y)
        self.new13x += 1
        self.canvas13.set_ylim(0, 120)  # change this if the max limit has to change
        self.canvas13.set_title('Gemiddelde Lichtintensiteit')
        self.canvas13.set_ylabel('Licht (lux)')
        self.canvas13.set_xlabel('Tijd')
        self.canvas13.plot(self.canvas13x, self.canvas13y, color="yellow")
        self.canvas5a.draw()

    def animatecanvas14(self, y):
        self.canvas14x.append(self.new14x)
        if len(self.canvas14x) > 20:
            del self.canvas14x[0]
            del self.canvas14y[0]
            self.canvas14.clear()
        self.canvas14y.append(y)
        self.new14x += 1
        self.canvas14.set_ylim(0, 120)  # change this if the max limit has to change
        self.canvas14.set_title('Gemiddelde Lichtintensiteit')
        self.canvas14.set_ylabel('Licht (lux)')
        self.canvas14.set_xlabel('Tijd')
        self.canvas14.plot(self.canvas14x, self.canvas14y, color="yellow")
        self.canvas6a.draw()

    def animatecanvas15(self, y):
        self.canvas15x.append(self.new15x)
        if len(self.canvas15x) > 20:
            del self.canvas15x[0]
            del self.canvas15y[0]
            self.canvas15.clear()
        self.canvas15y.append(y)
        self.new15x += 1
        self.canvas15.set_ylim(0, 120)  # change this if the max limit has to change
        self.canvas15.set_title('Gemiddelde Lichtintensiteit')
        self.canvas15.set_ylabel('Licht (lux)')
        self.canvas15.set_xlabel('Tijd')
        self.canvas15.plot(self.canvas15x, self.canvas15y, color="yellow")
        self.canvas7a.draw()

    def animatecanvas16(self, y):
        self.canvas16x.append(self.new16x)
        if len(self.canvas16x) > 20:
            del self.canvas16x[0]
            del self.canvas16y[0]
            self.canvas16.clear()
        self.canvas16y.append(y)
        self.new16x += 1
        self.canvas16.set_ylim(0, 300)  # change this if the max limit has to change
        self.canvas16.set_title('Gemiddelde Afstand')
        self.canvas16.set_ylabel('Afstand (cm)')
        self.canvas16.set_xlabel('Tijd')
        self.canvas16.plot(self.canvas16x, self.canvas16y, color="blue")
        self.canvas8a.draw()

    def animatecanvas17(self, y):
        self.canvas17x.append(self.new17x)
        if len(self.canvas17x) > 20:
            del self.canvas17x[0]
            del self.canvas17y[0]
            self.canvas17.clear()
        self.canvas17y.append(y)
        self.new17x += 1
        self.canvas17.set_ylim(0, 80)  # change this if the max limit has to change
        self.canvas17.set_title('Gemiddelde Temperatuur')
        self.canvas17.set_ylabel('Temperatuur (°C)')
        self.canvas17.set_xlabel('Tijd')
        self.canvas17.plot(self.canvas17x, self.canvas17y, color="red")
        self.canvas8a.draw()

    def animatecanvas18(self, y):
        self.canvas18x.append(self.new18x)
        if len(self.canvas18x) > 20:
            del self.canvas18x[0]
            del self.canvas18y[0]
            self.canvas18.clear()
        self.canvas18y.append(y)
        self.new18x += 1
        self.canvas18.set_ylim(0, 120)  # change this if the max limit has to change
        self.canvas18.set_title('Gemiddelde Lichtintensiteit')
        self.canvas18.set_ylabel('Licht (lux)')
        self.canvas18.set_xlabel('Tijd')
        self.canvas18.plot(self.canvas18x, self.canvas18y, color="yellow")
        self.canvas8a.draw()

    def set_1_temperatuur(self):
        print(self.entry_1.get())

    def set_2_temperatuur(self):
        print(self.entry_2.get())

    def set_3_temperatuur(self):
        print(self.Entry3.get())

    def set_4_temperatuur(self):
        print(self.Entry4.get())

    def set_5_temperatuur(self):
        print(self.Entry5.get())

    def set_6_temperatuur(self):
        print(self.Entry6.get())

    def set_7_temperatuur(self):
        print(self.Entry7.get())

    def set_8_temperatuur(self):
        print(self.Entry8.get())

    def set_1_licht(self):
        print(self.Entry9.get())

    def set_2_licht(self):
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

    def clear_canvasses_dashboard(self):
        self.canvas1.clear()
        self.canvas1y.clear()
        self.canvasx.clear()
        self.canvas2.clear()
        self.canvas2y.clear()
        self.canvas2x.clear()
        self.canvas3.clear()
        self.canvas3y.clear()
        self.canvas3x.clear()
        self.canvas3.clear()
        self.newx = 0
        self.new2x = 0
        self.new3x = 0

    def switch_to_arduino(self):
        length = len(arduinos)
        if length > 0:
            self.clear_canvasses_dashboard()
            self.huidige_grafiek = 0

    def switch_to_arduino_2(self):
        length = len(arduinos)
        if length > 1:
            self.clear_canvasses_dashboard()
            self.huidige_grafiek = 1

    def switch_to_arduino_3(self):
        length = len(arduinos)
        if length > 2:
            self.clear_canvasses_dashboard()
            self.huidige_grafiek = 2

    def switch_to_arduino_4(self):
        length = len(arduinos)
        if length > 3:
            self.clear_canvasses_dashboard()
            self.huidige_grafiek = 3

    def switch_to_arduino_5(self):
        length = len(arduinos)
        if length > 4:
            self.clear_canvasses_dashboard()
            self.huidige_grafiek = 4

    def set_bar1_data(self, ad1, ad2, ad3, ad4, ad5):
        self.data1 = (ad1, ad2, ad3, ad4, ad5)
        self.ax1.clear()
        self.ax1.bar(self.ind, self.data1, .5)
        self.ax1.set_xticks(self.ind)
        self.ax1.set_xticklabels(('Arduino 1', 'Arduino 2', 'Arduino 3', 'Arduino 4', 'Arduino 5'))
        self.ax1.set_title("Gemiddelde Afstand")
        self.ax1.set_ylabel("Aftand (cm)")
        self.canvasbar1.draw()

    def set_bar2_data(self, ad1, ad2, ad3, ad4, ad5):
        self.data2 = (ad1, ad2, ad3, ad4, ad5)
        self.ax2.clear()
        self.ax2.bar(self.ind, self.data2, .5, color="yellow")
        self.ax2.set_xticks(self.ind)
        self.ax2.set_xticklabels(('Arduino 1', 'Arduino 2', 'Arduino 3', 'Arduino 4', 'Arduino 5'))
        self.ax2.set_title("Gemiddelde Lichtintensiteit")
        self.ax2.set_ylabel("Lichtintensiteit (lux)")
        self.canvasbar2.draw()

    def set_bar3_data(self, ad1, ad2, ad3, ad4, ad5):
        self.data3 = (ad1, ad2, ad3, ad4, ad5)
        self.ax3.clear()
        self.ax3.bar(self.ind, self.data3, .5, color="red")
        self.ax3.set_xticks(self.ind)
        self.ax3.set_xticklabels(('Arduino 1', 'Arduino 2', 'Arduino 3', 'Arduino 4', 'Arduino 5'))
        self.ax3.set_title("Gemiddelde Temperatuur")
        self.ax3.set_ylabel("Temperatuur (°C)")
        self.canvasbar3.draw()

    def fill_listbox_1(self, string, index):
        self.listbox_1.insert(index, string)
        if len(string) == 22:
            self.listbox_1.itemconfig(index-1, {'bg':'red', 'fg':'white'})
        else:
            self.listbox_1.itemconfig(index - 1, {'bg': 'green'})

    def fill_listbox_2(self, string, index):
        self.listbox_2.insert(index, string)

    def set_run_config(self):
        self.run_config = True

    def set_temp(self):
        try:
            self.maxtemp = int(self.entry_1.get())
        except ValueError:
            print("Value of maxtemp has not changed")

    def set_light(self):
        try:
            self.maxlight = int(self.entry_2.get())
        except ValueError:
            print("Value of maxlight has not changed")

    def reset_temp(self):
        self.maxtemp = 200

    def reset_light(self):
        self.maxlight = 70

    def set_min_distance(self):
        try:
            self.mindistance = int(self.entry_3.get())
        except:
            print("Value of mindistance has not changed")

    def set_max_distance(self):
        try:
            self.maxdistance = int(self.entry_4.get())
        except:
            print("Value of maxdistance has not changed")

    def reset_min_distance(self):
        self.mindistance = 20

    def reset_max_distance(self):
        self.maxdistance = 140


if __name__ == '__main__':
    vp_start_gui()
