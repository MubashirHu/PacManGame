
def add_shape(obj, i,j, size, shape, color):
    if shape == 0:
        #circle
        x0 = i * size
        y0 = j * size
        x1 = x0 + size
        y1 = y0 + size
        obj._canvas.create_oval(x0, y0, x1, y1, fill=color)
        pass
    elif shape == 1:
        #rectangle
        x0 = i * size
        y0 = j * size
        x1 = x0 + size
        y1 = y0 + size
        obj._canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    else:
        pass