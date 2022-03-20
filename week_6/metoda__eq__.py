class Box:
    def __init__(self, capacity: int):
        self.capacity = capacity

    def __eq__(self, other):
        return self.capacity == other.capacity


box1 = Box(10)
box2 = Box(20)
print(box1 == box2)
