class Shoe:
    def __init__(self, brand, size, material, condition="Used"):
        self.brand = brand
        self.size = size
        self.material = material
        self.condition = condition
        
    @property
    def size(self):
        return self._size
        
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            raise ValueError("size must be an integer")
        self._size = value
            
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"