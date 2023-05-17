class maze:
    def __init__(self, rows, column):
        self._rows = rows
        self._columns = column
        self._cells = rows * column

    def _set_maze_width(self, rows, columns):
        self._rows = rows
        self._columns = columns
        
    def _get_number_of_cells(self):
        return self._cells


