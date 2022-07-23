data1 = int(input("Value"))
data2 = int(input("Value"))

def calc(x, y):
    print("+", x + y, sep="|")
    print("-", x - y, sep="|")
    print("*", x * y, sep="|")
    print(":", x / y, sep="|")
calc(data1, data2)