class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Values must be positive. No negatives allowed.")

        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


# Example 
if __name__ == "__main__":
    try:
        h = float(input("Enter height: "))
        w = float(input("Enter width: "))

        rectangle = Rectangle(w, h)

        print(rectangle.get_area())
        print(rectangle.get_perimeter())

    except ValueError as e:
        print(e)