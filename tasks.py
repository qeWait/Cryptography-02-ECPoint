from ECPoint import ECPoint, AddECPoints

point1 = ECPoint(3, 4)
point2 = ECPoint(1, 0)

point3 = AddECPoints(point1, point2)
point3.PrintECPoint()

point4 = point3.DoubleECPoint()
point4.PrintECPoint()

point5 = point3.ScalarMult(3)
point5.PrintECPoint()

print(point1.IsOnCurveCheck(), point2.IsOnCurveCheck(), point3.IsOnCurveCheck(), point4.IsOnCurveCheck(), point5.IsOnCurveCheck())