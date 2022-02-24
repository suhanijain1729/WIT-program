import random
import string
class Robot(object):
    """docstring for Robot"""
    
    def __init__(self):
        super(Robot, self).__init__()
        random.seed()
        self.reset()
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        self._name = name
        
    def reset(self):
        name = random.sample(
            string.ascii_uppercase, 2) + random.sample(string.digits, 3)
        self._name = ''.join(name)