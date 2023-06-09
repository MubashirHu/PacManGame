class Maze:
    def __init__(self):
        self._rows = 0
        self._columns = 0
        self._cells = self._rows * self._columns
        self._level = []
        
    def _get_number_of_cells(self):
        return self._cells
    
    def _get_number_of_rows(self):
        return self._rows
    
    def _get_number_of_columns(self):
        return self._columns
        
    def _get_level(self, level):
        self._rows = 0
        self._columns = 0 
        
        if level == 1:
            level_file_path = r'levels\lvl1'
        elif level == 2:
            level_file_path = r'levels\lvl2'
        elif level == 3:
            level_file_path = r'levels\lvl3'
        else:
            return "NO PATH FOUND"

        with open(level_file_path) as file:
            for eachline in file:
                self._rows+=1
                self._level.append(eachline)
                #print(eachline)
                
            self._columns = len(self._level[0]) - 1

        print("row count", self._rows)
        print("columns count", self._columns)

        return self._level
        


