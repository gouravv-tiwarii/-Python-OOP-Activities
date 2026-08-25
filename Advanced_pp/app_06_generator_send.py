def running_total():
    total = 0
    while True:
        val = yield total
        if val is None:
            break
        total += val


if __name__ == "__main__":
    calc = running_total()
    next(calc)             # Prime generator
    print(calc.send(10))   # 10
    print(calc.send(25))   # 35