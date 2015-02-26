from tkinter import *
from random import random
import math

class Lab:
    #По-умолчанию высота и ширина - 600. Количество ячеек по вертикали и по горизонтали - 40.
    def __init__(self, width = 600, height = 600, horizontal_cells = 40, vertical_cells = 40):
        self.width = width + 1
        self.height = height + 1
        self.vertical_cells = vertical_cells
        self.horizontal_cells = horizontal_cells
        self.vertical_size = height / vertical_cells
        self.horizontal_size = width / horizontal_cells

        self.marks = [[False for i in range(horizontal_cells)] for i in range(vertical_cells)]

        #Создаем окно
        self.master = Tk()

        #создаем canvas - холст для рисования
        self.w = Canvas(self.master, width=self.width, height=self.height)
        # и прикрепляем холст к self.master.
        self.w.pack()

        #очищаем поле, то есть приводим его к начальному состоянию
        self.clear()

    def clear(self):
        #рисуем на холсте белый прямоугольник
        self.background = self.w.create_rectangle(0, 0, self.width, self.height, fill='white', width=1)
        self.background = self.w.create_line(1, 1, self.width, 1)
        self.background = self.w.create_line(1, 1, 1, self.height)
        
        for i in range(self.horizontal_cells):
            for j in range(self.vertical_cells):
                #каждую ячейку очищаем, то есть прорисовываем ее в начальном состоянии
                self.clear_cell(i, j)

                
    #нумерация ячеек с нуля!
    #i - номер столбца
    #j - номер строки
    def fill_cell(self, i, j, color='black', change_fill = True):
        vs = self.vertical_size
        hs = self.horizontal_size

        if i > vs - 1 or j > hs - 1:
        	return

        if change_fill:
        	self.marks[i][j] = True

        #каждая ячейка - это маленький прямоугольник
        self.w.create_rectangle(j*hs + 2, i*vs + 2, (j + 1)*hs + 2, (i + 1)*vs + 2, fill=color, width=1)

    def clear_cell(self, i, j):
    	t = i
    	i = j
    	j = t
    	self.fill_cell(i, j, color = 'white', change_fill = False)
    	self.marks[i][j] = False

    def random_lab(self):
        v = self.vertical_cells
        h = self.horizontal_cells

        for i in range(v*h // 4):
            vert = math.floor(random() * h)+ 1
            hor = math.floor(random() * v) + 1

            self.fill_cell(vert, hor)

    def filled(self, i, j):
    	return self.marks[i][j]