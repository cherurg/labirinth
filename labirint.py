from tkinter import *

class Lab:
    #По-умолчанию высота и ширина - 600. Количество ячеек по вертикали и по горизонтали - 40.
    def __init__(self, width = 600, height = 600, vertical_cells = 40, horizontal_cells = 40):
        self.width = width
        self.height = height
        self.vertical_cells = vertical_cells
        self.horizontal_cells = horizontal_cells
        self.vertical_size = height / vertical_cells
        self.horizontal_size = width / horizontal_cells

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
        self.background = self.w.create_rectangle(0, 0, self.width, self.height, fill='white')
        
        for i in range(self.horizontal_cells):
            for j in range(self.vertical_cells):
                #каждую ячейку очищаем, то есть прорисовываем ее в начальном состоянии
                self.clear_cell(i, j)

                
    #нумерация ячеек с единицы, а не с нуля
    #i - номер столбца
    #j - номер строки
    def fill_cell(self, i, j, color='white'):
        vs = self.vertical_size
        hs = self.horizontal_size
        
        #каждая ячейка - это маленький прямоугольник
        self.w.create_rectangle((i - 1)*hs, (j - 1)*vs, i*hs, j*vs, fill=color)

    def clear_cell(self, i, j):
        #вызываем функцию заполнения ячейка со значением color по-умолчанию, т.е. white
        self.fill_cell(i, j)


#создаем поле
l = Lab(600, 600, 40, 40)

#закрашиваем ячейку
l.fill_cell(20, 10, 'black')

#через 5000 мс очищаем ее
l.master.after(5000, lambda: l.clear_cell(20, 10))
