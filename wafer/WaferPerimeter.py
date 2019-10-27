'''
Created on 4 oct. 2019

@author: DavidS
'''

from Shapes import Shape


class WaferPerimeter(Shape):
    '''
    classdocs
    '''
    SECONDARY_FLAT  = {"None":None,"45":45,"90":90,"180":180}
    
    #101.6mm = 4" 
    def __init__(self,x,y,colour,diameterInMillimeters=101.6, primaryFlat=True, secondaryFlat=WaferPerimeter.SECONDARY_FLAT.get("None")):
        
        Shape(WaferPerimeter, self).__init__(x, y, colour)
        self.diameterInMillimeters=diameterInMillimeters
        self.primaryFlat=primaryFlat
        if WaferPerimeter.SECONDARY_FLAT.get(secondaryFlat)==None:
            self.secondaryFlat=None
            raise AttributeError('Secondary Flat not allowed')
          
        