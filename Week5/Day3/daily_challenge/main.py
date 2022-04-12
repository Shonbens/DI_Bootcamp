class Circle:

    def __init__(self, radius):
        print("Created by __innit__")
        pass

    @classmethod
    def from_diameter(cls, diameter):
        print("created by class method")
        pass


circle = Circle(radius=2)
Circle.from_diameter(diameter=2)



