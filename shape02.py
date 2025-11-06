class Shape :
    def __init__(self,width,height):
        self.width = width
        self.height = height
    

class Triangle(Shape):
    def get_area(self):
        return(self.width *self.height/2)
    
tri = Triangle(4,6)
print(f'삼각현의밑변: {tri.width}')
print(f'삼각현의밑변: {tri.height}')
print(f'삼각현의밑변: {tri.get_area()}')