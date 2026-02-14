import math
import random
import time

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return self.width*self.height           
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    def get_diagonal(self):
        return math.sqrt(self.width**2+self.height**2)
    def get_picture(self):
        if self.width>50 or self.height>50:
            return "Too big for picture."
        picture=""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture  
    def get_amount_inside(self,shape):
        fit_width=self.width//shape.width
        fit_height=self.height//shape.height
        return fit_width*fit_height

    def spin(self):
        """Rotates the rectangle 90 degrees."""
        self.width, self.height = self.height, self.width

    def get_colored_picture(self):
        """Returns a string picture with a random color."""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[96m"] # Red, Green, Yellow, Blue, Cyan
        reset = "\033[0m"
        c = random.choice(colors)
        return f"{c}{self.get_picture()}{reset}"

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __str__(self):
        return f"Rectangle(width={self.width},height={self.height})"

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
    def set_width(self,side):
        self.width=side
        self.height=side
    def set_height(self,side):
        self.height=side
        self.width=side
    def set_side(self,side):
        self.width=side
        self.height=side        
    def __str__(self):
        return f"Square(side={self.width})"
    
if __name__ == "__main__":
    print("--- Polygon Party ---")
    shapes = []
    for _ in range(5):
        if random.choice([True, False]):
            shapes.append(Rectangle(random.randint(3, 10), random.randint(3, 10)))
        else:
            shapes.append(Square(random.randint(3, 10)))
    
    print("Generating random shapes and sorting them by area...")
    time.sleep(1)
    shapes.sort() # Uses __lt__
    
    for shape in shapes:
        print(f"\n{shape}")
        print(f"Area: {shape.get_area()}")
        print(shape.get_colored_picture())
        time.sleep(0.5)
