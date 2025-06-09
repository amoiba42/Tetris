class Color:
    dark_grey=(26,31,40)
    green=(0,255,0)
    red=(255,0,0)
    orange=(255,165,0)
    yellow=(255,255,0)
    blue=(0,0,255)
    purple=(128,0,128)
    cyan=(0,255,255)
    white=(255,255,255)
    dark_blue=(0,0,139)
    light_blue=(59,85,162)
    
    @classmethod                                                                                       #classmethod is a python decorator, it is used to define a method that is bound to the class rather than its object
    def get_cell_colors(cls):
        return[cls.dark_grey,cls.green,cls.red,cls.orange,cls.yellow,cls.blue,cls.purple,cls.cyan]
  