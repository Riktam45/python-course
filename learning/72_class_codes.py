class calculator:
    def add(self, a, b):
        return a + b
    def multiply(self, a, b):
        return a * b
class_calc = calculator()
print(class_calc.add(5, 3))
print(class_calc.multiply(3, 8))

class cal:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def cal(self):
        return f"sum: {self.a + self.b}, multiply: {self.a * self.b}"
calc = cal(2,4)
print(calc.cal())