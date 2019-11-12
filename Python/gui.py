# LIBS USED:    matplotlib
#               numpy
#               pyserial

from tkinter import *
from receive_data import *

import _thread
import queue
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
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

    # Add task to Thread
    def write(self, line):
        self.queue.put(line)

    # Clears the Thread
    def clear(self):
        self.queue.put(None)

    # Updates the Thread
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

# Starts the GUI
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    ding = ThreadSafeConsole(root)
    top = TopLevel1(root)
    _thread.start_new(loop_loop, ())
    root.mainloop()


w = None

# Creates a TopLevel
def create_toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = TopLevel1(w)
    return w, top

# Funtion for closing the GUI
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
        self.run_config = 0
        self.mindistance = 20
        self.maxdistance = 140
        self.open_of_dicht = 0
        self.tmp_for_styles = 0
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
        self.redbuttonfull = ttk.Style()
        self.greenbuttonfull = ttk.Style()
        self.arduino1style = ttk.Style()
        self.arduino2style = ttk.Style()
        self.arduino3style = ttk.Style()
        self.arduino4style = ttk.Style()
        self.arduino5style = ttk.Style()
        self.buttonstyle.configure('Custom.TButton', padding=1, relief="flat", background="black")
        self.redbutton.configure('Red.TButton', padding=1, relief="flat", background="red", foreground="black")
        self.greenbutton.configure('Green.TButton', padding=1, relief="flat", background="green", foreground="black")
        self.redbuttonfull.configure('Redfull.TButton', bd = 4,background="red", foreground="red")
        self.greenbuttonfull.configure('Redfull.TButton', bd = 4,background="green", foreground="green")

        self.arduino1style.configure('Arduino1.TButton', padding=1, relief="flat", background="grey", foreground="grey")
        self.arduino2style.configure('Arduino2.TButton', padding=1, relief="flat", background="grey", foreground="grey")
        self.arduino3style.configure('Arduino3.TButton', padding=1, relief="flat", background="grey", foreground="grey")
        self.arduino4style.configure('Arduino4.TButton', padding=1, relief="flat", background="grey", foreground="grey")
        self.arduino5style.configure('Arduino5.TButton', padding=1, relief="flat", background="grey", foreground="grey")
        top.geometry("1400x840+478+139")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("CUCKS GUI")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        # Style for all the notebook instances
        self.style.configure('TNotebook.Tab', background=_bgcolor, foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=[('selected', _compcolor), ('active', _ana2color)])

        self.t_notebook_1 = ttk.Notebook(top)
        self.t_notebook_1.place(relx=0.0, rely=0.0, relheight=1.003, relwidth=1.002)
        self.t_notebook_1.configure(takefocus="")

        # Notebook for the Dashboard
        self.t_notebook_1_t0 = tk.Frame(self.t_notebook_1)
        self.t_notebook_1.add(self.t_notebook_1_t0, padding=3)
        self.t_notebook_1.tab(0, text="Dashboard", compound="left", underline="-1", )
        self.t_notebook_1_t0.configure(highlightbackground="#d9d9d9", background="#d9d9d9", highlightcolor="black")

        # Notebook for the Graph
        self.t_notebook_1_t1 = tk.Frame(self.t_notebook_1)
        self.t_notebook_1.add(self.t_notebook_1_t1, padding=3)
        self.t_notebook_1.tab(1, text="Graph", compound="left", underline="-1", )
        self.t_notebook_1_t1.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        # Notebook for the Config
        self.t_notebook_1_t2 = tk.Frame(self.t_notebook_1)
        self.t_notebook_1.add(self.t_notebook_1_t2, padding=3)
        self.t_notebook_1.tab(2, text="Config", compound="none", underline="-1", )
        self.t_notebook_1_t2.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        # Notebook for the Help
        self.t_notebook_1_t3 = tk.Frame(self.t_notebook_1)
        self.t_notebook_1.add(self.t_notebook_1_t3, padding=3)
        self.t_notebook_1.tab(3, text="Help", compound="none", underline="-1", )
        self.t_notebook_1_t3.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        self.t_notebook_2 = ttk.Notebook(self.t_notebook_1_t0)
        self.t_notebook_2.place(relx=0.291, rely=0.014, relheight=0.241, relwidth=0.68)
        self.t_notebook_2.configure(takefocus="")

        # Notebook for the Distance sensor in Dashboard pane
        self.t_notebook_2_t0 = tk.Frame(self.t_notebook_2)
        self.t_notebook_2.add(self.t_notebook_2_t0, padding=3)
        self.t_notebook_2.tab(0, text="Distancesensor", compound="left", underline="-1", )
        self.t_notebook_2_t0.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")
        bar1 = Figure(figsize=(5, 2), dpi=75)
        self.ax1 = bar1.add_subplot(111)

        self.data1 = (20, 45, 30, 35)
        self.ax1.set_title('NOT CONNECTED', color="red")
        self.ind = np.arange(5)  # the x locations for the groups

        # Notebook for the Light sensor in Dashboard pane
        self.t_notebook_2_t1 = tk.Frame(self.t_notebook_2)
        self.t_notebook_2.add(self.t_notebook_2_t1, padding=3)
        self.t_notebook_2.tab(1, text="Lightsensor", compound="left", underline="-1")
        self.t_notebook_2_t1.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")
        bar2 = Figure(figsize=(5, 2), dpi=75)
        self.ax2 = bar2.add_subplot(111)
        self.ax2.set_title('NOT CONNECTED', color="red")
        self.data2 = (20, 35, 30, 35)

        # Notebook for the Temperature sensor in Dashboard pane
        self.t_notebook_2_t2 = tk.Frame(self.t_notebook_2)
        self.t_notebook_2.add(self.t_notebook_2_t2, padding=3)
        self.t_notebook_2.tab(2, text="Temperature", compound="none", underline="-1")
        self.t_notebook_2_t2.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        self.t_notebook_3 = ttk.Notebook(self.t_notebook_1_t1)
        self.t_notebook_3.place(relx=0.0, rely=0.014, relheight=0.995, relwidth=1.004)
        self.t_notebook_3.configure(takefocus="")

        # Notebook for the Arduino 1 in Dashboard pane
        self.t_notebook_3_t0 = tk.Frame(self.t_notebook_3)
        self.t_notebook_3.add(self.t_notebook_3_t0, padding=3)
        self.t_notebook_3.tab(0, text="Arduino 1", compound="left", underline="-1")
        self.t_notebook_3_t0.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        # Notebook for the Arduino 2 in Dashboard pane
        self.t_notebook_3_t1 = tk.Frame(self.t_notebook_3)
        self.t_notebook_3.add(self.t_notebook_3_t1, padding=3)
        self.t_notebook_3.tab(1, text="Arduino 2", compound="left", underline="-1")
        self.t_notebook_3_t1.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        # Notebook for the Arduino 3 in Dashboard pane
        self.t_notebook_3_t2 = tk.Frame(self.t_notebook_3)
        self.t_notebook_3.add(self.t_notebook_3_t2, padding=3)
        self.t_notebook_3.tab(2, text="Arduino 3", compound="none", underline="-1")
        self.t_notebook_3_t2.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        # Notebook for the Arduino 4 in Dashboard pane
        self.t_notebook_3_t3 = tk.Frame(self.t_notebook_3)
        self.t_notebook_3.add(self.t_notebook_3_t3, padding=3)
        self.t_notebook_3.tab(3, text="Arduino 4", compound="none", underline="-1")
        self.t_notebook_3_t3.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        # Notebook for the Arduino 5 in Dashboard pane
        self.t_notebook_3_t4 = tk.Frame(self.t_notebook_3)
        self.t_notebook_3.add(self.t_notebook_3_t4, padding=3)
        self.t_notebook_3.tab(4, text="Arduino 5", compound="none", underline="-1")
        self.t_notebook_3_t4.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        self.t_notebook_4 = ttk.Notebook(self.t_notebook_1_t2)
        self.t_notebook_4.place(relx=0.0, rely=0.014, relheight=0.981, relwidth=0.994)
        self.t_notebook_4.configure(takefocus="")

        # Notebook for the configuring sunshade configuration in Config pane
        self.t_notebook_4_t0 = tk.Frame(self.t_notebook_4)
        self.t_notebook_4.add(self.t_notebook_4_t0, padding=3)
        self.t_notebook_4.tab(0, text="Set sunshade config", compound="left", underline="-1")
        self.t_notebook_4_t0.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        self.t_notebook_5 = ttk.Notebook(self.t_notebook_1_t0)
        self.t_notebook_5.place(relx=0.291, rely=0.26, relheight=0.721, relwidth=0.693)
        self.t_notebook_5.configure(takefocus="")

        # Notebook for the Distance on Dashboard pane
        self.t_notebook_5_t0 = tk.Frame(self.t_notebook_5)
        self.t_notebook_5.add(self.t_notebook_5_t0, padding=3)
        self.t_notebook_5.tab(0, text="Distance", compound="left", underline="-1", )
        self.t_notebook_5_t0.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        # Notebook for the Light on Dashboard pane
        self.t_notebook_5_t1 = tk.Frame(self.t_notebook_5)
        self.t_notebook_5.add(self.t_notebook_5_t1, padding=3)
        self.t_notebook_5.tab(1, text="Light", compound="left", underline="-1", )
        self.t_notebook_5_t1.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        # Notebook for the Temperature on Dashboard pane
        self.t_notebook_5_t2 = tk.Frame(self.t_notebook_5)
        self.t_notebook_5.add(self.t_notebook_5_t2, padding=3)
        self.t_notebook_5.tab(2, text="Temperature", compound="none", underline="-1", )
        self.t_notebook_5_t2.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")
        bar3 = Figure(figsize=(5, 2), dpi=75)
        self.ax3 = bar3.add_subplot(111)
        self.ax3.set_title('NOT CONNECTED', color="red")
        self.data3 = (20, 35, 30, 35)

        # The button "CLOSE SUNBLIND" on the "Dashboard" page.
        self.Button23 = ttk.Button(self.t_notebook_1_t0, style='Red.TButton')
        self.Button23.place(relx=0.01, rely=0.863, height=54, relwidth=0.270)
        self.Button23.configure(command=close_zonnescherm,  text='''CLOSE SUNBLIND''')

        # The button "OPEN SUNBLIND" on the "Dashboard" page.
        self.button_1 = ttk.Button(self.t_notebook_1_t0, style='Green.TButton')
        self.button_1.place(relx=0.01, rely=0.767, height=54, relwidth=0.270)
        self.button_1.configure(command=open_zonnescherm, text='''OPEN SUNBLIND''')

        # The 1st "Set" button on the page "Config"
        self.button_2 = ttk.Button(self.t_notebook_4_t0, style='Green.TButton')
        self.button_2.place(relx=0.265, rely=0.029, height=24, relwidth=0.05)
        self.button_2.configure(command=self.set_temp, text='''Set''')

        # The 1st "Set" button on the page "Config"
        self.button_3 = ttk.Button(self.t_notebook_4_t0, style='Green.TButton')
        self.button_3.place(relx=0.265, rely=0.072, height=24, relwidth=0.05)
        self.button_3.configure(command=self.set_light, text='''Set''')

        # The 1st "Reset" button on the page "Config"
        self.button_4 = ttk.Button(self.t_notebook_4_t0, style='Red.TButton')
        self.button_4.place(relx=0.324, rely=0.029, height=24, relwidth=0.05)
        self.button_4.configure(command=self.reset_temp, text='''Reset''')

        # The 2nd "Reset" button on the page "Config"
        self.button_5 = ttk.Button(self.t_notebook_4_t0, style='Red.TButton')
        self.button_5.place(relx=0.324, rely=0.072, height=24, relwidth=0.05)
        self.button_5.configure(command=self.reset_light, text='''Reset''')

        # The 1st "Set" button on the page "Config"
        self.Button6 = ttk.Button(self.t_notebook_4_t0, style='Green.TButton')
        self.Button6.place(relx=0.265, rely=0.116, height=24, relwidth=0.05)
        self.Button6.configure(command=self.set_min_distance, text='''Set''')

        # The 1st "Set" button on the page "Config"
        self.Button7 = ttk.Button(self.t_notebook_4_t0, style='Green.TButton')
        self.Button7.place(relx=0.265, rely=0.159, height=24, relwidth=0.05)
        self.Button7.configure(command=self.set_max_distance, text='''Set''')

        # The 3th "Reset" button on the page "Config"
        self.Button8 = ttk.Button(self.t_notebook_4_t0, style='Red.TButton')
        self.Button8.place(relx=0.324, rely=0.116, height=24, relwidth=0.05)
        self.Button8.configure(command=self.reset_min_distance, text='''Reset''')

        # The 4th "Reset" button on the page "Config"
        self.Button9 = ttk.Button(self.t_notebook_4_t0, style='Red.TButton')
        self.Button9.place(relx=0.324, rely=0.159, height=24, relwidth=0.05)
        self.Button9.configure(command=self.reset_max_distance, text='''Reset''')

        # The button for "Arduino 1" on the "Dashboard" page
        self.button_68 = ttk.Button(self.t_notebook_1_t0, style='Arduino1.TButton')
        self.button_68.place(relx=0.01, rely=0.521, height=74, relwidth=0.080)
        self.button_68.configure(command=self.switch_to_arduino, text='''Arduino 1''')

        # The button for "Arduino 2" on the "Dashboard" page
        self.button_69 = ttk.Button(self.t_notebook_1_t0, style='Arduino2.TButton')
        self.button_69.place(relx=0.105, rely=0.521, height=74, relwidth=0.080)
        self.button_69.configure(command=self.switch_to_arduino_2, text='''Arduino 2''')

        # The button for "Arduino 3" on the "Dashboard" page
        self.button_70 = ttk.Button(self.t_notebook_1_t0, style='Arduino3.TButton')
        self.button_70.place(relx=0.200, rely=0.521, height=74, relwidth=0.080)
        self.button_70.configure(command=self.switch_to_arduino_3, text='''Arduino 3''')

        # The button for "Arduino 4" on the "Dashboard" page
        self.button_71 = ttk.Button(self.t_notebook_1_t0, style='Arduino4.TButton')
        self.button_71.place(relx=0.05, rely=0.644, height=74, relwidth=0.080)
        self.button_71.configure(command=self.switch_to_arduino_4, text='''Arduino 4''')

        # The button for "Arduino 5" on the "Dashboard" page
        self.button_72 = ttk.Button(self.t_notebook_1_t0, style='Arduino5.TButton')
        self.button_72.place(relx=0.155, rely=0.644, height=74, relwidth=0.080)
        self.button_72.configure(command=self.switch_to_arduino_5, text='''Arduino 5''')

        self.checkbuttonstyle = ttk.Style()
        self.checkbuttonstyle.configure('Custom.TCheckbutton', activebackground="#ececec", activeforeground="#000000",
                                        background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                                        highlightbackground="#d9d9d9", highlightcolor="black", justify='left')

        # The checkbutton box for using the changeable config, executes the function "self.toggle_config".
        self.Checkbutton1 = ttk.Checkbutton(self.t_notebook_4_t0, style='Custom.TCheckbutton')
        self.Checkbutton1.place(relx=0.101, rely=0.203, relheight=0.036, relwidth=39)
        self.Checkbutton1.configure(command=self.toggle_config,
                                    text='''Use the above config''')

        # 1st listbox at Dashboard pane
        self.listbox_1 = tk.Listbox(self.t_notebook_1_t0)
        self.listbox_1.place(relx=0.01, rely=0.014, relheight=0.236, relwidth=0.272)
        self.listbox_1.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                 foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                 selectbackground="#c4c4c4", selectforeground="black")

        # 2nd listbox at Dashboard pane
        self.listbox_2 = tk.Listbox(self.t_notebook_1_t0)
        self.listbox_2.place(relx=0.01, rely=0.26, relheight=0.236, relwidth=0.272)
        self.listbox_2.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                 foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                 selectbackground="#c4c4c4", selectforeground="black")

        # listbox at Config pane
        self.listbox_3 = tk.Listbox(self.t_notebook_4_t0)
        self.listbox_3.place(relx=0.40, rely=0.028, relheight=0.166, relwidth=0.272)
        self.listbox_3.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                 foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                 selectbackground="#c4c4c4", selectforeground="black")

        # Distance sensor bar graph - Dashboard
        self.canvasbar1 = FigureCanvasTkAgg(bar1, master=self.t_notebook_2_t0)
        self.canvasbar1.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        # Light sensor bar graph - Dashboard
        self.canvasbar2 = FigureCanvasTkAgg(bar2, master=self.t_notebook_2_t1)
        self.canvasbar2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        # Temperature sensor bar graph - Dashboard
        self.canvasbar3 = FigureCanvasTkAgg(bar3, master=self.t_notebook_2_t2)
        self.canvasbar3.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        # Distance graph dashboard - canvas
        self.fig1 = Figure(figsize=(5, 4), dpi=100)
        self.canvas1 = self.fig1.add_subplot(1, 1, 1)
        self.canvasx = []
        self.canvas1y = []
        self.newx = 0

        self.canvas1a = FigureCanvasTkAgg(self.fig1, master=self.t_notebook_5_t0)  # A tk.DrawingArea.

        self.toolbar = NavigationToolbar2Tk(self.canvas1a, self.t_notebook_5_t0)
        self.toolbar.update()
        self.canvas1a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        # Light graph dashboard - canvas
        fig2 = Figure(figsize=(5, 4), dpi=100)
        self.canvas2 = fig2.add_subplot(1, 1, 1)
        self.canvas2y = []
        self.canvas2x = []
        self.new2x = 0

        self.canvas2a = FigureCanvasTkAgg(fig2, master=self.t_notebook_5_t1)  # A tk.DrawingArea.

        toolbar = NavigationToolbar2Tk(self.canvas2a, self.t_notebook_5_t1)
        toolbar.update()
        self.canvas2a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        # Temperature graph dashboard - canvas
        fig3 = Figure(figsize=(5, 4), dpi=100)
        self.canvas3 = fig3.add_subplot(1, 1, 1)
        self.canvas3y = []
        self.canvas3x = []
        self.new3x = 0

        self.canvas3a = FigureCanvasTkAgg(fig3, master=self.t_notebook_5_t2)  # A tk.DrawingArea.

        toolbar = NavigationToolbar2Tk(self.canvas3a, self.t_notebook_5_t2)
        toolbar.update()
        self.canvas3a.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        # Distance, Light and Temperature graphs of Arduino 1 in graph panel
        fig4 = Figure(figsize=(5, 8), dpi=100)
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

        # Distance, Light and Temperature graphs of Arduino 2 in graph panel
        fig5 = Figure(figsize=(5, 8), dpi=100)
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

        # Distance, Light and Temperature graphs of Arduino 3 in graph panel
        fig6 = Figure(figsize=(5, 8), dpi=100)
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

        # Distance, Light and Temperature graphs of Arduino 4 in graph panel
        fig7 = Figure(figsize=(5, 8), dpi=100)
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

        # Distance, Light and Temperature graphs of Arduino 5 in graph panel
        fig8 = Figure(figsize=(5, 8), dpi=100)
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

        # Style for all the entry boxes on the "Config" page.
        self.entry_style = ttk.Style()
        self.entry_style.configure('Custom.TEntry', background="white", disabledforeground="#a3a3a3",
                                   font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                                   highlightcolor="black", insertbackground="black", selectbackground="#c4c4c4",
                                   selectforeground="black")

        # The 1st entry box on the "Config" page.
        self.entry_1 = ttk.Entry(self.t_notebook_4_t0, style='Custom.TEntry')
        self.entry_1.place(relx=0.101, rely=0.029, height=20, relwidth=0.161)

        # The 2nd entry box on the "Config" page.
        self.entry_2 = ttk.Entry(self.t_notebook_4_t0, style='Custom.TEntry')
        self.entry_2.place(relx=0.101, rely=0.072, height=20, relwidth=0.161)

        # The 3rd entry box on the "Config" page.
        self.entry_3 = ttk.Entry(self.t_notebook_4_t0, style='Custom.TEntry')
        self.entry_3.place(relx=0.101, rely=0.116, height=20, relwidth=0.161)

        # The 4th entry box on the "Config" page.
        self.entry_4 = ttk.Entry(self.t_notebook_4_t0, style='Custom.TEntry')
        self.entry_4.place(relx=0.101, rely=0.159, height=20, relwidth=0.161)

        self.label_style = ttk.Style()
        self.label_style.configure('Custom.TLabel', activebackground="#f9f9f9", activeforeground="black",
                                   background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000",
                                   highlightbackground="#d9d9d9", highlightcolor="black")

        # Label for the text on the "Help" page.
        self.label_1 = ttk.Label(self.t_notebook_1_t3, style='Custom.TLabel')
        self.label_1.place(relx=0.01, rely=0.014, height=674, width=674)
        self.label_1.configure(text='''INSTRUCTIONS:
        
        DASHBOARD:
        The dashboard shows an overview of the application, including graphs showing the current distance (between the
        sun blind and it's lowest point, as a check whether or not the sun blind is functioning correctly), temperature 
        (in °C), and light level (in Lux), as well as controls for the sunblind, bar graphs showing average values, and
        controls to determine which Arduino is shown in the graphs. An overview which shows which Arduino's are plugged
        ino the system
        
        GRAPH:
        The graph tab shows all data from all Arduino's in seperate graphs. Use the tabs to switch between which Arduino
        to display.
    
        CONFIG:
        The config window allows you to configure at what settings you want the sun screen to automatically open/close.
        
        The Temprature field allows a user to set a minimum temperature (in °C) through the set button. 
        If the temperature falls below this value the screen will automatically close, if the temperature exceeds the
        set minimum the screen will automatically open.
        
        The Light field allows a user to set a minimum light value (in Lux) through the set button.
        If the light value falls below this value the screen will automatically close, if the light value exceeds the
        set minimum the screen will automatically open.
        
        The reset buttons will set the minimum temprature/light value (depending on the reset button used) back to their
        default value.
        
        The set minimum and maximum distance can be used to set at what minimal and maximal distance the sunscreen is
        detirmined to be closed or open (respectively). This setting can be used in case the sunblinds are moved to a
        location with more or less room so the sensors can still work accurately.
        
        The "Use the above config" checkbox determines whether or not the screen will automatically open/close if
        minimum values are reached/exceeded. If checked off the default values will be used instead.
        
        HELP:
        This current window
        
        Free Hong Kong!
        A revolution in our generation!''')

        # 1st label on the "Config" page.
        self.label_2 = ttk.Label(self.t_notebook_4_t0, style='Custom.TLabel')
        self.label_2.place(relx=0.0, rely=0.029, height=21, relwidth=0.1)
        self.label_2.configure(text='''Set temperature''')

        # 2nd label on the "Config" page.
        self.label_2 = ttk.Label(self.t_notebook_4_t0, style='Custom.TLabel')
        self.label_2.place(relx=0.0, rely=0.072, height=21, relwidth=0.1)
        self.label_2.configure(text='''Set light''')

        # 3rd label on the "Config" page.
        self.Label2 = ttk.Label(self.t_notebook_4_t0, style='Custom.TLabel')
        self.Label2.place(relx=0.0, rely=0.116, height=21, relwidth=0.1)
        self.Label2.configure(text='''Set minimal distance''')

        # 4th label on the "Config" page.
        self.Label2 = ttk.Label(self.t_notebook_4_t0, style='Custom.TLabel')
        self.Label2.place(relx=0.0, rely=0.159, height=21, relwidth=0.1)
        self.Label2.configure(text='''Set maximum distance''')

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

    # Breaking the root.mainloop with a loop
    def loop(self):
        global counter, getallen, aantal_huidig, arduinos

        self.open_or_close(temp_gemiddelde, light_gemiddelde, distance_gemiddelde)
        self.main_loop()
        root.after(1000, self.loop)

    # main loop for running all the funtions
    def main_loop(self):
        self.fix_grafieken()
        self.button_kleur()
        aantal_live = len(arduinos)
        self.listbox_1.delete(0, END)
        self.listbox_2.delete(0, END)
        self.listbox_3.delete(0, END)
        set_current_graph(self.huidige_grafiek, self.run_config)
        status = get_zonnescherm()
        if self.tmp_for_styles != aantal_live:
            self.reset_arduino_button_styles(aantal_live)

        set_min_max_length(self.mindistance ,self.maxdistance)
        for i in range(5):
            if zonnescherm_status[i] == 1:
                self.fill_listbox_2(str("Sunblind ") + str(i + 1) + str(" is open"), i + 1)
            elif zonnescherm_status[i] == 2:
                self.fill_listbox_2(str("Sunblind ") + str(i + 1) + str(" is closed"), i + 1)
            elif zonnescherm_status[i] == 3:
                self.fill_listbox_2(str("Sunblind ") + str(i + 1) + str(" is buzy"), i + 1)
        for i in range(5):
            if i+1 <= aantal_live:
                self.fill_listbox_1(str("Arduino ") + str(i+1) + str(" is online"), i+1)
            else:
                self.fill_listbox_1(str("Arduino ") + str(i+1) + str(" is not online"), i+1)
        config_status = ""
        if self.run_config == 1:
            config_status = "on"
        else:
            config_status = "off"
        self.fill_listbox_3(str("Config is: " + config_status), 1)
        self.fill_listbox_3(str("Current temp setting: " + str(self.maxtemp)), 2)
        self.fill_listbox_3(str("Current light setting: " + str(self.maxlight)), 3)
        self.fill_listbox_3(str("Current min distance setting: " + str(self.mindistance)), 4)
        self.fill_listbox_3(str("Current max distance setting: " + str(self.maxdistance)), 5)

    # updating the graphs
    def fix_grafieken(self):
        self.animatecanvas1(distance_gemiddelde[self.huidige_grafiek])
        self.animatecanvas2(light_gemiddelde[self.huidige_grafiek])
        self.animatecanvas3(int(temp_gemiddelde[self.huidige_grafiek]/10))

        self.animatecanvas4(distance_gemiddelde[0])
        self.animatecanvas5(int(temp_gemiddelde[0]/10))
        self.animatecanvas12(light_gemiddelde[0])
        self.animatecanvas6(distance_gemiddelde[1])
        self.animatecanvas7(int(temp_gemiddelde[1]/10))
        self.animatecanvas13(light_gemiddelde[1])
        self.animatecanvas8(distance_gemiddelde[2])
        self.animatecanvas9(int(temp_gemiddelde[2]/10))
        self.animatecanvas14(light_gemiddelde[2])
        self.animatecanvas10(distance_gemiddelde[3])
        self.animatecanvas11(int(temp_gemiddelde[3]/10))
        self.animatecanvas15(light_gemiddelde[3])
        self.animatecanvas16(distance_gemiddelde[4])
        self.animatecanvas17(int(temp_gemiddelde[4]/10))
        self.animatecanvas18(light_gemiddelde[4])

        self.set_bar1_data(distance_gemiddelde[0], distance_gemiddelde[1], distance_gemiddelde[2],
                           distance_gemiddelde[3], distance_gemiddelde[4])
        self.set_bar2_data(light_gemiddelde[0], light_gemiddelde[1], light_gemiddelde[2], light_gemiddelde[3],
                           light_gemiddelde[4])
        self.set_bar3_data(int(temp_gemiddelde[0]/10), int(temp_gemiddelde[1]/10), int(temp_gemiddelde[2]/10),
                           int(temp_gemiddelde[3]/10), int(temp_gemiddelde[4]/10))

    # The function for auto open or closing
    def open_or_close(self, gemiddelde_temp, gemiddelde_light, gemiddelde_afstand):
        aantal_live = len(arduinos)
        aantal_light = 0
        aantal_temp = 0
        aantal_afstand = 0
        light = 0
        temp = 0
        afstand = 0
        for i in gemiddelde_temp:
            if i != 0:
                aantal_temp += 1
                temp += int(i/10)

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
        if self.run_config == 1:
            # deze code kan alleen wanneer er echt een motor is aangesloten.
                #for i in range(0, aantal_live):
                    #if light > self.maxlight or temp > self.maxtemp:
                        #if zonnescherm_status[i] == 2:
                            #open_zonnescherm()
                   # else:
                        #if zonnescherm_status[i] == 1:
                            #close_zonnescherm()
            if light > self.maxlight:
                print("LIGHT | OPEN")
            if temp > self.maxtemp:
                print("TEMP | OPEN")
            if light < self.maxlight:
                print("LIGHT | CLOSE")
            if temp < self.maxtemp:
                print("TEMP | CLOSE")
            print("")

    # Animate function for graph, input new Y and increments the X
    def animatecanvas1(self, y):
        self.canvasx.append(self.newx)
        if len(self.canvasx) > 20:
            del self.canvasx[0]
            del self.canvas1y[0]
            self.canvas1.clear()
        self.canvas1y.append(y)
        self.newx += 1
        self.canvas1.set_ylim(0, 300)  # change this if the max limit has to change
        self.canvas1.set_title('Average distance')
        self.canvas1.set_ylabel('Distance (cm)')
        self.canvas1.set_xlabel('Time (s)')
        self.canvas1.plot(self.canvasx, self.canvas1y, color="blue")
        self.canvas1a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas2(self, y):
        self.canvas2x.append(self.new2x)
        if len(self.canvas2x) > 20:
            del self.canvas2x[0]
            del self.canvas2y[0]
            self.canvas2.clear()
        self.canvas2y.append(y)
        self.new2x += 1
        self.canvas2.set_ylim(0, 120)  # change this if the max limit has to change
        self.canvas2.set_title('Average lightintensity')
        self.canvas2.set_ylabel('Light (lux)')
        self.canvas2.set_xlabel('Time (s)')
        self.canvas2.plot(self.canvas2x, self.canvas2y, color="yellow")
        self.canvas2a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas3(self, y):
        self.canvas3x.append(self.new3x)
        if len(self.canvas3x) > 20:
            del self.canvas3x[0]
            del self.canvas3y[0]
            self.canvas3.clear()
        self.canvas3y.append(y)
        self.new3x += 1
        self.canvas3.set_ylim(0, 35)  # change this if the max limit has to change
        self.canvas3.set_title('Average Temperature')
        self.canvas3.set_ylabel('Temperature (°C)')
        self.canvas3.set_xlabel('Time (s)')
        self.canvas3.plot(self.canvas3x, self.canvas3y, color="red")
        self.canvas3a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas4(self, y):
        self.canvas4x.append(self.new4x)
        if len(self.canvas4x) > 20:
            del self.canvas4x[0]
            del self.canvas4y[0]
            self.canvas4.clear()
        self.canvas4y.append(y)
        self.new4x += 1
        self.canvas4.set_ylim(0, 300)  # change this if the max limit has to change
        self.canvas4.set_title('Average distance')
        self.canvas4.set_ylabel('Distance (cm)')
        self.canvas4.set_xlabel('Time (s)')
        self.canvas4.plot(self.canvas4x, self.canvas4y, color="blue")
        self.canvas4a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas5(self, y):
        self.canvas5x.append(self.new5x)
        if len(self.canvas5x) > 20:
            del self.canvas5x[0]
            del self.canvas5y[0]
            self.canvas5.clear()
        self.canvas5y.append(y)
        self.new5x += 1
        self.canvas5.set_ylim(0, 35)  # change this if the max limit has to change
        self.canvas5.set_title('Average temperature')
        self.canvas5.set_ylabel('Temperature (°C)')
        self.canvas5.set_xlabel('Time (s)')
        self.canvas5.plot(self.canvas5x, self.canvas5y, color="red")
        self.canvas4a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas6(self, y):
        self.canvas6x.append(self.new6x)
        if len(self.canvas6x) > 20:
            del self.canvas6x[0]
            del self.canvas6y[0]
            self.canvas6.clear()
        self.canvas6y.append(y)
        self.new6x += 1
        self.canvas6.set_ylim(0, 300)  # change this if the max limit has to change
        self.canvas6.set_title('Average distance')
        self.canvas6.set_ylabel('Distance (cm)')
        self.canvas6.set_xlabel('Time (s)')
        self.canvas6.plot(self.canvas6x, self.canvas6y, color="blue")
        self.canvas5a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas7(self, y):
        self.canvas7x.append(self.new7x)
        if len(self.canvas7x) > 20:
            del self.canvas7x[0]
            del self.canvas7y[0]
            self.canvas7.clear()
        self.canvas7y.append(y)
        self.new7x += 1
        self.canvas7.set_ylim(0, 35)  # change this if the max limit has to change
        self.canvas7.set_title('Average temperature')
        self.canvas7.set_ylabel('Temperature (°C)')
        self.canvas7.set_xlabel('Time (s)')
        self.canvas7.plot(self.canvas7x, self.canvas7y, color="red")
        self.canvas5a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas8(self, y):
        self.canvas8x.append(self.new8x)
        if len(self.canvas8x) > 20:
            del self.canvas8x[0]
            del self.canvas8y[0]
            self.canvas8.clear()
        self.canvas8y.append(y)
        self.new8x += 1
        self.canvas8.set_ylim(0, 300)  # change this if the max limit has to change
        self.canvas8.set_title('Average distance')
        self.canvas8.set_ylabel('Distance (cm)')
        self.canvas8.set_xlabel('Time (s)')
        self.canvas8.plot(self.canvas8x, self.canvas8y, color="blue")
        self.canvas6a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas9(self, y):
        self.canvas9x.append(self.new9x)
        if len(self.canvas9x) > 20:
            del self.canvas9x[0]
            del self.canvas9y[0]
            self.canvas9.clear()
        self.canvas9y.append(y)
        self.new9x += 1
        self.canvas9.set_ylim(0, 35)  # change this if the max limit has to change
        self.canvas9.set_title('Average temperature')
        self.canvas9.set_ylabel('Temperature (°C)')
        self.canvas9.set_xlabel('Time (s)')
        self.canvas9.plot(self.canvas9x, self.canvas9y, color="red")
        self.canvas6a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas10(self, y):
        self.canvas10x.append(self.new10x)
        if len(self.canvas10x) > 20:
            del self.canvas10x[0]
            del self.canvas10y[0]
            self.canvas10.clear()
        self.canvas10y.append(y)
        self.new10x += 1
        self.canvas10.set_ylim(0, 300)  # change this if the max limit has to change
        self.canvas10.set_title('Average distance')
        self.canvas10.set_ylabel('Distance (cm)')
        self.canvas10.set_xlabel('Time (s)')
        self.canvas10.plot(self.canvas10x, self.canvas10y, color="blue")
        self.canvas7a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas11(self, y):
        self.canvas11x.append(self.new11x)
        if len(self.canvas11x) > 20:
            del self.canvas11x[0]
            del self.canvas11y[0]
            self.canvas11.clear()
        self.canvas11y.append(y)
        self.new11x += 1
        self.canvas11.set_ylim(0, 35)  # change this if the max limit has to change
        self.canvas11.set_title('Average temperature')
        self.canvas11.set_ylabel('Temperature (°C)')
        self.canvas11.set_xlabel('Time (s)')
        self.canvas11.plot(self.canvas11x, self.canvas11y, color="red")
        self.canvas7a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas12(self, y):
        self.canvas12x.append(self.new12x)
        if len(self.canvas12x) > 20:
            del self.canvas12x[0]
            del self.canvas12y[0]
            self.canvas12.clear()
        self.canvas12y.append(y)
        self.new12x += 1
        self.canvas12.set_ylim(0, 120)  # change this if the max limit has to change
        self.canvas12.set_title('Average lightintensity')
        self.canvas12.set_ylabel('Light (lux)')
        self.canvas12.set_xlabel('Time (s)')
        self.canvas12.plot(self.canvas12x, self.canvas12y, color="yellow")
        self.canvas4a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas13(self, y):
        self.canvas13x.append(self.new13x)
        if len(self.canvas13x) > 20:
            del self.canvas13x[0]
            del self.canvas13y[0]
            self.canvas13.clear()
        self.canvas13y.append(y)
        self.new13x += 1
        self.canvas13.set_ylim(0, 120)  # change this if the max limit has to change
        self.canvas13.set_title('Average lightintensity')
        self.canvas13.set_ylabel('Light (lux)')
        self.canvas13.set_xlabel('Time (s)')
        self.canvas13.plot(self.canvas13x, self.canvas13y, color="yellow")
        self.canvas5a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas14(self, y):
        self.canvas14x.append(self.new14x)
        if len(self.canvas14x) > 20:
            del self.canvas14x[0]
            del self.canvas14y[0]
            self.canvas14.clear()
        self.canvas14y.append(y)
        self.new14x += 1
        self.canvas14.set_ylim(0, 120)  # change this if the max limit has to change
        self.canvas14.set_title('Average lightintensity')
        self.canvas14.set_ylabel('Light (lux)')
        self.canvas14.set_xlabel('Time (s)')
        self.canvas14.plot(self.canvas14x, self.canvas14y, color="yellow")
        self.canvas6a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas15(self, y):
        self.canvas15x.append(self.new15x)
        if len(self.canvas15x) > 20:
            del self.canvas15x[0]
            del self.canvas15y[0]
            self.canvas15.clear()
        self.canvas15y.append(y)
        self.new15x += 1
        self.canvas15.set_ylim(0, 120)  # change this if the max limit has to change
        self.canvas15.set_title('Average lightintensity')
        self.canvas15.set_ylabel('Light (lux)')
        self.canvas15.set_xlabel('Time (s)')
        self.canvas15.plot(self.canvas15x, self.canvas15y, color="yellow")
        self.canvas7a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas16(self, y):
        self.canvas16x.append(self.new16x)
        if len(self.canvas16x) > 20:
            del self.canvas16x[0]
            del self.canvas16y[0]
            self.canvas16.clear()
        self.canvas16y.append(y)
        self.new16x += 1
        self.canvas16.set_ylim(0, 300)  # change this if the max limit has to change
        self.canvas16.set_title('Average distance')
        self.canvas16.set_ylabel('Distance (cm)')
        self.canvas16.set_xlabel('Time (s)')
        self.canvas16.plot(self.canvas16x, self.canvas16y, color="blue")
        self.canvas8a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas17(self, y):
        self.canvas17x.append(self.new17x)
        if len(self.canvas17x) > 20:
            del self.canvas17x[0]
            del self.canvas17y[0]
            self.canvas17.clear()
        self.canvas17y.append(y)
        self.new17x += 1
        self.canvas17.set_ylim(0, 35)  # change this if the max limit has to change
        self.canvas17.set_title('Average temperature')
        self.canvas17.set_ylabel('Temperature (°C)')
        self.canvas17.set_xlabel('Time (s)')
        self.canvas17.plot(self.canvas17x, self.canvas17y, color="red")
        self.canvas8a.draw()

    # Animate function for graph, input new Y and increments the X
    def animatecanvas18(self, y):
        self.canvas18x.append(self.new18x)
        if len(self.canvas18x) > 20:
            del self.canvas18x[0]
            del self.canvas18y[0]
            self.canvas18.clear()
        self.canvas18y.append(y)
        self.new18x += 1
        self.canvas18.set_ylim(0, 120)  # change this if the max limit has to change
        self.canvas18.set_title('Average lightintensity')
        self.canvas18.set_ylabel('Light (lux)')
        self.canvas18.set_xlabel('Time (s)')
        self.canvas18.plot(self.canvas18x, self.canvas18y, color="yellow")
        self.canvas8a.draw()

    # clears the graphs on the dashboard and all of their values
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

    # resets the buttons for switching the arduino's
    def reset_arduino_button_styles(self, amount_of_arduinos):
        self.tmp_for_styles = amount_of_arduinos
        if len(arduinos) >= 1:
            self.arduino1style.configure("Arduino1.TButton", background="black", foreground="black",
                                         font=('Sans', '10', 'normal'))
        if len(arduinos) >= 2:
            self.arduino2style.configure("Arduino2.TButton", background="black", foreground="black",
                                         font=('Sans', '10', 'normal'))
        if len(arduinos) >= 3:
            self.arduino3style.configure("Arduino3.TButton", background="black", foreground="black",
                                         font=('Sans', '10', 'normal'))
        if len(arduinos) >= 4:
            self.arduino4style.configure("Arduino4.TButton", background="black", foreground="black",
                                         font=('Sans', '10', 'normal'))
        if len(arduinos) >= 5:
            self.arduino5style.configure("Arduino5.TButton", background="black", foreground="black",
                                         font=('Sans', '10', 'normal'))

    # switch the dashboard graph to the selected arduino
    def switch_to_arduino(self):
        length = len(arduinos)
        if length > 0:
            self.clear_canvasses_dashboard()
            self.reset_arduino_button_styles(length)
            self.arduino1style.configure("Arduino1.TButton", background="green", foreground="black",
                                         font=('Sans', '10', 'bold'))
            self.huidige_grafiek = 0

    # switch the dashboard graph to the selected arduino
    def switch_to_arduino_2(self):
        length = len(arduinos)
        if length > 1:
            self.clear_canvasses_dashboard()
            self.reset_arduino_button_styles(length)
            self.arduino2style.configure("Arduino2.TButton", background="green", foreground="black",
                                         font=('Sans', '10', 'bold'))
            self.huidige_grafiek = 1                # led = rood

    # switch the dashboard graph to the selected arduino
    def switch_to_arduino_3(self):
        length = len(arduinos)
        if length > 2:
            self.clear_canvasses_dashboard()
            self.reset_arduino_button_styles(length)
            self.arduino3style.configure("Arduino3.TButton", background="green", foreground="black",
                                         font=('Sans', '10', 'bold'))
            self.huidige_grafiek = 2                # led = groen

    # switch the dashboard graph to the selected arduino
    def switch_to_arduino_4(self):
        length = len(arduinos)
        if length > 3:
            self.clear_canvasses_dashboard()
            self.reset_arduino_button_styles(length)
            self.arduino4style.configure("Arduino4.TButton", background="green", foreground="black",
                                         font=('Sans', '10', 'bold'))
            self.huidige_grafiek = 3                # led = rood

    # switch the dashboard graph to the selected arduino
    def switch_to_arduino_5(self):
        length = len(arduinos)
        if length > 4:
            self.clear_canvasses_dashboard()
            self.reset_arduino_button_styles(length)
            self.arduino5style.configure("Arduino5.TButton", background="green", foreground="black",
                                         font=('Sans', '10', 'bold'))
            self.huidige_grafiek = 4

    # setter for bar3, this is the DISTANCE field on the dashboard
    def set_bar1_data(self, ad1, ad2, ad3, ad4, ad5):
        self.data1 = (ad1, ad2, ad3, ad4, ad5)
        self.ax1.clear()
        self.ax1.bar(self.ind, self.data1, .5)
        self.ax1.set_xticks(self.ind)
        self.ax1.set_xticklabels(('Arduino 1', 'Arduino 2', 'Arduino 3', 'Arduino 4', 'Arduino 5'))
        self.ax1.set_title("Average distance")
        self.ax1.set_ylabel("distance (cm)")
        self.canvasbar1.draw()

    # setter for bar3, this is the LIGHT field on the dashboard
    def set_bar2_data(self, ad1, ad2, ad3, ad4, ad5):
        self.data2 = (ad1, ad2, ad3, ad4, ad5)
        self.ax2.clear()
        self.ax2.bar(self.ind, self.data2, .5, color="yellow")
        self.ax2.set_xticks(self.ind)
        self.ax2.set_xticklabels(('Arduino 1', 'Arduino 2', 'Arduino 3', 'Arduino 4', 'Arduino 5'))
        self.ax2.set_title("Average lightintensity")
        self.ax2.set_ylabel("Lightintensity (lux)")
        self.canvasbar2.draw()

    # setter for bar3, this is the temperature field on the dashboard
    def set_bar3_data(self, ad1, ad2, ad3, ad4, ad5):
        self.data3 = (ad1, ad2, ad3, ad4, ad5)
        self.ax3.clear()
        self.ax3.bar(self.ind, self.data3, .5, color="red")
        self.ax3.set_xticks(self.ind)
        self.ax3.set_xticklabels(('Arduino 1', 'Arduino 2', 'Arduino 3', 'Arduino 4', 'Arduino 5'))
        self.ax3.set_title("Average temperature")
        self.ax3.set_ylabel("Temperature (°C)")
        self.canvasbar3.draw()

    # fill function for listbox1, TOP one on dashboard
    def fill_listbox_1(self, string, index):
        self.listbox_1.insert(index, string)
        if len(string) == 23:
            self.listbox_1.itemconfig(index-1, {'bg':'red', 'fg': 'white'})
        else:
            self.listbox_1.itemconfig(index - 1, {'bg': 'green'})

    # fill function for listbox2, BOTTOM one on dashboard
    def fill_listbox_2(self, string, index):
        self.listbox_2.insert(index, string)
        if "open" in string:
            self.listbox_2.itemconfig(index-1, {'bg': 'green', 'fg': 'black'})
        elif "closed" in string:
            self.listbox_2.itemconfig(index - 1, {'bg': 'red', 'fg': 'white'})
        else:
            self.listbox_2.itemconfig(index - 1, {'bg': 'yellow', 'fg': 'black'})

    # fill function for listbox3, the listbox on the config pane
    def fill_listbox_3(self, string, index):
        self.listbox_3.insert(index, string)

    # function that colors the button when a open or close signal is given
    def button_kleur(self):
        if self.run_config == 0:
            if open_of_dicht == 1:
                self.Button23 = ttk.Button(self.t_notebook_1_t0, style='Greenfull.TButton')
                self.Button23.place(relx=0.01, rely=0.863, height=54, relwidth=0.270)
                self.Button23.configure(command=open_zonnescherm, text='''CLOSE SCHERM''')
                self.button_1 = ttk.Button(self.t_notebook_1_t0, style='Redfull.TButton')
                self.button_1.place(relx=0.01, rely=0.767, height=54, relwidth=0.270)
                self.button_1.configure(command=open_zonnescherm, text='''OPEN SCHERM''')
            elif open_of_dicht == 2:
                self.button_1 = ttk.Button(self.t_notebook_1_t0, style='Red.TButton')
                self.button_1.place(relx=0.01, rely=0.767, height=54, relwidth=0.270)
                self.button_1.configure(command=close_zonnescherm, text='''OPEN SCHERM''')
                self.Button23 = ttk.Button(self.t_notebook_1_t0, style='Greenfull.TButton')
                self.Button23.place(relx=0.01, rely=0.863, height=54, relwidth=0.270)
                self.Button23.configure(command=close_zonnescherm, text='''CLOSE SCHERM''')

    # set function for the max temperature
    def set_temp(self):
        try:
            self.maxtemp = int(self.entry_1.get())
        except ValueError:
            print("Value of maxtemp has not changed")

    # toggle checkbox in config panel
    def toggle_config(self):
        if self.run_config == 0:
            self.run_config = 1
        else:
            self.run_config = 0

    # set the light value
    def set_light(self):
        try:
            self.maxlight = int(self.entry_2.get())
        except ValueError:
            print("Value of maxlight has not changed")

    # reset temp field
    def reset_temp(self):
        self.maxtemp = 20

    # reset the light field
    def reset_light(self):
        self.maxlight = 70

    # set the minimum distance
    def set_min_distance(self):
        try:
            self.mindistance = int(self.entry_3.get())
        except ValueError:
            print("Value of mindistance has not changed")

    # set the max distance
    def set_max_distance(self):
        try:
            self.maxdistance = int(self.entry_4.get())
        except ValueError:
            print("Value of maxdistance has not changed")

    # reset the min distance
    def reset_min_distance(self):
        self.mindistance = 20

    # reset the max distance
    def reset_max_distance(self):
        self.maxdistance = 140


if __name__ == '__main__':
    vp_start_gui()
