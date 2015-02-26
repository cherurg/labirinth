from labyrinth import *

#создаем поле
l = Lab(600, 600, 4, 4)

#закрашиваем ячейку
l.fill_cell(2, 3, 'black')

#через 5000 мс очищаем ее
l.master.after(5000, lambda: l.clear_cell(2, 3))
