import math    # to get radius

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)



# Example 
if __name__ == "__main__":
    r = float(input("Enter radius: "))
    circle = Circle(r)
    print("Area:", circle.get_area())