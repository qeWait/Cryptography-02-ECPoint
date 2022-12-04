equation = {
    "a": int(input("Введіть параметр `a` для рівнянна: ")),
    "b": int(input("Введіть параметр `b` для рівнянна: ")),
}

print(f'Рівнянн еліптичної кривої: y^2 = x^3 + {equation["a"]}x + {equation["b"]}')

class ECPoint:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def ECPointToString(self) -> str:
        return f"[{round(self.x, 1)}, {round(self.y, 1)}]"

    def PrintECPoint(self) -> None:
        print(self.ECPointToString())

    def DoubleECPoint(self):
        x = ( (3*self.x**2 + equation['a']) / (2*self.y) )**2 - 2*self.x
        y = -self.y + ( (3*self.x**2 + equation['a']) / (2*self.y) ) * (self.x - x)

        return ECPoint(int(x), int(y))

    def ScalarMult(self, n: int):
        x = self.x * n
        y = self.y * n

        return ECPoint(int(x), int(y))

    def IsOnCurveCheck(self):
        return self.y**2 == int((self.x**3 + equation['a']*self.x + equation['b']))

def AddECPoints(P: ECPoint, Q: ECPoint) -> ECPoint:
    m = (P.y - Q.y) / (P.x - Q.x)

    x = m**2 - P.x - Q.x
    y = P.y + m * (x - P.x)

    return ECPoint(int(x), int(y))