from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")


if __name__ == "__main__":
    with tag("b"):
        print("Bold text")