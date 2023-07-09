class Ghost:
    def __init__(self, name, color):
        self._name = name
        self._color = color

        self._position = []
        self._ghost_house_position = []
        self._scatter_target = []
        self._chase_target = []
        self._direction = None
        self._state = None
        self._speed = None
        self._status = None
        self._vulnerability_timer = None

    #setters
    def _set_position(self, row, column):
        self._position.append(row)
        self._position.append(column)

    def _set_direction(self, direction):
        self._direction = direction
        
    def _set_state(self, state):
        self._state = state

    def _set_speed(self, speed):
        self._speed = speed

    def _set_status(self, status):
        self._status = status

    def _set_scatter_target(self, row, column):
        self._scatter_target.append(row)
        self._scatter_target.append(column)

    def _set_chase_target(self, row, column):
        self._chase_target = (row, column)

    def _set_vulnerability_timer(self, timer):
        self._vulnerability_timer = timer

    #getters
    def _get_starting_position(self, ghost_obj, map_obj, _current_level ):
        if ghost_obj._name == "Pinky":  
            for i in range(map_obj._rows):
                for j in range(map_obj._columns):
                    if _current_level[i][j] == "3":
                        self._position.append(i)
                        self._position.append(j)
        elif ghost_obj._name == "Blinky":  
            for i in range(map_obj._rows):
                for j in range(map_obj._columns):
                    if _current_level[i][j] == "4":
                        self._position.append(i)
                        self._position.append(j)
        if ghost_obj._name == "Clyde":  
            for i in range(map_obj._rows):
                for j in range(map_obj._columns):
                    if _current_level[i][j] == "5":
                        self._position.append(i)
                        self._position.append(j)
        if ghost_obj._name == "Inky":  
            for i in range(map_obj._rows):
                for j in range(map_obj._columns):
                    if _current_level[i][j] == "6":
                        self._position.append(i)
                        self._position.append(j)
        
    def _get_direction(self):
        return self._direction
    
    def _get_color(self):
        return self._color
    
    def _get_mode(self):
        return self._mode
    
    def _get_speed(self):
        return self._speed
    
    def _get_status(self):
        return self._status
    
    def _get_scatter_target(self):
        return self._scatter_target
    
    def _get_chase_target(self):
        return self._chase_target
    
    def _get_vulnerability_timer(self):
        return self._vulnerability_timer