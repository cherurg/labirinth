from labyrinth import *
from queue import Queue
import time

cell_size = 20
vertical_cells = 20
horizontal_cells = 20

# создаем лабиринт
l = Lab(cell_size*horizontal_cells, cell_size*vertical_cells, horizontal_cells, vertical_cells)

#создание случайного лабиринта
l.random_lab()

#здесь будем хранить метки
marks = [[float('inf') for i in range(horizontal_cells)]
         for i in range(vertical_cells)]

#начальная ячейка
start = (0, 0)
marks[start[0]][start[1]] = 0
q = Queue()
q.put(start)

end = (19, 19)
while marks[end[0]][end[1]] == None and not q.empty():
    cell = q.get()
    if cell == end:
        break
    
    v = cell[0]
    h = cell[1]
    
    if v > 0 and marks[v - 1][h] == None and not l.filled(v - 1, h):
        marks[v - 1][h] = marks[v][h] + 1
        q.put((v - 1, h))
        l.fill_cell(v - 1, h, color='gray', change_fill = False)

    if h > 0 and marks[v][h - 1] == None and not l.filled(v, h - 1):
        marks[v][h - 1] = marks[v][h] + 1
        q.put((v, h - 1))
        l.fill_cell(v, h - 1, color='gray', change_fill = False)

    if v < vertical_cells - 1 and marks[v + 1][h] == None and not l.filled(v + 1, h):
        marks[v + 1][h] = marks[v][h] + 1
        q.put((v + 1, h))
        l.fill_cell(v + 1, h, color='gray', change_fill = False)

    if h < horizontal_cells - 1 and marks[v][h + 1] == None and not l.filled(v, h + 1):
        marks[v][h + 1] = marks[v][h] + 1
        q.put((v, h + 1))
        l.fill_cell(v, h + 1, color='gray', change_fill = False)


l.fill_cell(end[0], end[1], color='red', change_fill = False)
if marks[end[0]][end[1]] != None:
    cell = end
    while cell != start:

        top = None
        if cell[0] > 0 and not l.filled(cell[0] - 1, cell[1]):
            top = ((cell[0] - 1, cell[1]), marks[cell[0] - 1][cell[1]])
            
        left = None
        if cell[1] > 0 and not l.filled(cell[0], cell[1] - 1):
            left = ((cell[0], cell[1] - 1), marks[cell[0]][cell[1] - 1])
        
        bot = None
        if cell[0] < vertical_cells - 1 and not l.filled(cell[0] + 1, cell[1]):
            bot = ((cell[0] + 1, cell[1]), marks[cell[0] + 1][cell[1]])

        right = None
        if cell[1] < horizontal_cells - 1 and not l.filled(cell[0], cell[1] + 1):
            right = ((cell[0], cell[1] + 1), marks[cell[0]][cell[1] + 1])

        arr = []
        if top != None:
            arr.append(top)
        if left != None:
            arr.append(left)
        if right != None:
            arr.append(right)
        if bot != None:
            arr.append(bot)

        arr = sorted(arr, key=lambda el: el[1])
        cell = arr[0][0]
        l.fill_cell(cell[0], cell[1], color = 'green', change_fill = False)
    
