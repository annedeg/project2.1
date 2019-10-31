from tkinter import *
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

import unknown_support


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

        top.geometry("1032x754+454+171")
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
        self.TNotebook1.place(relx=0.0, rely=0.0, relheight=0.989
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

        self.Text1 = tk.Text(self.TNotebook1_t0)
        self.Text1.place(relx=0.01, rely=0.264, relheight=0.222, relwidth=0.272)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(inactiveselectbackground="#000000")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")

        self.Text1 = tk.Text(self.TNotebook1_t0)
        self.Text1.place(relx=0.01, rely=0.5, relheight=0.236, relwidth=0.272)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(inactiveselectbackground="#000000")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")

        self.Canvas1 = tk.Canvas(self.TNotebook1_t0)
        self.Canvas1.place(relx=0.291, rely=0.264, relheight=0.699
                           , relwidth=0.68)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.create_line(50, 550, 1150, 550, width=2)  # x-axis dikke lijn
        self.Canvas1.create_text(600, 575, text='Step')  # ik weet niet welke tekst hier moet
        self.Canvas1.create_line(50, 550, 50, 50, width=2)  # y-axis dikke lijn
        self.Canvas1.create_text(18, 275,
                                text='Value')  # Ziet er echt super slordig uit maar ik weet niet hoe ik die text opzij kan
        # flippen dus hij ziet hier maar ietsje lelijk erbij

        # x-axis
        for i in range(23):
            x = 50 + (i * 50)
            self.Canvas1.create_line(x, 550, x, 50, width=1, dash=(2, 5))
            self.Canvas1.create_text(x, 550, text='%d' % (10 * i), anchor=N)

        # y-axis
        for i in range(11):
            y = 550 - (i * 50)
            self.Canvas1.create_line(50, y, 1150, y, width=1, dash=(2, 5))
            self.Canvas1.create_text(40, y, text='%d' % (10 * i), anchor=E)

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.01, rely=0.778, height=54, width=277)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''OPEN SCHERM''')

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.01, rely=0.875, height=54, width=277)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''CLOSE SCHERM''')

        self.Listbox1 = tk.Listbox(self.TNotebook1_t0)
        self.Listbox1.place(relx=0.01, rely=0.014, relheight=0.239
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
        self.TNotebook2.place(relx=0.291, rely=0.014, relheight=0.244
                              , relwidth=0.68)
        self.TNotebook2.configure(takefocus="")
        self.TNotebook2_t0 = tk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.TNotebook2_t0, padding=3)
        self.TNotebook2.tab(0, text="Afstandsensor", compound="left"
                            , underline="-1", )
        self.TNotebook2_t0.configure(background="#d9d9d9")
        self.TNotebook2_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook2_t0.configure(highlightcolor="black")
        self.TNotebook2_t1 = tk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.TNotebook2_t1, padding=3)
        self.TNotebook2.tab(1, text="Lichtsensor", compound="left", underline="-1"
                            , )
        self.TNotebook2_t1.configure(background="#d9d9d9")
        self.TNotebook2_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook2_t1.configure(highlightcolor="black")
        self.TNotebook2_t2 = tk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.TNotebook2_t2, padding=3)
        self.TNotebook2.tab(2, text="Temperatuur", compound="none", underline="-1"
                            , )
        self.TNotebook2_t2.configure(background="#d9d9d9")
        self.TNotebook2_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook2_t2.configure(highlightcolor="black")

        self.TNotebook3 = ttk.Notebook(self.TNotebook1_t1)
        self.TNotebook3.place(relx=0.01, rely=0.014, relheight=0.967
                              , relwidth=0.975)
        self.TNotebook3.configure(takefocus="")
        self.TNotebook3_t0 = tk.Frame(self.TNotebook3)
        self.TNotebook3.add(self.TNotebook3_t0, padding=3)
        self.TNotebook3.tab(0, text="Licht", compound="left", underline="-1", )
        self.TNotebook3_t0.configure(background="#d9d9d9")
        self.TNotebook3_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook3_t0.configure(highlightcolor="black")
        self.TNotebook3_t1 = tk.Frame(self.TNotebook3)
        self.TNotebook3.add(self.TNotebook3_t1, padding=3)
        self.TNotebook3.tab(1, text="Temperatuur", compound="left", underline="-1"
                            , )
        self.TNotebook3_t1.configure(background="#d9d9d9")
        self.TNotebook3_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook3_t1.configure(highlightcolor="black")
        self.TNotebook3_t2 = tk.Frame(self.TNotebook3)
        self.TNotebook3.add(self.TNotebook3_t2, padding=3)
        self.TNotebook3.tab(2, text="Afstand", compound="none", underline="-1", )
        self.TNotebook3_t2.configure(background="#d9d9d9")
        self.TNotebook3_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook3_t2.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(self.TNotebook1_t2)
        self.Entry1.place(relx=0.456, rely=0.028, height=20, relwidth=0.159)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry1 = tk.Entry(self.TNotebook1_t2)
        self.Entry1.place(relx=0.456, rely=0.069, height=20, relwidth=0.159)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry1 = tk.Entry(self.TNotebook1_t2)
        self.Entry1.place(relx=0.456, rely=0.111, height=20, relwidth=0.159)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry1 = tk.Entry(self.TNotebook1_t2)
        self.Entry1.place(relx=0.456, rely=0.153, height=20, relwidth=0.159)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Checkbutton1 = tk.Checkbutton(self.TNotebook1_t2)
        self.Checkbutton1.place(relx=0.01, rely=0.028, relheight=0.035
                                , relwidth=0.093)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Temperatuur''')
        self.Checkbutton1.configure(variable=unknown_support.che71)

        self.Checkbutton1 = tk.Checkbutton(self.TNotebook1_t2)
        self.Checkbutton1.place(relx=0.01, rely=0.056, relheight=0.035
                                , relwidth=0.059)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Licht''')
        self.Checkbutton1.configure(variable=unknown_support.che71)

        self.Checkbutton1 = tk.Checkbutton(self.TNotebook1_t2)
        self.Checkbutton1.place(relx=0.01, rely=0.083, relheight=0.035
                                , relwidth=0.069)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Afstand''')
        self.Checkbutton1.configure(variable=unknown_support.che71)

        self.Checkbutton1 = tk.Checkbutton(self.TNotebook1_t2)
        self.Checkbutton1.place(relx=0.01, rely=0.111, relheight=0.035
                                , relwidth=0.04)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''????''')
        self.Checkbutton1.configure(variable=unknown_support.che71)

        self.Button2 = tk.Button(self.TNotebook1_t2)
        self.Button2.place(relx=0.631, rely=0.028, height=24, width=30)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Set!''')

        self.Button3 = tk.Button(self.TNotebook1_t2)
        self.Button3.place(relx=0.67, rely=0.028, height=24, width=49)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Default''')

        self.Button2 = tk.Button(self.TNotebook1_t2)
        self.Button2.place(relx=0.631, rely=0.069, height=24, width=30)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Set!''')

        self.Button3 = tk.Button(self.TNotebook1_t2)
        self.Button3.place(relx=0.67, rely=0.069, height=24, width=49)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Default''')

        self.Button2 = tk.Button(self.TNotebook1_t2)
        self.Button2.place(relx=0.631, rely=0.111, height=24, width=30)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Set!''')

        self.Button3 = tk.Button(self.TNotebook1_t2)
        self.Button3.place(relx=0.67, rely=0.111, height=24, width=49)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Default''')

        self.Button3 = tk.Button(self.TNotebook1_t2)
        self.Button3.place(relx=0.67, rely=0.153, height=24, width=49)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Default''')

        self.Button2 = tk.Button(self.TNotebook1_t2)
        self.Button2.place(relx=0.631, rely=0.153, height=24, width=30)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Set!''')

        self.Entry1 = tk.Entry(self.TNotebook1_t2)
        self.Entry1.place(relx=0.728, rely=0.028, height=20, relwidth=0.159)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry1 = tk.Entry(self.TNotebook1_t2)
        self.Entry1.place(relx=0.728, rely=0.069, height=20, relwidth=0.159)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry1 = tk.Entry(self.TNotebook1_t2)
        self.Entry1.place(relx=0.728, rely=0.111, height=20, relwidth=0.159)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry1 = tk.Entry(self.TNotebook1_t2)
        self.Entry1.place(relx=0.728, rely=0.153, height=20, relwidth=0.159)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Button2 = tk.Button(self.TNotebook1_t2)
        self.Button2.place(relx=0.893, rely=0.028, height=24, width=30)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Set!''')

        self.Button2 = tk.Button(self.TNotebook1_t2)
        self.Button2.place(relx=0.893, rely=0.069, height=24, width=30)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Set!''')

        self.Button2 = tk.Button(self.TNotebook1_t2)
        self.Button2.place(relx=0.893, rely=0.111, height=24, width=30)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Set!''')

        self.Button2 = tk.Button(self.TNotebook1_t2)
        self.Button2.place(relx=0.893, rely=0.153, height=24, width=30)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Set!''')

        self.Button3 = tk.Button(self.TNotebook1_t2)
        self.Button3.place(relx=0.932, rely=0.028, height=24, width=49)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Default''')

        self.Button3 = tk.Button(self.TNotebook1_t2)
        self.Button3.place(relx=0.932, rely=0.069, height=24, width=49)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Default''')

        self.Button3 = tk.Button(self.TNotebook1_t2)
        self.Button3.place(relx=0.932, rely=0.111, height=24, width=49)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Default''')

        self.Button3 = tk.Button(self.TNotebook1_t2)
        self.Button3.place(relx=0.932, rely=0.153, height=24, width=49)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Default''')

        self.Button2 = tk.Button(self.TNotebook1_t2)
        self.Button2.place(relx=0.631, rely=0.208, height=24, width=92)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Set ALL!!!!''')

        self.Button2 = tk.Button(self.TNotebook1_t2)
        self.Button2.place(relx=0.893, rely=0.208, height=24, width=92)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Set ALL!!!!''')

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


    def value_to_y(self, val):
        return 550 - 5 * val

    def step(self, newY):
        if self.running:
            if self.s == 23:
                # new frame
                self.s = 1
                self.x2 = 50
                self.Canvas1.delete('temp')  # only delete items tagged as temp
            x1 = self.x2
            y1 = self.y2
            self.x2 = 50 + self.s * 50
            self.y2 = self.value_to_y(newY)
            self.Canvas1.create_line(x1, y1, self.x2, self.y2, fill='blue', tags='temp')
            self.s = self.s + 1
            self.Canvas1.after(300, self.step)

    def pause(self):
        if self.running:
            self.running = False
        else:
            self.running = True


if __name__ == '__main__':
    vp_start_gui()



