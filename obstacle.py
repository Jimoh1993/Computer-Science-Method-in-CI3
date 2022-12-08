from abc import ABC, abstractmethod
import numpy as np

class Obstacle(ABC):
    
    @abstractmethod
    def distance(self, x):
        pass
    
    @abstractmethod
    def is_inside(self, x):
        pass
    
class Rectangle(Obstacle):
    
    def __init__(self):
        self._lower_right = np.zeros([1, 2])
        self._width = float(100)
        self._height = float(5)
    
    @property
    def lower_right(self):
        return self._lower_right()

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
    
    @lower_right.setter
    def lower_right(self, lower_right: np.ndarray):
        self._lower_right = lower_right
        return self._lower_right

    @width.setter
    def width(self, width: float):
        self._width = width
        return self._width

    @height.setter
    def height(self, height: float):
        self._height = height
        return self._height
    
    def is_inside(self, x):
        rect_min = self._lower_right
        rect_max = np.copy(rect_min)
        rect_max[:,0] = self._width
        rect_max[:,1] = self._height
        condition_1 = x>=rect_min
        condition_2 = x<=rect_max
        condition_3 = condition_1*condition_2
        return int(np.sum(condition_3, axis=1)) == int(2)
    
    def distance(self, x):
        rect_min = self._lower_right
        rect_max = np.copy(rect_min)
        rect_max[:,0] = self._width
        rect_max[:,1] = self._height
        if self.is_inside(x) == False:
            s = np.stack((rect_min-x, np.zeros(np.shape(rect_min)), x-rect_max), axis=2)
            d = np.max(s, axis=2)
            m = np.zeros(np.shape(rect_min))
            m[:,0] = d[:,0]
            m[:,1] = d[:,1]
            
            check_0 = -1*(s[:,:,0]==d)
            check_2 = +1*(s[:,:,2]==d)
        
            check_3 = check_0 + check_2
            
            if (abs(check_3-np.zeros(np.shape(check_3))) < 1e-6).all():
                check_3 = check_0
            else:
                pass
            
            dist = check_3*d
        else:
            s = np.stack((x-rect_min, rect_max-x), axis=2)
            m = np.min(s, axis=2)
            n = (m == np.min(m, axis=1))
            d = m*n
            
            o = np.zeros(np.shape(rect_min))
            o[:,0] = d[:,0]
            o[:,1] = d[:,1]
            
            check_0 = -1*(s[:,:,0]==d)
            check_1 = +1*(s[:,:,1]==d)
        
            check_2 = check_0 + check_1
            
            if (abs(check_2-np.zeros(np.shape(check_2))) < 1e-6).all():
                check_2 = check_0
            else:
                pass
            
            dist = check_2*d
        return dist
    
    
    
