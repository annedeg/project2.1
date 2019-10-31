from tkinter import *


class Graph:
    def __init__(self):
        self.s = 1
        self.x2 = 50
        self.y2 = 0
        self.running = True
        self.root = root = Tk()
        self.canvas = Canvas(root, width=1200, height=600, bg='white') #kleur kan veranderen

    def value_to_y(self, val):
        return 550 - 5 * val

    def initialize(self, width, height, colour):

        canvas = Canvas(self.root, width=width, height=height,  # standaard was 1200, 600
                        bg=colour)  # colour moet een string zijn met de naam van de kleur, zoals 'white'
        canvas.pack(expand=YES, fill=BOTH)

        Button(self.root, text='Pause', anchor=E, justify=LEFT, command=self.pause).pack(side=LEFT)  # als het nodig is

        canvas.create_line(50, 550, 1150, 550, width=2)  # x-axis dikke lijn
        canvas.create_text(600, 575, text='Step')  # ik weet niet welke tekst hier moet
        canvas.create_line(50, 550, 50, 50, width=2)  # y-axis dikke lijn
        canvas.create_text(18, 275,
                           text='Value')  # Ziet er echt super slordig uit maar ik weet niet hoe ik die text opzij kan
        # flippen dus hij ziet hier maar ietsje lelijk erbij

        # x-axis
        for i in range(23):
            x = 50 + (i * 50)
            canvas.create_line(x, 550, x, 50, width=1, dash=(2, 5))
            canvas.create_text(x, 550, text='%d' % (10 * i), anchor=N)

        # y-axis
        for i in range(11):
            y = 550 - (i * 50)
            canvas.create_line(50, y, 1150, y, width=1, dash=(2, 5))
            canvas.create_text(40, y, text='%d' % (10 * i), anchor=E)

    def step(self, newY):
        if self.running:
            if self.s == 23:
                # new frame
                self.s = 1
                self.x2 = 50
                self.canvas.delete('temp')  # only delete items tagged as temp
            x1 = self.x2
            y1 = self.y2
            self.x2 = 50 + self.s * 50
            self.y2 = self.value_to_y(newY)
            self.canvas.create_line(x1, y1, self.x2, self.y2, fill='blue', tags='temp')
            self.s = self.s + 1
        self.canvas.after(300, self.step)

    def pause(self):
        if self.running:
            self.running = False
        else:
            self.running = True
