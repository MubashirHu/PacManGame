class Ghost:
    def __init__(self, color):
        self._coordinate = (0,0)
        self._direction = ""
        self._color = color
        self._mode = 0
        self._speed = 0
        self._status = 0
        self._scatter_target = (0,0)
        self._chase_target = (0,0)
        self._vulnerability_timer = 0

    #setters
    def _set_coordinate(self, row, column):
        self._coordinate = (row,column)

    def _set_direction(self, direction):
        self._direction = direction

    def _set_color(self, color):
        self._color = color

    def _set_mode(self, mode):
        self._mode = mode

    def _set_speed(self, speed):
        self._speed = speed

    def _set_status(self, status):
        self._status = status

    def _set_scatter_target(self, row, column):
        self._scatter_target = (row, column)

    def _set_chase_target(self, row, column):
        self._chase_target = (row, column)

    def _set_vulnerability_timer(self, timer):
        self._vulnerability_timer = timer

    #getters
    def _get_coordinate(self):
        return self._coordinate
    
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

