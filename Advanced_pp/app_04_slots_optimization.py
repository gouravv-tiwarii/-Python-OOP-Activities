class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    p = Point(1, 2)
    print(f"Point: x={p.x}, y={p.y}")
    try:
        p.z = 3  # Not permitted by __slots__
    except AttributeError as e:
        print(f"AttributeError caught: {e}")